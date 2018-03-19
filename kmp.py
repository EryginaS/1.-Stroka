Baza="abcdefabcefabcdeabcdeffcbdse" #Базовая строка
stroka=raw_input("Enter the combination: ")#Строка пользователя
#проверка на длину строки пользователя 
if len(stroka)>len(Baza):
    print("Your string is longer than the base!")
else:
    New="@"+stroka+'@'+Baza #Новая строка для префикс-функции 
    i=2 # индекс списка новой функции
    k=0 # второй индекс для префик-функции
    p=[] #список для префикс-функции
    p.append(0)
    p.append(0)
    #префикс функция 
    while i<len(New):
        if k==0:
            if New[i]==New[k+1]:
                p.append(k+1)
                k=k+1

                
                i=i+1
            else:
                p.append(0)
                i=i+1
        else:
            if New[i]==New[k+1]:
                p.append(k+1)
                k=k+1
                i=i+1
            else:
                k=p[k]
                if New[i]==New[k+1]:
                    p.append(k+1)
                    k=k+1
                    i=i+1
                else:
                    p.append(k)
                    i=i+1
#Вывод на экран
                    
s=len(stroka)
if (s in p):
    print ("match found! ")
else:
    print("match not found!")
