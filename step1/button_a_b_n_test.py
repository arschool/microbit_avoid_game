# TESTING BUTTON A AND B
from microbit import *

a = Image("09990:"
          "90009:"
          "99999:"
          "90009:"
          "90009")
b = Image("99990:"
          "90009:"
          "99990:"
          "90009:"
          "99990")
n = Image("90009:"
          "99009:"
          "90909:"
          "90099:"
          "90009")
while True:
    if button_a.is_pressed():
        display.show(a)
    elif button_b.is_pressed():
        display.show(b)
    else:
        display.show(n)
