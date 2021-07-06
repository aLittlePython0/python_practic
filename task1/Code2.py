# Вводимо рядок
String = input("Input your string : ")
Numbers = []
Words = ''
length=len(String)
print('String : ' + String)
k=0
# Цикл записує числа в однин рядок а слова в інший
for i in range(length):
    j=String[i]
    if '0' <= j <= '9':
        Numbers.append(int(j))
        k+=1
        i+=1
    else:
        Words+=j
        i+=1
Words+=' '
print('Numbers : ' + str(Numbers))
print('String without numbers : ' + Words)
i=0
MaxNumber=0
# Знаходимо найбільше число
for i in range(len(Numbers)):
        if Numbers[i]>MaxNumber:
            MaxNumber=Numbers[i]
            i+=1
        else:
            i+=1

Numbers2=[]
i=0
# Всі числа не включаючи найбільше записуються в масив та підносяться до степеню свого індекса
for i in range(len(Numbers)):
         if Numbers[i]!=MaxNumber:
              Numbers2.append(Numbers[i]**i)
              i+=1
         else:
              continue
# Вивід Максимального значення та чисел після піднесення до степеня
print('Max number : ' + str(MaxNumber))
print('Numbers without max : ' + str(Numbers2))
# Ініціалізація рядка в яку будуть записуватися слова з першою і останньою буквою в верхньому регістрі
StringUpper=''
l=0
i=0
# Першу і останню букву слова замінюємо на великі
for i in range(len(Words)-1):
    j=Words[i+1]
    if j==' ':
        StringUpper+=Words[l].upper()
        StringUpper+=Words[l+1:i]
        StringUpper+=Words[i].upper()+' '
        l=i+2
        i+=1
    else:
        i+=1
print('String with upper : ' + StringUpper)
