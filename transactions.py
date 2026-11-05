def delete_transaction(transactions, transaction_id):
    """
    видаляє транзакцію за унікальним індексом або ID

    агрументи:
        transactions (list) - список поточних транзакцій
        transaction_id (int)- індекс транзакції для видалення

    повертає:
        оновлений список транзакцій та повідомлення про статус
    """
    if 0 <= transaction_id < len(transactions):
        removed = transactions.pop(transaction_id)
        return transactions, f"видалено транзакцію {removed}"
    return transactions, "помилка. транзакцію не знайдено"


def filter_by_category(transactions, category):
    """
    фільтрує та виводить транзакцію за категорією

    аргументи:
        transactions (list) - список поточних транзакцій
        category (str) - назва категорії для фільтрації

    повертає:
        список відфільтрованих транзакцій
    """
    category_lower = category.strip().lower()
    filtered = [t for t in transactions if t["category"].lower() == category_lower]

    if not filtered:
        print("транзакцію у категорії не знайдено")
    else:
        print("відфільтровані транзакції для категорії")
        print(f"{'ID'} | {'Type'} | {'Amount'} | {'Category'} | {'Description'}")
        for t in filtered:
            print(
                f"{t['id']} | {t['type']} | {t['amount']} | {t['category']} | {t['description']}"
            )
        return filtered


def show_transactions(transactions: list) -> None:
    """
    Показує відформатовані транзакції
    Args:
        transactions: Список транзакцій
    Returns:
        None
    """

    fields = ["id", "type", "amount", "category", "description"]
    column_width = 16

    for field in fields:
        print(f"{field.upper():^{column_width - 1}}|", end="")

    print("\n", "-" * column_width * len(fields))

    for transaction in transactions:
        for field in fields:
            print(f"{str(transaction[field]):^{column_width - 1}}|", end="")

        print()


last_id = 0


def add_transaction(
    transactions: list,
    transaction_type: str,
    amount: float,
    category: str,
    description: str,
) -> None | list:
    """
    Створює транзакцію

    Args:
        transactions: Існуючий список транзакцій
        transaction_type: Тип ( income або expense )
        amount: Сума транзакції
        category: Категорія
        description: Опис
    """
    if amount <= 0:
        print("Сума повинна бути позитивна")
        return None
    if transaction_type not in ["income", "expense"]:
        print("Транзакція повинна бути income or expense")
        return None
    if not category or not description:
        print("Категорія і опис не повинні бути порожніми!")
        return None

    global last_id

    transaction = {
        "id": last_id,
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description,
    }
    last_id += 1
    transactions.append(transaction)

    return transactions
