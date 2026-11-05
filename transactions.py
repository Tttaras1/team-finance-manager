def delete_transaction(transactions, transaction_id):
    """видаляє транзакцію"""
    if 0 <= transaction_id < len(transactions):
        removed = transactions.pop(transaction_id)
        return transactions, f"видалено транзакцію {removed}"
    return transactions, "помилка. транзакцію не знайдено"

def filter_by_category(transactions, category):
    """фільтрує та виводить транзакцію за категорією"""
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