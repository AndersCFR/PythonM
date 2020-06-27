from googletrans import Translator
translator = Translator()


try: 
    with open('PythonMaster/File_IO/his.txt',mode='r') as myfile:
        print(myfile.read())
        text = myfile.read()
        print(text.__str__())
        print(translator.translate('hola amigo'))
except FileNotFoundError:
    print('check your path')
