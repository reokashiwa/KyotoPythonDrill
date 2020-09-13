from turtle import *
import random # 乱数を使うので random モジュールもインポート

# 実行を停止するための変数（フラッグ）
stop_flag = False

# マウスがクリックされたときの関数、引数x, yをとるようにしないといけないが、使わない実行停止フラグを True にする

def clicked(x,y):
    global stop_flag
    stop_flag = True

# マウスがクリックされたときの動作を指定、 clicked 関数を呼び出す
onscreenclick(clicked)

speed(0)
while(not stop_flag):
    # - 90 度から 90 度の範囲でランダムに向きを変える
    left(random.randint(-90,90))
    forward(10)
    # タートルの位置が原点から一定の距離を超えれば、戻る
    if (position()[0]**2+position()[1]**2 > 200**2):
        forward(-10)
