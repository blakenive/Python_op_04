num = int(input("Введите 4-х значное число:"))
thousand = num // 1000
hngrd = num//100%10
tens = num//10%10
one = num%10
print("Цифра в позиции тысяч равна", thousand)
print("Цифра в позиции сотен равна", hngrd)
print("Цифра в позиции десяток равна", tens)
print("Цифра в позиции единиц равна", one)
