# Описание проекта
В проекте определяется банковский кредитный скоринг клиента.

[Исходная выборка ](https://www.kaggle.com/datasets/kapturovalexander/bank-credit-scoring/data)

# Запуск проекта
Для запуска необходимо выполнить команды:
```
git clone https://github.com/KochurovaVA/IIS.git
cd /IIS/
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
# Исследование

Находится в `C:/home/mainuser/my_proj/eda/eda.ipynb`. 

При исследовании:
* Удалены признаки "pdays","previous", "poutcome" ввиду отсутствия их смысла
* Не обнаружено аномальных значений признаков, которые идут вразрез с их физическим смыслом
* Столбцам 'job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'y' присвоен категориальный тип
* Столбцам 'age', 'balance', 'day', 'duration', 'campaign' был присвоен соответсвующий тип данных, который подходит под конкретный "разброс" значений

Были выявлено: 
* В менеджменте баланс клиента в среднем больше, чем у студента (график `./eda/graph1.png`)
* Слабая корелляция признаков (график `./eda/graph2.png`)
* Женатым клиентам чаще отказывают в выдаче кредита, чем разведённым или холостым (график `./eda/graph3.png`)
* Зависимость текущего баланса от возраста (график `./eda/graph4.png`)

Обработанная выборка сохранена в файл `./data/clean_data.pkl`