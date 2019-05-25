""""W poprzednich częściach pisaliśmy kalkulator BMI, teraz wzbogacimy go o interpretację wyniku. Program powinien sprawdzić czy BMI należy do jednego z 4 wyników: niedowaga/waga normalna/lekka nadwaga i nadwaga. Ponadto w przypadku nadwagi chcemy sprawdzić czy mamy doczynienia z otyłością.

Poniżej tabela z klasyfikacją wyników:

Niedowaga	< 18,5
Waga normalna	18,5 – 24
Lekka nadwaga	24 – 26,5
Nadwaga	> 26,5
Otyłość I stopnia	30 – 35
Otyłość II stopnia	30 – 40
Otyłość III stopnia	> 40 """



wzrost = float(input("Podaj swój wzrost w metrach: "))
waga = float(input("Podaj swoją wagę: "))
BMI = waga / (wzrost ** 2)
print("Twoje bmi wynosi: {:.2f}".format(BMI))
if BMI < 18.5:
    print("Masz niedowagę.")
elif BMI >= 18.5 and BMI < 24:
    print("Twoja waga jest w normie.")
elif BMI >= 24 and BMI < 26.5:
    print("Masz lekką nadwagę")
else:
    if BMI >= 30 and BMI < 35:
        print("Masz nadwagę. Otyłość I stopnia.")
    elif BMI >= 35 and BMI < 40:
        print("Masz nadwagę. Otyłość II stopnia.")
    elif BMI >= 40:
        print("Masz nadwagę. OTyłość III stopnia.")
    else:
        print("Masz nadwagę.")
