
a = 6                   #het eerste getal van de berekening
op = "+"                #De soort berekening (rekenkundige operator)
b = 10                  #het tweede getal van de berekening
     

                        #checken welke operator je hebt gekozen
if op == "+":           #Je kiest voor optellen
    result = a+b        #Bereken de uitkomst
elif op == "-":         #Je kiest voor aftrekken
    result = a-b        #Bereken de uitkomst
elif op == "/":         #Je kiest voor delen
    result = a/b        #Bereken de uitkomst
elif op == "*":         #Je kiest voor vermenigvuldigen
    result = a*b        #Bereken de uitkomst
elif op == "%":         #Je kiest voor restwaarde na deling (modulo)
    result = a%b        #Bereken de uitkomst
else:                   #Je hebt geen geldige berekening gekozen
    result = 0          

print(result)           #Print de uitkomst van je berekening