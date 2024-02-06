# A test assignment for the company "UpTrader" 
The project was completed as a test assignment for an interview with the company

## Technical specification
> ### Задание:
> Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
> 1. Меню реализовано через template tag
> 2. Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
> 3. Хранится в БД.
> 4. Редактируется в стандартной админке Django
> 5. Активный пункт меню определяется исходя из URL текущей страницы
> 6. Меню на одной странице может быть несколько. Они определяются по названию.
> 7. При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
> 8. На отрисовку каждого меню требуется ровно 1 запрос к БД
> 
> ### Результат:
> Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
> ```html
>  {% draw_menu 'main_menu' %}
> ```
> При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.


## Launch for testing
1. Create an .env file and specify the following parameters:
   * DEBUG - responsible for the operation mode of the project
   * SECRET_KEY - responsible for data encryption
   * DOMAIN_NAME - responsible for the domain name on which the service will be raised
2. Create a virtual environment and activate it (python version 3.10.4 was used when creating the project):
```cmd
   python -m venv venv
```
   * Activate virtual environment in Windows
```cmd
   venv\Scripts\activate
```
   * Activate virtual environment in Linux/Mac
```cmd
   source venv/bin/activate
```
3. Installing dependencies
```pip
   pip install -r requirements.txt
```
4. Database migration and creation of a superuser
```cmd
   python manage.py migrate
   python manage.py createsuperuser
```
5. Project Launch
```cmd
   python manage.py runserver DOMAIN_NAME
```