from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path

from conf import settings
from .views import *

urlpatterns = [
                  path('', item_list, name='product_list'),
                  path("item/<int:item_id>", contract_detail, name='item_detail'),
                  path("order/<int:order_id>", contract_detail, name='order_detail'),
                  path("buy/<int:item_id>", create_checkout_session, name='buy_item'),
                  path("buy_order/<int:order_id>", create_checkout_session, name='buy_order'),
                  path("cancelled/", cancelled, name='cancel'),
                  path("success/", success, name='ok'),
                  # path('order/<int:order_id>', create_checkout_session, name='buy_order')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
