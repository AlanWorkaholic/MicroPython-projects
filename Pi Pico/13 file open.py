#import os.path
i = -1
while True:
    i += 1
    name = 'log' + str(i)
    try:
        file = open(name)
        file.close()
    except OSError:
    #    print('файла не существует')
        break
file = open(name, 'w')