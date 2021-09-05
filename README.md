# Wargaming red test task
Реализовано веб приложение для подсчета показателей TF и IDF для переданного в качестве исходных данных txt файла.
Данные хранятся с использованием базы данных MongoDB на локальном хосте mongodb://localhost:27017/.
Каждый загруженный текстовый файл является сущностью БД и имеет следующую структуру {слово:{IF:int, IDF: float}}.
Для реализации веб приложения был использоан фреймворк Flask.

**Руководство по установке и использованию:**
* 1)Склонировать данный репозиторий (команда: git clone https://github.com/fl1p3mth3b1rd/Wargaming_red_test_task)
* 2)Установить все зависимости (команда: pip install -r requirements.txt)
* 3)Скопировать http://127.0.0.1:5000/ в поисковую строку браузера и нажать Enter
* 4)Нажать на кнопку "выберите файл", выбрать файл txt нажать загрузить
* 5)Получить ответ в виде таблицы со столбцами "Слово", "TF", "IDF".
