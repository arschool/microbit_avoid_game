## STEP 2 敵キャラを登場させよう！

### STEP 2のゴール 敵キャラを登場させよう！


### ますはじめに イメージしてことばにみましょう！
1. 光の点はどんな動きをする？
1. １コマにどんなコードが必要？


  
  
  
  
  
  
  
  
  
  
  
### STEP 2で使う関数
#### 0〜5までの数字からランダムに取り出して、xに入れておく
```
import random
x = random.randint(0,5)
```

#### 変数を宣言する
```
a = [入れたいものを指定する]
```

#### 変数の中身に1をたす
```
a = a + 1
```

### STEP 2.1 上から下に光の点が流れるコードを書こう！
```
from microbit import *
import random

# このコードの変数をどうしたら動くように見えるかな？
x = 2
y = 0

while True:
    display.set_pixel(x,y,5)
    sleep(500)
    display.set_pixel(x,y,0)
    sleep(500)

```

### STEP 2.2 下まで行ったら一番上に戻すコードを書こう！
```
from microbit import *
import random

# このコードのどこにif文を入れたら上に戻るだろう？
x = 2
y = 0

while True:
    display.set_pixel(x,y,5)
    sleep(500)
    display.set_pixel(x,y,0)
    sleep(500)

```

### STEP 2.3 場所をランダムに決めて出そう！
```
from microbit import *
import random

# このコードのどこにif文を入れたら場所がランダムに出てくるかな？
x = 2
y = 0

while True:
    display.set_pixel(x,y,5)
    sleep(500)
    display.set_pixel(x,y,0)
    sleep(500)

```
