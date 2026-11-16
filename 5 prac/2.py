weight, height = map(float, input('Введите вес (кг) и рост (м): ').split())

iwh = weight / height**2

print(f'Ваш индекс массы тела: {iwh:.1f}')