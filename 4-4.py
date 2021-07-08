import logging
import sys
logging.basicConfig(level=logging.DEBUG, format=' %(message)s', filename="logfile.log")

"""
def calculator(a,b,c):
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    elif c==4:
        print(a/b)



    input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

"""


action = input("Podaj dzialanie, poslugujac sie odpowiednia liczba: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie: ")
num1= input("Podaj skladnik 1.")
num2= input("Podaj skladnik 2.")

if num1.isdigit():
    if num2.isdigit():
        num1=int(num1)
        num2=int(num2)
        if action == '1':
            print(f"Dodaje {num1} i {num2}\n"\
            "wynik to ",num1+num2)
        elif action == '2':
            print(f"Odejmuje {num2} od {num1}\n"\
            "wynik to ",num1-num2)
        elif action == '3':
            print(f"Mnoze {num1} i {num2}\n"\
            "wynik to ",num1*num2)    
        elif action == '4':
            print(f"Dziele {num1} przez {num2}\n"\
            "wynik to ",num1/num2)
    else:
        print("Nalezy podac liczbe")
        exit(1)
else:
    print("Nalezy podac liczbe")
    exit(1)


#    print(num1, "+", num2, "=", num1+num2)
#    logging.debug("dodaje %s i " % sys.argv[0])
