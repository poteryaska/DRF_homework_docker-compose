Задание 1
Подключить и настроить вывод документации для проекта. 
Убедиться, что каждый из реализованных эндпоинтов описан в 
документации верно, при необходимости описать вручную.

Задание 2
Подключить возможность оплаты курсов через https://stripe.com/docs/api.
Доступы можно получить напрямую из документации, а также пройти простую 
регистрацию по адресу https://dashboard.stripe.com/register.

Для работы с запросами вам понадобится реализовать обращение к эндпоинтам:
https://stripe.com/docs/api/payment_intents/create — создание платежа;
https://stripe.com/docs/api/payment_intents/retrieve — получение платежа.
Для тестирования можно использовать номера карт из документации:

https://stripe.com/docs/terminal/references/testing#standard-test-cards
Подключение оплаты лучше всего рассматривать как обычную задачу подключения 
к стороннему API.

Основной путь: запрос на покупку → оплата. Статус проверять не нужно.
Каждый эквайринг предоставляет тестовые карты для работы с виртуальными деньгами.

* Дополнительное задание
Реализуйте проверку статуса с помощью эндпоинта 
* https://stripe.com/docs/api/payment_intents/retrieve — получение платежа.