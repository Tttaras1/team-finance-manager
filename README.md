# Financial Tracker Application

Навчальна Python-програма для обліку доходів і витрат. Дані зберігаються у списку Python під час роботи програми; збереження у файл або базу даних поки не реалізоване.

## Можливості

- Додавати до списку транзакцію типу `income` або `expense` із сумою, категорією та описом.
- Переглядати транзакції у табличному форматі.
- Видаляти транзакцію за її ID.
- Обчислювати загальний дохід, витрати та баланс.
- Фільтрувати транзакції за категорією без урахування регістру.

Для суми дозволені лише додатні значення. Тип транзакції має бути `income` або `expense`, а категорія й опис — непорожніми.

## Структура проєкту

```text
git_overview/
├── transactions.py  # додавання, перегляд і видалення транзакцій
├── statistics.py    # підрахунки та фільтр за категорією
└── README.md        # опис проєкту та інструкція
```

## Запуск

Потрібен Python 3.10 або новіший. Залежностей від сторонніх пакетів немає.

```bash
cd git_overview
python3 transactions.py
```

Зараз `transactions.py` демонструє виведення порожнього списку. Щоб використовувати функції як частину сценарію, імпортуйте їх і передавайте спільний список транзакцій. Модулі наразі не мають інтерактивного меню й не зберігають дані між запусками.

## Приклади використання

Після виправлення імпорту `List` у `transactions.py` (див. примітку нижче) функції можна використовувати так:

```python
from transactions import add_transaction, show_transactions, delete_transaction
from statistics import (
    calculate_income,
    calculate_expenses,
    calculate_balance,
    filter_by_category,
)

transactions = []
add_transaction(transactions, "income", 2500, "Зарплата", "Зарплата за жовтень")
add_transaction(transactions, "expense", 350, "Їжа", "Обід")

show_transactions(transactions)
print("Дохід:", calculate_income(transactions))       # 2500
print("Витрати:", calculate_expenses(transactions))   # 350
print("Баланс:", calculate_balance(transactions))    # 2150
print("Їжа:", filter_by_category(transactions, "їжа"))
delete_transaction(transactions, 1)
```

## Поточні обмеження

- `transactions.py` анотує аргумент `show_transactions` типом `List`, але не імпортує `List`. Python видає `NameError` під час імпорту модуля. Для прикладів вище додайте на початок файла `from typing import List` (або замініть `List` на `list`).
- ID створюються як цілі числа, тому для видалення передавайте число, наприклад `1`.
- Список транзакцій живе лише в пам’яті процесу; після завершення програми дані зникають.
