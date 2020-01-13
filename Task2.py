def sjekkparitet(tall):
    if (tall % 2) == 0:
        print("PARTALL!!!")
    else:
        print("...oddetall... :(")
#sjekkparitet( int( input("Skriv inn et tall")))

def sjekkdelbarpåfire(tall):
    if (tall % 4) == 0:
        print("DELBAR PÅ 4!!!")
    else:
        print("Ikke delbar på 4 :((")
#sjekkdelbarpåfire( int( input("Skriv inn et tall")))

def brukerdeling(dividend, divisor):
    if dividend % divisor == 0:
        print("Ingen desimaler her i huset!!! <3 <3 <3 ")
    else: print("... desimaler :(( ...")
brukerdeling( int (input("Velg en dividend: ")), int(input("Velg en divisor: ")))
