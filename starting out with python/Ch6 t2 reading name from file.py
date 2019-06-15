def main():
    name_file = open('my_name.txt', 'r')
    file_contents = name_file.read()
    name_file.close()
    print(file_contents.rstrip('\n'))
main()    
