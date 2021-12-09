print("Kuru no uzdevumiem vēlies realizēt")
print("Izvēlies ciparu")
print("1- pirmo uzdevumu")
print("2 - otro uzdevumu")
print("3 - trešo uzdevumu")
print("__________________")
print("Tu esi izvēlējies uzdevumu nr.")
b=[]


def uzdevums1():
  print('Uzdevums1')
  kods=1
  for i in range (4):
    c=int(input('Ieavdi skaitli'))
    b.append(c)
    print(kods)
    kods=kods+1
    if kods==3:
     b1=c
     print(b1)
    if kods==5:
     b2=c
     print(b2)
  print(b)
  print('2. un 4. skaitla reizināums ir',b1*b2)
    



def uzdevums2():
  print('Uzdevums2')



def uzdevums3():
  print('Uzdevums3')







a=int(input('ieavadi uzdevuma numuru'))
if a==1:
  uzdevums1()
elif a==2:
  uzdevums2()
elif a==3:
  uzdevums3()