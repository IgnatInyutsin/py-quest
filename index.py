#модули
import time
import random

#импорт данных о доступных предметах
from items import allEquipment

#инвентарь
inventory = []
#вступительный диалог
print ("Добро пожалавать в мою мини-игру")
time.sleep (1)
print ("Желаю удачи")
time.sleep (1)
print ("\nТы у входа в подземелье. Тебе страшно идти в это опасное место без каких-либо вещей.")
time.sleep (2)
print ("К счастью мимо проходил торговец который сказал:")
time.sleep (1)
print ('"Я смотрю ещё один искатель приключений пришёл покорить подземелье')
time.sleep (0.5)
print ("Но ты совсем без вещей. Думаю я могу поделится с тобой некоторыми товарами, но конечно же в кредит)")
time.sleep (0.5)
print ("10 товаров будут пронумерованы от 1 до 11")
time.sleep (0.5)
print ('А ты не видя предметы назовёшь цифру от 1 до 11.')
time.sleep (0.5)

#выбор первого снаряжения
print ("Выбирай")
#илюзия выбора
number=int(input ())
if number <= 11 and number > 0:
        number = random.randint(1, 11)

if number == (1):
        inventory.append(allEquipment['magic'][0])
        print ("Ты получил Волшебную палjчку ПР 5 МАГ.АТК 70")
elif number == (2):
        inventory.append(allEquipment['fisycAttack'][0])
        print ("Ты получил Меч ПР 20 АТК 25")
elif number == (3):
        inventory.append(allEquipment['magic'][2])
        print("Ты получил Кулон ПР 20 ЗЩ 22 МАГ.АТК +20")
elif number == (4):
        inventory.append(allEquipment['defend'][0])
        print("Ты получил Шлем ПР 25 ЗЩ 32")
elif number == (5):
        inventory.append(allEquipment['defend'][1])
        print("Ты получил Перчатки ПР 20 ЗЩ 22 АТК +20")
elif number == (6):
        inventory.append(allEquipment['fisycAttack'][1])
        print("Ты получил Кинжал ПР 15 АТК 20")
elif number == (7):
        inventory.append(allEquipment['fisycAttack'][2])
        print("Ты получил Топор ПР 5 АТК 70")
elif number == (8):
        inventory.append(allEquipment['magic'][1])
        print("Ты получил заклинание Огненый шар ПР 20 МАГ.АТК 25")
elif number == (9):
        inventory.append(allEquipment['defend'][2])
        print("Ты получил Кольчугу ПР 30 ЗЩ 40")
elif number == (10):
        inventory.append(allEquipment['item'][0])
        print("Ты получил Тотем Бессмертия ПР 1 ЗД + Макс.Востоновление")
elif number == (11):
        inventory.append(allEquipment['item'][1])
        print("Ты получил Лекарственные травы ПР 10 ЗД + 25")
else:
        print("Ну ладно тогда не бери")
time.sleep(1)

#второй предмет
print("Выбирай второй предмет")
#буллевая переменная, позволяющая выйти из цикла
i = True
#цикл, на случай если предметы одинаковые
while i:
        number=int(input ())
        if number <= 11 and number > 0:
                number = random.randint(1, 11)

        if number == (1):
                inventory.append(allEquipment['magic'][0])
                print ("Ты получил Волшебную палачку ПР 5 МАГ.АТК 70")
        elif number == (2):
                inventory.append(allEquipment['fisycAttack'][0])
                print ("Ты получил Меч ПР 20 АТК 25")
        elif number == (3):
                inventory.append(allEquipment['magic'][2])
                print("Ты получил Кулон ПР 20 ЗЩ 22 МАГ.АТК +20")
        elif number == (4):
                inventory.append(allEquipment['defend'][0])
                print("Ты получил Шлем ПР 25 ЗЩ 32")
        elif number == (5):
                inventory.append(allEquipment['defend'][1])
                print("Ты получил Пречатки ПР 20 ЗЩ 22 АТК +20")
        elif number == (6):
                inventory.append(allEquipment['fisycAttack'][1])
                print("Ты получил Кинжал ПР 15 АТК 20")
        elif number == (7):
                inventory.append(allEquipment['fisycAttack'][2])
                print("Ты получил Топор ПР 5 АТК 70")
        elif number == (8):
                inventory.append(allEquipment['magic'][1])
                print("Ты получил заклинание Огненый шар ПР 20 МАГ.АТК 25")
        elif number == (9):
                inventory.append(allEquipment['defend'][2])
                print("Ты получил Кольчугу ПР 30 ЗЩ 40")
        elif number == (10):
                inventory.append(allEquipment['item'][0])
                print("Ты получил Тотем Бессмертия ПР 1 ЗД + Макс.Востоновление")
        elif number == (11):
                inventory.append(allEquipment['item'][1])
                print("Ты получил Лекарственные травы ПР 10 ЗД + 25")
        else:
                print("Ну ладно тогда не бери")
        
        if inventory[0] == inventory[1]:
                del inventory[1]
                print("Тебе попался тот же предмет, поэтому давай еще раз сыграем.")
        else:
                i = False
time.sleep(1)

#дальнейший вход в подземелье и выбор экипировки
print('\nТорговец: "Жду возвращения кредита, но помни - чем дольше не будешь возвращать его, тем больше процентов я начислю".')
time.sleep(3)
print('\nПосле данных слов тороговец ушел и вы решили начать свое приключение в подземелье.')
print('Спускаясь вниз воздух становиться все более сырой и вы чувствуете запах крови, а еще ниже слышится вой волков. Что вы сделаете?')
i = False
while i == False:
        print('\n1 - Экипируете снаряжение')
        print('2 - Спуститесь вниз')
        answer = int(input())

        if answer == 1:
                print('Вы можете экипировать по одной магической вещи, одному холодному оружию и одному элементу защитного снаряжения.')
                time.sleep(0.5)
                print('Ваша статистика будет равна сумме статистик вашего снаряжения')
                time.sleep(0.5)
                print("\n Какое снаряжение вы желаете экипировать?")
                print("0 - выйти из режима экипировки\n")

                a = 1
                #массив по всем элемен1там инвентаря
                i = 0
                while i < len(inventory):
                        if "type" in inventory[i] == False:
                                continue

                        #строка вывода элемента инвентаря
                        str = str(a) + " - " + inventory[i]["name"] + " Тип:" + inventory[i]["type"] + " "
                        print(inventory)
                        print(str)
                        i+=1