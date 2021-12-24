import os as o
import random

def osClear():
	rOS = p.system()
	if rOS in ("Windows", "NT"):
		o.system("cls")
	else:
		o.system("clear")

def main():
  while True:
    osClear()

    asciiArt = ['sus.py', 'trol.py', 'gobl.py', 'hak.py', 'babyRick.py', 'ZAMN.py', 'cry.py', 'hi.py', 'bing.py', 'cred.py', 'gloc.py', 'heli.py', 'mo.py', 'roc.py', 'wall.py', '?.py', 'noo.py', 'trolSmile.py', 'fsociety.py']

    o.system("python3 ./asciis/" + random.choice(asciiArt))

    typeOption = int(input('[$]>>: '))

    if typeOption == 1:
      o.system('python3 home.py')
    elif typeOption == 2:
      o.system('python3 business.py')
    elif typeOption == 3:
      print('TERMINATED!..')
      exit()

if __name__ == "__main__":
  main()
