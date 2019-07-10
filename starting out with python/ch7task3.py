def main():
    rainfall = get_monthly_rainfall()
    total = calculate_total_rainfall(rainfall)
    average = total / 12
    highest = max(rainfall)
    lowest = min(rainfall)
    print('Całkowita wielkość opadów w roku wyniosła: ', total)
    print('Średnia wielkość opadów w miesiącu wynosiła: ', average)
    print('Najniża wielkość opadów w miesiącu to: ' + str(lowest) + ', a najwyższa to: ' + str(highest) + '.')


def get_monthly_rainfall():
    rainfall = []
    for item in range(12):
        monthly_rainfall = float(input('Podaj całkowitą wielkość opadu deszczu w miesiącu ' + str(item + 1) + ':'))
        rainfall.append(monthly_rainfall)
    return rainfall


def calculate_total_rainfall(value_list):
    total = 0.0
    for value in value_list:
        total += value
    return total


main()