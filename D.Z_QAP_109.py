# Домашнее задание 18.8.19 Студент: Александр.QAP-109.

kolichesto_biletov = int(input('Сколько билетов вы хотите приобрести?\nВведите количество :'))
vozrast = [int(input('Укажите возраст участников:')) for i in range(kolichesto_biletov)]
vozrast_do_18 = 0
vozrast_do_25 = 990
vozrast_ot_25 = 1390
summa = 0

for i in range(0, kolichesto_biletov >= 3):
    i = kolichesto_biletov
    for i in vozrast:
        if 18 <= i < 25:
            i = vozrast_do_25 - (990 * 10 / 100)
            summa = summa + i
        elif 25 <= i < 100:
            i = vozrast_ot_25 - (1390 * 10 / 100)
            summa = summa + i
        elif 1 <= i < 18:
            i = vozrast_do_18
            summa = summa + i
            print()
    print('У вас бонус - 10 % . Ваша сумма к оплате', int(summa),"руб")
for i in range(0, kolichesto_biletov < 3 and not 0):
    i = kolichesto_biletov
    for i in vozrast:
        if 18 <= i < 25:
            i = vozrast_do_25
            summa = summa + i
        elif 25 <= i < 100:
            i = vozrast_ot_25
            summa = summa + i
        elif 1 <= i < 18:
            i = vozrast_do_18
            summa = summa + i
            print()
    print('К сожалению у вас нет бонуса -10 % . Ваша сумма к оплате', int(summa),"руб")

