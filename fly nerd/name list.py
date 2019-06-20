"""Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście."""

names = str(input("Podaj imiona oddzielone spacją: "))            
for name in names.split():
            print("Cześć,", name)
            
