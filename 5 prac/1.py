# Константы
TAX_RATE = 13

# Запрос на ввод данных
income = float(input("Введите свой годовой доход:"))

# Расчитываем сумму налога и сумму после вычета
income_tax = income * TAX_RATE / 100
paid_income = income - income_tax

# Вывод данных
print(f"Общая сумма дохода: {income:,.2f} ₽")
print(f"Налог: {income_tax:,.2f} ₽")
print(f"Общая сумма дохода после вычета налога: {paid_income:,.2f} ₽")