"""Do zmiennej sentence przypisz zdanie: „Kurs Pythona jest prosty i przyjemny.”, a następnie:

Policz wszystkie znaki w napisie
Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
Wyświetl znak o indeksie (czy za każdym razem rozumiesz co się dzieje?):
7
12
-4
37
Wprowadź do zdania 2 błędy ortograficzne. """

sentence = "Kurs Pythona jest prosty i przyjemny."
print(len(sentence))
print(sentence[18:24])
print(sentence[7]) # prints t
print(sentence[12]) # prints a space 
print(sentence[-4]) # prints m
print(sentence[37]) # out of range
sentence = sentence[0] + "ó" + sentence[2:22] + "s" + sentence[23:]
print(sentence)

                                                        
