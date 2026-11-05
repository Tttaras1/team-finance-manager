import transactions as transaction_module
import statistics as statistics_module


def main():
    transactions = []
    while True:
        print(
            "\n========== FINANCE MANAGER ==========\n\n"
            "1. Додати дохід\n"
            "2. Додати витрату\n"
            "3. Переглянути всі транзакції\n"
            "4. Показати загальний дохід\n"
            "5. Показати загальні витрати\n"
            "6. Показати поточний баланс\n"
            "7. Фільтрація за категорією\n"
            "8. Видалити транзакцію за ID\n"
            "0. Вихід\n"
        )
        choice = input("Оберіть дію: ").strip()
        if choice in ("1", "2"):
            transaction_type = "income" if choice == "1" else "expense"
            try:
                amount = float(input("Сума: "))
            except ValueError:
                print("Введіть коректне число для суми.")
                continue
            category = input("Категорія: ").strip()
            description = input("Опис: ").strip()
            transaction_module.add_transaction(
                transactions,
                transaction_type,
                amount,
                category,
                description,
            )
        elif choice == "3":
            transaction_module.show_transactions(transactions)
        elif choice == "4":
            print(
                f"Загальний дохід: {statistics_module.calculate_income(transactions):.2f}"
            )
        elif choice == "5":
            print(
                f"Загальні витрати: {statistics_module.calculate_expenses(transactions):.2f}"
            )
        elif choice == "6":
            print(
                f"Поточний баланс: {statistics_module.calculate_balance(transactions):.2f}"
            )
        elif choice == "7":
            category = input("Категорія: ").strip()
            transaction_module.show_transactions(
                transaction_module.filter_by_category(transactions, category)
            )
        elif choice == "8":
            try:
                transaction_id = int(input("ID транзакції: "))
            except ValueError:
                print("Введіть ціле число для ID.")
                continue
            _, message = transaction_module.delete_transaction(
                transactions, transaction_id
            )
            print(message)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невідома дія. Оберіть пункт від 0 до 8.")


if __name__ == "__main__":
    main()
