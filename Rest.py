import random 

menuList = [' 1. Котлета;\n', '2. Салат;\n', '3. Курка варена;\n', '4. Бургер;\n', '5. Борщ;\n', '6. Суп;\n']
offer = input('Ласкаво просимо до нашого ресторану.\nЯкщо бажаєте ознайомитись з меню, напишіть Так, якщо ні - Ні  \n')
if offer=='Ні':
    print("Запропонуйте свої страви, наш повар виконає всі ваші побажання!")
if offer=='Так':
    print('Меню:\n' + ' '.join(menuList))
menu = input('Щоб зробити замовлення, будь-ласка, введіть назви обраних Вами страв через кому:\n\n')
menu = menu.split(',')
bill = 0

print('\n   Кафе “У Монті”   ')

for dish in menu:
    price=random.randint(1,100)
    bill =  bill + price
    print(f'{dish.strip()}....... {price}грн')
print(f'\nВсього...... {bill}грн')