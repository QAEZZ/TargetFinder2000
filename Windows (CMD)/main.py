import os
import random
import time


def main():
  while True:
    os.system("cls")
    
    print("WARNING:")
    print("\n MOST ASCII ART IS BROKEN IN CMD/POWERSHELL")
    print("This warning will go away in 5 seconds")
    time.sleep(1)
    os.system("cls")
    print("WARNING:")
    print("\n MOST ASCII ART IS BROKEN IN CMD/POWERSHELL")
    print("This warning will go away in 4 seconds")
    time.sleep(1)
    os.system("cls")
    print("WARNING:")
    print("\n MOST ASCII ART IS BROKEN IN CMD/POWERSHELL")
    print("This warning will go away in 3 seconds")
    time.sleep(1)
    os.system("cls")
    print("WARNING:")
    print("\n MOST ASCII ART IS BROKEN IN CMD/POWERSHELL")
    print("This warning will go away in 2 seconds")
    time.sleep(1)
    os.system("cls")
    print("WARNING:")
    print("\n MOST ASCII ART IS BROKEN IN CMD/POWERSHELL")
    print("This warning will go away in 1 second")
    time.sleep(1)
    os.system("cls")
    
    asciiArt = ['sus.py', 'trol.py', 'gobl.py', 'hak.py', 'babyRick.py', 'ZAMN.py', 'cry.py', 'hi.py', 'bing.py', 'cred.py', 'gloc.py', 'heli.py', 'mo.py', 'roc.py', 'wall.py', '?.py', 'noo.py', 'trolSmile.py', 'fsociety.py']

    os.system("python ./asciis/" + random.choice(asciiArt))

    typeOption = int(input('[$]>>: '))

    if typeOption == 1:
      os.system('python home.py')
    elif typeOption == 2:
      os.system('python business.py')
    elif typeOption == 3:
      print('TERMINATED!..')
      exit()

if __name__ == "__main__":
  main()
