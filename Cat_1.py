##############################______21.9.1_________
class Rectangle:
    def __init__(self, x="", y="", width="", height="" ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


n = Rectangle(5,10,50,100)

print(f'Rectangle:{n.x},{n.y},{n.width},{n.height}')

##############################______21.9.3_________#########
class Klients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс:{self.balance} руб."'

    def Korporative_Cat(self):
        return [f'{self.name}, {self.surname}, {self.city}']


Klient = Klients('Иван','Петров','Москва', 50)
Klient2 = Klients('Валерий', 'Мазаев','Симферополь', 1234)
print(Klient)
print(Klient.Korporative_Cat(), Klient2.Korporative_Cat())


