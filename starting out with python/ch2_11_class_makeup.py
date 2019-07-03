women = int(input("Enter the number of women in you class: "))
men = int(input("Enter the number of men in your class: "))
total = women + men
women_percentage = (women / total) * 100
men_percentage = (men / total) * 100
print("The percentage of women in your classes is {:.0f}% and the percantage of men is {:.0f}%".format(women_percentage, men_percentage))
