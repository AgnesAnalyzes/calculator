# Taschenrechner

print("Hallo, mein Name ist Polly und ich bin ein Taschenrechner.")
print("Ich kann +, −, ×, /, //, % und ** berechnen. Let's Go!")

def ist_float(zahl):
    try:
        float(zahl)
        return True
    except ValueError:
        return False


while True:
    
    zahl1 = input("Tippe deine erste Zahl hier ein:")
    if ist_float(zahl1):
        zahl1 = float(zahl1)
    else:
        print("Deine Eingabe ist übgültig. Sie muss eine Ganze - oder Kommazahl sein. Beginne von vorne.")
        continue
    
    operator = str(input("Wähle zwischen den folgenden Operatoren: +, −, *, /, //, % und **:"))

    zahl2 = input("Tippe deine zweite Zahl hier ein:")
    if ist_float(zahl2):
        zahl2 = float(zahl2)
    else:
        print("Deine Eingabe ist übgültig. Sie muss eine Ganze - oder Kommazahl sein. Beginne von vorne.")
        continue

    if operator == "+":
        result_add = zahl1 + zahl2
        print("Ausgabe:", result_add)
    elif operator == "-":
        result_sub = zahl1 - zahl2
        print("Ausgabe:", result_sub)
    elif operator == "*":
        result_mult = zahl1 * zahl2
        print("Ausgabe:", result_mult)
    elif operator == "/":
        if zahl2 == 0:
            print("Du kannst nicht durch 0 dividieren. Wiederhole deine Eingabe.")
            continue
        else:
            result_div1 = zahl1 / zahl2
            print("Ausgabe:", result_div1)
    elif operator == "//":
        result_div2 = zahl1 // zahl2
        print("Ausgabe:", result_div2)
    elif operator == "%":
        result_modu = zahl1 % zahl2
        print("Ausgabe:", result_modu)
    elif operator == "**":
        result_sqr = zahl1 ** zahl2
        print("Ausgabe:", result_sqr)
    else:
        print("Sorry, deine Eingabe zum Operator ist nichtt eindeutig. Bitte versuche es nochmal!")

    exit = str(input("Möchtest du noch was ausrechnen? j / n"))
    if exit == "n":
            break
    elif exit == "j":
            continue
