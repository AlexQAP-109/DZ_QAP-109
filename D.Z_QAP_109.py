#######################################################################################################
#Напишите программу, которая получает от пользователя имя файла, открывает этот файл
# в текущем каталоге, читает его и выводит два слова: наиболее часто встречающееся из тех,
# что имеют размер более трех символов, и наиболее длинное слово .
####################################################################################

n = input('Название файла: ')
with open(n, encoding='utf8') as f:
    n = f.read()


def ochistka_texta(ns1):
    for i in '!"\'#$%&()*+-,/.:;<=>?@[\\]^_{|}~':
        ns = n.replace(i, '')
    return n.split()

ns1 = ochistka_texta(n)

################ Ограничиваем список значениями из 3 букв
def ogranuchenie_3_buk(ns1):
    ns = []
    for i in ns1:
        if len(i) > 3 :
            ns.append(i)
    return ns

ns = ogranuchenie_3_buk(ns1)

dlinnoe_slovo = max(ns, key=len)
print(f'Самое длинное слово:   "{dlinnoe_slovo}"')
#Переводим список в словарь
def slovar(nss):
    slovar1 = {}
    for i in ns:
        if i in slovar1:
            slovar1[i] += 1
        else:
            slovar1[i] = 1
    return slovar1

nss = slovar(ns)

#Функция которая переберет словарь и выдаст частые повторяющиеся слова по цифре
def chastue_slova(slovo):
    for i  in nss.values():
        if i == max(nss.values()):
            slovo = i

    return slovo
slovo = chastue_slova(nss)


#Функция на определение соответствующего ключа
def opredelenie(nss,slovo):
    for i, d in nss.items():
        if (d == slovo):
            return i

urra = opredelenie(nss,slovo)
print(f'Самое часто встречающееся слово ---"{urra}" --- втречается --- "{slovo}"  раза')

