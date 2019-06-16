def main():
    file = input('Enter a .txt file name: ')
    file = open(file, 'r')
    line = file.readline()
    count = 0
    while line != '':
        count += 1
        print(str(count) + ': ' + line)
        line = file.readline()
    file.close()
main()
        
