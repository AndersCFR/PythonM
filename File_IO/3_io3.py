#reading from other folder. pathlib is very used for mac, unix and windows
try:
    with open('app/sad.txt',"r") as myfile:  
    #./ means from the current ../menas back folder
        print(myfile.read())
except FileNotFoundError as err:
    print('File doesnt exists')
    raise err
