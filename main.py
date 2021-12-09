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
a = int(input("Ievadi 1. skaitli, kurš ir intervālā no -10 līdz 10"))
b = int(input("Ievadi 2. skaitli, kurš ir intervālā no -10 līdz 10"))
c = int(input("Ievadi 3. skaitli, kurš ir intervālā no -10 līdz 10"))
d = int(input("Ievadi 4. skaitli, kurs ir intervālā no -10 līdz 10"))
e = int(input("Ievadi 5. skaitli, kurs ir intervālā no -10 līdz 10"))
print( a, b, c, d, e)
z=0
if a < b:
  print(" 2. ievadītais skaitlis ir lielāks ar 1. ievadīto skaitli")
  z=z+1

if b<c:
  print(" 3. ievadītais skaitlis ir lielāks ar 2. ievadīto skaitli")
  z=z+1  

if c < d:
  print(" 4. ievadītais skaitlis ir lielāks ar 3. ievadīto skaitli")  
  z=z+1

if d < e:
  print(" 5. ievadītais skaitlis ir lielāks ar 4. ievadīto skaitli") 
  z=z+1 
print("Pēc skaita sarakstā skaitļi, kuri lielāki par iepriekšpēdējo saraksta elementu ir:  ",z)


def uzdevums3():
  print('Uzdevums3')







a=int(input('ieavadi uzdevuma numuru'))
if a==1:
  uzdevums1()
elif a==2:
  uzdevums2()
elif a==3:
  uzdevums3()
