import random
import os
import sys
import time
from time import sleep

def slowPrint(text, slptime):
	for i in text:
		sys.stdout.write(i)
		sys.stdout.flush()
		sleep(slptime)

def clear():
	os.system('clear')

slowPrint("Hello! Welcome to THE VAULT!", 0.075)
time.sleep(1)
clear()
print("Locating file server...")
time.sleep(2.5)
if os.path.exists("universal_savedGames.py") and ("savedGames.py"):
  print("\n Found local file(s)...")

else:
  print("\n File not found...") # There will always be a file btw
  time.sleep(2.5)
  clear()
  n = input(str("What is your name?\n"))
  m = random.randint(30, 30)
  print("Welcome " + n + ", this is your current bank balance!")
  print("you have $" + str(m))
 
  f = open(n + ".py","w+")
  f.write("name = '"+ n + "'")
  f.write("\nmoney = " + str(m))
  f.close()

  time.sleep(1)
  auto = 0

  while True:
    ch = input(str("Type 'get' to get money\nType 'save' to override your last save\n")).lower()
   
    if (ch == "get"):
      ma = random.randint(5, 50)
      print("you got $"+str(ma))
      m = m + ma
      print("you now have $"+str(m))
      time.sleep(.3)
      auto = auto + 1
    
    if (ch == "save"):
      f = open(n + ".py","w+")
      f.write("name = '"+ n + "'")
      f.write("\nmoney = " + str(m))
      f.close()
    
      os.system('clear')
      time.sleep(1)
    
      print("Progress Saved")
    
      time.sleep(.3)
      auto = 0
      continue
    
    if (auto == 5):
      f = open(n + ".py","w+")
      f.write("name = '"+ n + "'")
      f.write("\nmoney = " + str(m))
      f.close()
      auto = 0
      print("Game autosaved to " + n + ".py!")
      continue

time.sleep(10)
clear()

passprotect = input("Enter the password: ")

if passprotect == "passprotect.main.vault":
  if os.path.exists("universal_savedGames.py"):
    print("\n Found local file...")
    time.sleep(2.5)
    clear()
    import universal_savedGames
    n = universal_savedGames.name
    m = universal_savedGames.money
    time.sleep(1)
    print("Name is " +n+ '\n+ loadStr = lsCD_ID-18')
    time.sleep(.3)
    print("You have $"+str(m))
        
    time.sleep(1)
    auto = 0

    while True:
      ch = input(str("Type 'get' to get money\nType 'save' to override your last save\n")).lower()
    
      if (ch == "get"):
        ma = random.randint(10, 1010)
        print("you got $"+str(ma))
        m = m + ma
        print("you now have $"+str(m))
        time.sleep(.3)
        auto = auto + 1
      
      if (ch == "save"):
        f = open("universal_savedGames" + ".py","w+")
        f.write("name = '"+ n + "'")
        f.write("\nmoney = " + str(m))
        f.close()
        os.system('clear')
        time.sleep(1)
        print("Progress Saved")
        time.sleep(.3)
        auto = 0
        continue
    
      if (auto == 5):
        f = open("universal_savedGames" + ".py","w+")
        f.write("name = '"+ n + "'")
        f.write("\nmoney = " + str(m))
        f.close()
        auto = 0
        print("Game autosaved to universal_savedGames.py!")
        continue

    if passprotect != "passprotect.main.vault":
      if os.path.exists("universal_savedGames.py"):
        print("\n Found local file...")
        time.sleep(2.5)
        clear()
        import universal_savedGames
        n = universal_savedGames.name
        m = universal_savedGames.money
        time.sleep(1)
        print("Name is " +n+ '\n+ loadStr = lsCD_ID-04')
        time.sleep(.3)
        print("You have $"+str(m))


elif passprotect != "passprotect.main.vault":
  if os.path.exists("savedGames.py"):
    print("\n Found local file...")
    time.sleep(2.5)
    clear()
    import savedGames
    n = savedGames.name
    m = savedGames.money
    time.sleep(1)
    print("Name is " +n+ '\n+ loadStr = lsCD_ID-04')
    time.sleep(.3)
    print("You have $"+str(m))
        
    time.sleep(1)
    auto = 0

    while True:
      ch = input(str("Type 'get' to get money\nType 'save' to override your last save\n")).lower()
    
      if (ch == "get"):
        ma = random.randint(5, 50)
        print("you got $"+str(ma))
        m = m + ma
        print("you now have $"+str(m))
        time.sleep(.3)
        auto = auto + 1
      
      if (ch == "save"):
        f = open("savedGames" + ".py","w+")
        f.write("name = '"+ n + "'")
        f.write("\nmoney = " + str(m))
        f.close()
        os.system('clear')
        time.sleep(1)
        print("Progress Saved")
        time.sleep(.3)
        auto = 0
        continue
    
      if (auto == 5):
        f = open("savedGames" + ".py","w+")
        f.write("name = '"+ n + "'")
        f.write("\nmoney = " + str(m))
        f.close()
        auto = 0
        print("Game autosaved to savedGames.py!")
        continue

    if passprotect != "passprotect.main.vault":
      if os.path.exists("savedGames.py"):
        print("\n Found local file...")
        time.sleep(2.5)
        clear()
        import savedGames
        n = savedGames.name
        m = savedGames.money
        time.sleep(1)
        print("Name is " +n+ '\n+ loadStr = lsCD_ID-04')
        time.sleep(.3)
        print("You have $"+str(m))

  
