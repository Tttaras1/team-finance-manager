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
            print(f"{t['id']} | {t['type']} | {t['amount']} | {t['category']} | {t['description']}")
        return filtered