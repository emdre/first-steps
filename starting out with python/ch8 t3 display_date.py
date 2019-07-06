import calendar

def main():
    date = input("Enter a date formatted as dd/mm/rrrr: ")
    date_list = date.split('/')
    day = date_list[0]
    month = int(date_list[1])
    month_full_name = calendar.month_name[month]
    year = date_list[2]
    print(f'{day} {month_full_name} {year}')
main()