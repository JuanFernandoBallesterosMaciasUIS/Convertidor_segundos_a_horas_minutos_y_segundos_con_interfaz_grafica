#Programa No 4: Convertirdor de segundos a horas, minutos y segundos.
print("---------------------------------")
print("--CONVERTIDOR-SEGUNDO-A-GENERAL--")
print("---------------------------------")

#input 
n = input("Digite la cantidad de segundos: ")
n = int(n)

#proceso

h = n/3600

h1 = int(h)
m1 = (h-h1)*60

m2 = int(m1)
s1 = int((m1-m2)*60)

#output
if h1 == 1:
    print("De los ", n ," segundos, serian: ", h1, " hora con", m2, "minutos y ", s1, "segundos")
else:
    print("De los ", n ," segundos, serian: ", h1, " horas con", m2, "minutos y ", s1, "segundos")