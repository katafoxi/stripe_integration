# Интеграция со Stripe
----
## О проекте

Простой сервер с html страничкой магазина, настроенной админкой, который общается со Stripe и создает платёжные формы для товаров. 
![2022-09-21 23_25_32-Products](https://user-images.githubusercontent.com/83884504/191699259-8d1ca276-fd1d-43fc-90c6-b19d64817548.png)

----
### Запуск контейнеров
Клонируем репозиторий, после выполняем команду.

```shell
docker-compose up -d

```
Опционально доступен PgAdmin  [http://localhost:5050/](http://localhost:5050/)

----
После запуска контейнеров идем по адресу [http://localhost:8080/admin](http://localhost:8080/admin).

login: root  | password: 123

Создаем Item(товары), Order(Заказы) и идем по адресу [http://localhost:8080/](http://localhost:8080/)

Опционально на товары можно вешать иконки/картинки.

![2022-09-22 11_19_57-Buy Item {contract id}](https://user-images.githubusercontent.com/83884504/191699396-b85cdb69-4c3b-406e-8685-bbd49f53f6c4.png)
![image](https://user-images.githubusercontent.com/83884504/191699677-55a359eb-8ce2-43b5-aa4b-30b2916f0167.png)


### Используемый стек

1) Django.
2) Stripe.
3) PostgreSQL
4) Docker


## Задание
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
1) Django Модель Item с полями (name, description, price) 
2) API с двумя методами:
GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
----
## Дополнительно
- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели
- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
