#prints year the user will turn 100
navn = input("Ditt navn: ")
alder = int(input("Din alder: "))
yearofdeath = 2020 + 100-alder
gjentanummer = int(input("Hvor mange ganger vil du ha svaret ditt?"))

for i in range(gjentanummer):
    print (str(i) + " Du, " + navn + " vil dø i året: " + str(yearofdeath))
