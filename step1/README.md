## STEP 1 プレイヤーのドットを表示させよう！

### STEP 1のゴール　AボタンとBボタンを使って、左右にプレイヤーを動かせるようにする。

### STEP 1で使う関数
#### 1秒待つ
```
sleep(1000) #1000ミリ秒単位
```

#### 5 x 5の画面を使って絵を作る [イメージ](http://microbit-micropython.readthedocs.io/ja/latest/tutorials/images.html)
```
# micro:bitにあるものを描く場合
display.show(Image.HEART)

# 自分で描く場合
a = Image("09990:"
          "90009:"
          "99999:"
          "90009:"
          "90009")
display.show(a)

# 特定のピクセルを光らせる
display.set_pixel([x座標],[y座標],[明るさ])
```

#### ボタンの入力 [ボタン](http://microbit-micropython.readthedocs.io/ja/latest/tutorials/buttons.html)
```
# Aボタンを押したらスマイルが表示され、Bボタンを押すと画面から何もなくなる
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()
```


### Pythonのコード

#### micro:bitが起動している限り繰り返す
```
while True:
    [ここにコードを書く]
```

#### if文の書き方
```
if [一つ目の条件]:
    [一つ目の条件にあったときにする処理]
elif [二つ目の条件]:
    [二つ目の条件にあったときにする処理]
else:
    [一つ目の条件にも二つ目の条件にもあわないときにする処理]
```


### STEP 1.1 ボタンを押して色々な絵を表示させよう！
```
# TESTING BUTTON A AND B
from microbit import *

# ここの絵を変えてみよう！
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
```

### STEP 1.2 点の一つ一つを指定して表示させよう！
```
# DISPLAY CROSS ON LED
from microbit import *

while True:
    display.set_pixel(2,0,9)
    display.set_pixel(2,1,9)
    display.set_pixel(2,2,9)
    display.set_pixel(2,3,9)
    display.set_pixel(2,4,9)
    display.set_pixel(0,2,9)
    display.set_pixel(1,2,9)
    display.set_pixel(3,2,9)
    display.set_pixel(4,2,9)
```

### STEP 1.3 プレイヤーを動かそう！
```
# CHANGING POSITION OF PLAYER
from microbit import *

x = 2

while True:
    display.set_pixel(x,3,0)
    sleep(500)
    # ボタンを動かした後の一コマ
    if button_a.get_presses():
        # ここに動かすためのコードを書こう！
    elif button_b.get_presses():
        # ここに動かすためのコードを書こう！
    display.set_pixel(x,3,9)
    sleep(500)
```
