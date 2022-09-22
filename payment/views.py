import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Item, Order


def item_list(request):
    """

    @param request:
    @return: Возвращем главную страничку магазина
    """
    items = Item.objects.all()
    return render(request, 'payment/list.html', context={'items': items})


def get_contract(kwargs: dict) -> dict:
    """
    Функция сериализации разнородных типов Item, Order к универсальному объекту Контракт.
    Контракт может обслуживать и отдельные Item, и Order c многочисленными Item внутри.

    @type kwargs: Путь запроса {'item_id': <id>}

    @return Возращаем универсальный контракт (словарь)
    """
    contract = dict()
    for key, obj_id in kwargs.items():
        contract['subtype'] = key.split('_')[0]
        contract['id'] = obj_id
        obj_name = contract['subtype'].capitalize()
        obj = get_object_or_404(globals()[obj_name], pk=obj_id)

        if contract['subtype'] == 'order':
            contract['name'] = obj
            contract['description'] = f"Количество товаров: {obj.get_count()}"
            contract['price'] = obj.get_price()

        elif contract['subtype'] == "item":
            contract['name'] = obj.name
            contract['description'] = obj.description
            contract['price'] = obj.price
            try:
                contract['icon'] = obj.icon.url
            except ValueError as e:
                print("Иконки нет!")
        else:
            raise ValueError
        return contract


@csrf_exempt
def create_checkout_session(request, **kwargs):
    if request.method == 'GET':
        contract = get_contract(kwargs)
        domain_url = f'{request.scheme}://{request.get_host()}/'
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': contract['name'],
                            'description': contract['description'],
                            # 'images': ['https://picsum.photos/280/320?random=4']
                        },
                        'unit_amount_decimal': contract['price'] * 100,
                    },
                    'quantity': 1,
                }],

            )
            return JsonResponse({
                'sessionId': session['id'],
                'publicKey': settings.STRIPE_PUBLISHABLE_KEY
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def contract_detail(request, **kwargs):
    if request.method == 'GET':
        context = {'contract': get_contract(kwargs), }
        return render(request, 'payment/get_button.html', context=context)


def cancelled(request):
    return render(request, template_name="payment/cancel.html")


def success(request):
    return render(request, template_name="payment/success.html")
