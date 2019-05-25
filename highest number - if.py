"""Trzy dowolne liczby zapisz do trzech zmiennych.
Znajdź największą liczbę.
Wyświetl liczby od największej do najmniejszej."""

x = 3
y = 6
z = 10
if x > y and x > z:
    maximum = z
elif y > x and y > z:
    maximum = y
else:
    maximum = z

print(maximum)


if x > y and x > z:
    if y > z:
        print(x, y, z)
    else:
        print(x, z, y)
elif y > z and y > x:
    if z > x:
        print(y, z, x)
    else:
        print(y, x, z)
else:
    if z > y and z > x:
        if y > x:
            print(z, y, x)
    else: print(z, x, y)    
                
