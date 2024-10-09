def print_save(string, file):
    print(string)
    if file:
        file = open(file, 'a+')
        file.write(string+'\n')
        file.close()