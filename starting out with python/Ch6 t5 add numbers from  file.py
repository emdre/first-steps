def main():
    outfile = open('number_list.txt', 'r')
    total = 0
    line = outfile.readline()
    while line != '':
        num = int(line)
        total += num
        line = outfile.readline()
    outfile.close()
    print(total)
main()
