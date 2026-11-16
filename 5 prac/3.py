# Константы
USD_TO_RUB = 95.50

#Функция по конвертации
def convert_usd_to_rub(amount_usd):
    """
    Конвертирует доллары в рубли

    :param amount_usd: кол-во долларов (float)
    :return: возвращает рассчитанную сумму в рублях (float)
    """
    return amount_usd * USD_TO_RUB

# Запрос на ввод данных
dollars = float(input("Введите сумму в долларах: "))

# Вызываем функцию для конвертации и записываем в переменную
rubles = convert_usd_to_rub(dollars)

# Выводим данные
print(f"{dollars:.2f} долларов - это {rubles:.2f} рублей")