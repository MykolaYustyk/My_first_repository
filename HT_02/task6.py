"""
    6. Написати скрипт, який об'єднає три словника в самий перший. Оновлюється тільки перший словник. Дані можна "захардкодити".
        Sample Dictionary :
        dict_1 = {1:10, 2:20}
        dict_2 = {3:30, 4:40}
        dict_3 = {5:50, 6:60}
        Expected Result : dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}
print('dict_1 was\n', dict_1)
print('dict_2 was\n', dict_2)
print('dict_3 was \n', dict_3)
dict_1.update(dict_2)
dict_1.update(dict_3)
print('dict_1 is : \n', dict_1)