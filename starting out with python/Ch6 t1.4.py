def main():
    file = open('number_list.txt', 'r')
    count = 0
    for line in file:
        count += 1
    file.close()
    print(count)
main()
