import json

with open('json_example_QAP.json',encoding='utf8') as f:
    n = json.load(f)
print(type(n))
#####Проверяем строку на длинну json в соответствии с требованиями##########
for i in n:
    if len(i) ==16:
        i == True
    else:
        print(f'!!!!!!!!!!!!!!!!!!1Длинна каждого json не соотвтствует требованиям--{len(i)}-- вместо 16!!!!!!!!!!!!')
print(f'!!!!!!!!!!!!!!!!!!!!!Все в норме длина каждого json соответствует--{len(i)}-- требованиям!!!!!!!!!!!!!!!!!!!!!!!!')

############## Вызываем функцию с разными значениями n[]#################
def iteraciya_json(*args):
    for i in args:
        for i, d in i.items():
            # print(i,d)
            if i == 'timestamp' and type(d) == int:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'referer' and type(d) == str and (d[0:6] == 'https:' or d[0:4] == 'http'):
                print(f'у ключа"{i}" значение {type(d)} --есть "URL" https или http--- ответ ==== "True"')
            elif i == 'location' and type(d) == str and (d[0:6] == 'https:' or d[0:4] == 'http'):
                print(f'у ключа"{i}" значение {type(d)} --есть "URL" https или http--- ответ ==== "True"')
            elif i == 'remoteHost' and type(d) == str:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'partyId' and type(d) == str:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'sessionId' and type(d) == str:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'pageViewId' and type(d) == str:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'eventType' and type(d) == str and d == 'itemBuyEvent' or d == 'itemViewEvent':
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True" присутствует значение---{d}')
            elif i == 'item_id' and type(d) == str:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'item_price' and type(d) == int:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'item_url' and type(d) == str and (d[0:6] == 'https:' or d[0:4] == 'http'):
                print(f'у ключа"{i}" значение {type(d)} --есть "URL" https или http--- ответ ==== "True"')
            elif i == 'basket_price' and type(d) == str:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'detectedDuplicate' and type(d) == bool:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'detectedCorruption' and type(d) == bool:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'firstInSession' and type(d) == bool:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            elif i == 'userAgentName' and type(d) == str:
                print(f'у ключа"{i}" значение {type(d)}  ответ ==== "True"')
            else:
                print(f'В даной паре ключ  "{i}" значение "{type(d)} параметры не соответствуют требованиям ===== "False"')



        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

iteraciya_json(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],n[10],n[11],n[12],n[13],n[14],n[15],n[16],n[17],n[18],n[19])