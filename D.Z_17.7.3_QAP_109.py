#Домашнее задание 17.7.3.Студент: Александр.QAP-109.
money = int(input('Какую сумму вы планируете положить на депозит? :'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent['ТКБ'] = int((money)/100*5.6)
per_cent['СКБ'] = int((money)/100*5.9)
per_cent['ВТБ'] = int((money)/100*4.28)
per_cent['СБЕР'] = int((money)/100*4.0)

deposit = list(per_cent.values())
print(deposit)
deposit = max(deposit)
print('Максимальная сумма которую вы можете зарабртать:', int(deposit))
