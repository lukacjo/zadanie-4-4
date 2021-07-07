import logging
import sys

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

def calculator(dodawanie, odejmowanie, mnozenie, dzielenie, liczba1, liczba2):
    print(f"hello  {dodawanie} i {odejmowanie} ")
if __name__ == "__main__":
    dodawanie =sys.argv[1]
    odejmowanie =sys.argv[2]
"""
print("Witaj, ten program pomoże Ci sprawdzić czy jesteś pełnoletni/a")
adult = None
sex = input("Podaj proszę swoją płeć [M/K]: ")
if sex == 'M':
    age = int(input("Twój wiek? "))
    adult = age >= 18
elif sex == 'K':
    print("Kobiet o wiek się nie pyta, więc zrobię to delikatnie.")
    over18_yesno = input("Czy miałaś już osiemnastkę? [T/N]?")
    adult = (over18_yesno == 'T')
else:
    print("Nie ma takiej płci!")
    exit(1)
print("Już wiem. Twoja pełnoletniość w boolean to %s" % str(adult))