#В отдельный файл импортируйте и создайте объект Cat, который выводит имеющихся
# на сайте котов, с одинаковыми параметрами, но с разными значениями.

class Cat:     #Probnuy.py
    def __init__(self, name="", age=0, gender="", code=""):
        self.name = name
        self.age = age
        self.gender = gender
        self.code = code


from Probnuy import Cat    #Cat.py

n = Cat("Сем",2 , "девочка","f")
n1 = Cat("Барон",2,"Мальчик","m")
n3 = Cat("Барсик", 4, "Девочка","F")
n_dikt = n.__dict__, n1.__dict__, n3.__dict__

import json
#############_____Словари переводим в Json
njison = json.dumps(n_dikt)
print(njison)
print(json.loads(njison))