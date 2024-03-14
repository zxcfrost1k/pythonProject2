# Python

# 1
# Сначала я вручную перенёс данные из файла cars.csv в cars.txt

mass = [i.split() for i in open('cars.txt', encoding='utf-8')]

new_mass_for_red_car = []

for x in mass:
    if x[-1] == 'красный':
        new_mass_for_red_car.append(f'У {x[2]} {x[3]} есть машина красного цвета. Её стоимость {x[0]}.')

print('\n'.join(new_mass_for_red_car))

# Дальше опять вручную внёс данные в файл red_car.txt


new_mass_for_volvo_red_car = []

for x in mass:
    if x[-1] == 'красный' and x[2] == 'volvo':
        new_mass_for_volvo_red_car.append(f'{x[3]} есть машина красного цвета. Её стоимость {x[0]}')

print('\nvolvo\n' + '\n'.join(new_mass_for_volvo_red_car))

# И перенёс данных в файл red_volvo.txt


# 2
mass = [[g.strip() for g in i.split('	')] for i in open('cars.txt', encoding='utf-8')]


def search():
    new_mass = []
    manufacturer, color = map(str, input().split())

    if manufacturer == 'car' and color == 'none':
        return False

    for x in mass:
        if x[2] == manufacturer and x[-1] == color:
            new_mass.append(f'{x[2]} {x[-1]} цена {x[0]}, пробег данной машины составляет {x[4]}')

    if new_mass:
        print('По вашему запросу:\n' + '\n'.join(new_mass))
    else:
        print('По данным параметрам ничего не найдено')

    return True


while search() is True:
    search()


# 4
mass = [[g.strip() for g in i.split('	')] for i in open('cars.txt', encoding='utf-8')]
mass.pop(0)

for i in range(1, len(mass)):
    if float(mass[i][-2]) > 70000:
        mass[i][0] = str(round(int(mass[i][0]) - int(mass[i][0]) * 0.12))

print('\n'.join(['  '.join(x) for x in mass[:10]]))
