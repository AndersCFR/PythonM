with open('test.txt', mode='r+') as my_file:   #we dont need close the file r+ nos permite escribir y leer, pero no salta, 
#append me permite agregar al final, si solo uso w puedo crear un nuevo archivo
    text = my_file.write('hey writing from vscode \n')
    print(my_file.readlines()) 

