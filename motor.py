import RPi.GPIO as GPIO
import curses

GPIO.setwarnings(False)

screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.OUT) # Motor 1 
GPIO.setup(14,GPIO.OUT) # Motor 1 

GPIO.setup(17,GPIO.OUT) #Motor 2
GPIO.setup(18,GPIO.OUT) # Motor 2 

while True:
  a=screen.getch()
  if a== ord('q'):
    break
  elif a== curses.KEY_UP:
    GPIO.output(4,True) 
    GPIO.output(14,False) 
    GPIO.output(17,True) 
    GPIO.output(18,False) 
    print("W")
  elif a == curses.KEY_DOWN:
    GPIO.output(4,False) 
    GPIO.output(14,True) 
    GPIO.output(17,False) 
    GPIO.output(18,True) 
    print("S")
  elif a == curses.KEY_RIGHT:
    GPIO.output(4,True) 
    GPIO.output(14,False) 
    GPIO.output(17,False) 
    GPIO.output(18,True) 
    print("D")
  elif a == curses.KEY_LEFT:
    GPIO.output(4,False) 
    GPIO.output(14,True) 
    GPIO.output(17,True) 
    GPIO.output(18,False) 
    print("A")
  elif a == 0:
    GPIO.output(4,False) 
    GPIO.output(14,False) 
    GPIO.output(17,False) 
    GPIO.output(18,False) 
    print("STOP")
