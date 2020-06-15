from os import system, name, path

def run(code):

    string = code.split(' ')
    def notFound():
      print(f"Command not found: {string[0]}")
    def clear(): 
      if name == 'nt': 
        _ = system('cls') 
      else: 
        _ = system('clear') 
    def echo():
      prepend = "\n"
      if ("-n" in string):
        string.remove('-n')
        prepend = ""
      tempstring = string.copy()
      tempstring.pop(0)
      print(" ".join(tempstring), end = prepend)
    def cat():
      try :
        f = open(string[1], "r")
        print(f.read())
        f.close()
      except FileNotFoundError:
        print("No such file or directory")
      except IndexError:
        print("No file name")
    def pwd():
      print(path.dirname(path.realpath(__file__)))

    switchCommand = {
      'clear': clear,
      'echo': echo,
      'cat': cat,
      'pwd': pwd,
      'notFound': notFound
    }

    switchCommand.get(string[0], notFound)()

continueShell = True
while (continueShell):
  string = input(">> ")
  run(string)
