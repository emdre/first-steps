"""
Utwórz nowy plik np. jednostki.py, który po podaniu przez użytkownika długości w cm będzie wyświetlał wynik w metrach i calach zaokrąglając do 4 miejsc po przecinku.
"""

print("Podaj wartość w cm: ")
cm = int(input())
m = cm/100
cal = cm * 0.3937
print("{} cm to {:.4f} m".format(cm, m))
print("{} cm to {:.4f} in".format(cm, cal))
