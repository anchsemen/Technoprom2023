# Technoprom2023
## Задача проекта
Задача проекта состоит в том, чтобы автоматически собрать информацию о стратегических проектах университетов, участвующих в программе "Приоритет 2030" с веб-сайта priority2030.ru. Это включает в себя извлечение названий стратегических проектов и их кратких описаний, если они доступны. Всего в программе участвует 129 университетов, и у каждого из них на сайте есть свой раздел с описанием стратегических проектов. Необходимо все было оформить в Excel-таблицу, в которой находятся следующие столбцы: Университет, сайт программ, название программы, Описание стратегического проекта, Цель стратегического проекта, Задачи стратегического проекта, Ожидаемые результаты стратегических проектов, а также столбец с обозначением проекта - спецчасть (1) / базовый (0).

Далее необходимо было, используя метод машинного обучения определить какие ключевые слова или фразы могут помочь отделить стратегические проекты университетов базовой части от стратегических проектов спец. части на основе их описаний. 

Происходило это следующим образом:
1. В каждом описании проектов необходимо было удалить стоп-слова (ненужные), произвести лемматизацию (приведение слова к его базовой форме) 
2. Каждое описание векторизировали с помощью TF-IDF (мера, используемая для оценки важности слова в контексте документа)
3. С помощью модели DecisionTreeClassifier на основе векторизированных данных оценивали каждый проект (куда относится проект по их описаниям)

Результаты точности модели: accuracy - 0.85, recall - 0.615.

Один из результатов предсказания модели можно посмотреть в decision_tree.pdf

Также есть <a href="https://vk.com/video-215675438_456239224">видеопрезентация</a> проекта от моего научного руководителя Павловского Евгения Николаевича.
