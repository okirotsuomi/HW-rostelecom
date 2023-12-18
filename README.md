Тестирование авторизации в ЛК "Ростелеком" 

Требования описаны в брифе от заказчика https://docs.yandex.ru/docs/view?url=ya-browser%3A%2F%2F4DT1uXEPRrJRXlUFoewruPwX_lHu6GpoiWPB8D0k-cl5xpAmQ254GHeqxfXKrTadMzM9Bto04ul6NVRRpGTXz_D0vK-RGTKj88X4kOEYItld23L2cjpHJQXiauuX-EeLmtWu0egchdr9wM6MyVp7Bw%3D%3D%3Fsign%3DU-LmCFGluDIJ5uWNPjwWhOzfytokVxqCYhjzxqj1LPY%3D&name=asset-v1_SkillFactory%2BQAP-3.0%2B2021%2Btype%40asset%2Bblock%40Требования_SSO_для_тестирования_last.doc

Реализованы тесты к "Стандартная авторизация по логину и паролю"

Тест-кейсы https://docs.google.com/spreadsheets/d/1tCEcc3-rVcjAXImIxBrjg8sRKYgPOa9U/edit?usp=sharing&ouid=108335243803342499514&rtpof=true&sd=true
На вкладке "Форма авторизации" описаны тест-кейсы по проверке наличия на странице авторизации всех описанных в требованиях элементов
На вкладке "Авторизация" описаны тест-кейсы по авторизации в ЛК Ростелеком
Найденные баги описаны на вкладке "Баги" в документе с тест-кейсами

При создании тест-кейсов использованы техники позитивного тестирования для проверки авторизации на сайте различными способами, описанными в технических требованиях, и негативного тестирования для проверки невозможности доступа в личный кабинет с неподходящими данными и оповещения пользователя об ошибке доступа. В негативном тестировании используются классы эквивалентности для подбора вариантов данных для тестов.

При проведении тестов возможно появление капчи в форме авторизации. В этом случае сразу после ввода данных в полях логин и пароль нужно кликнуть в поле ввода капчи и за 15 сек. ввести текст с картинки. Если не успеть это сделать, тест будет провален.

Негативные тесты на авторизацию с пустым паролем отмечены как xfail, т.к. все время падают - на сайте нет предупреждения о вводе пароля.


Инструменты, которые применялись для тестирования:
Для тестирования сайта был использован интсрумент Selenium;
Для определения локаторов использовались следующие инструменты: DevTools, ChroPath.
Запуск тестов:
python -m pytest -v --driver Chrome --driver-path C:/projects/Skillfactory/chromedriver.exe tests/test_auth_page_elements.py
python -m pytest -v --driver Chrome --driver-path C:/projects/Skillfactory/chromedriver.exe tests/test_negative_auth.py
python -m pytest -v --driver Chrome --driver-path C:/projects/Skillfactory/chromedriver.exe tests/test_positive_auth.py
