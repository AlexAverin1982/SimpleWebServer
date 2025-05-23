# Курсовая работа "Приложение для поиска вакансий на сайте HeadHunter.ru и локальной обработки найденной информации"
## Цель домашней работы
Используя навыки, полученные в ходе изучения ООП, разработать приложение, получает информацию через API сайта,
и может эту информацию сортировать, фильтровать, сохранять в файлы разных форматов и загрузажать ее из этих файлов.
Также добавлена возможность сохранять информацию о вакансиях и работодателях в базу данных.

## Возможности приложения
+ Формирование параметров поиска инфорамции о вакансиях в интерактивном режиме;
+ Поиск вакансий с указанными параметрами или без них (в пределах России - по умолчанию);
+ Отображение списка кратких описаний всех найденных вакансий;
+ Отображение детальной информации вакансий - как всех, так и только выбранных указанием порядковых номеров
  и их диапазонов в списке найденных вакансий с учетом текущей сортировки;  
+ Фильтрация найденных вакансий с использованием изменных параметров поиска;
+ Сортировка найденных вакансий по различным параметрам (зарплата, заголовок вакансии, работодателя, и т.п.)
+ Удаление вакансий из набранных путем указания порядковых номеров и их диапазонов в списке всех вакансий с учетом 
  текущей сортировки.
+ Сохранение вакансий в файлы разных форматов (txt, json).
+ Загрузка вакансий из файлов разных форматов (txt, json) с учетом или без текущих поисковых параметров.
+ При наличии сетевого или локльного сервера PostgreSQL пользователь приложения может создавать
  базу данных с нуля, дописывать в нее данные и получать из нее некоторые данные в виде
результата заранее сохраненных запросов к базе. Доступ к базе возможет и при отсутствии доступа к интернету.

## Структура проекта
#### + Исходный код функционала приложения находится в папке `src`
  + модуль `main` - точка входа приложения, отображает главное меню приложения для навигации по компонентам программы;
#### + Тесты работы исходного кода находится в папке `tests`
#### + Данные, с которыми будет работать приложение находятся в папке `data`
#### + Настройки для быстрого подключения к базам даных находятся в папке `settings`
#### + Данные отчета о покрытии кода тестами находятся в папке htmlcov
Основновная информация доступна через файл `index.html`



## Инструкции по использованию приложения
- Запустите модуль `.\main.py`, следуйте инструкциям на экране
- Отдельными компонентами можно пользоваться, импортируя их из соответствующих модулей папки `src`

