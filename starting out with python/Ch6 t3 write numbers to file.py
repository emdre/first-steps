def main():
    infile = open('number_list.txt', 'w')
    for num in range(1, 101):
        infile.write(str(num) + '\n')
    infile.close()


main()    
