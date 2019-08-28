import qrcode as qr
import tkinter as tk
import tkinter.filedialog as fd
#外部ライブラリPillowからImageTkモジュールを読み込む
from PIL import ImageTk

base = tk.Tk()
#ベースタイトルを設定
base.title('QRcode Generator')
#フレームの作成．他の部品をひとまとめにする
#bd(boderwidth)：フレームの幅を指定．
#QRコードにする文字列とボタンを置くためのフレーム
input_area = tk.Frame(base, relief = tk.RAISED, bd = 2)
#QRコードの画像を置くためのフレーム
image_area = tk.Frame(base, relief = tk.SUNKEN, bd = 2)
#入力された文字列を保存しておくためStringVarクラスのencode_textとしてインスタンス化
encode_text = tk.StringVar()
#encode_textを用いて，テキストボックスを作成するためのEntryクラスをインスタンス化
#テキストボックスを置く場所をinput_areaを指定．
#packメソッドで左詰で設置．
entry = tk.Entry(input_area, textvariable = encode_text).pack(side = tk.LEFT)

#アプリ上で作成されたQRコードを表示させるためのラベル設定．
#image_areaというフレームを置くことにする
qr_label = tk.Label(image_area)

#QRコード作成
def generate():
    #QRコードにする文字列をgetメソッドで取得．
    #make関数でQRコードの画像を作成し，qr_labelのqr_imgに入れている．
    qr_label.qr_img = qr.make(encode_text.get())
    #QRコード(qr_img)の高さと幅のサイズを取得．
    img_width, img_height = qr_label.qr_img.size

    #qrcodeパッケージで作成した画像をPillowのTkモジュールを使って
    #tkinterで表示できるデータに変換．
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)
    #qr_labelに対して，各項目を上書きすることで設定．
    #表示する画像の指定とともに表示する画像のサイズをラベルのサイズに指定．
    #デカ過ぎても小さ過ぎてもダメなので画像のサイズを元に調整する．
    qr_label.config(image = qr_label.tk_img, width = img_width, height = img_height)
    qr_label.pack()

#encodeボタンを定義．
#ボタンを押すとgenarate関数が実行される．
encode_button = tk.Button(input_area, text = 'QRcode!!', command = generate).pack(side = tk.LEFT)
#QRコードにしたい文字列の入力欄とボタンを置いたinput_areaフォームをpack関数で表示
#padx, padyでそれぞれのフレームの外側をどれくらいの幅だけ空けるかを指定
input_area.pack(pady = 5)
#QRコード画像を表示するラベルに載せたimage_areaフォームをpack関数で表示
image_area.pack(padx = 3, pady = 1)

#メニュー画面の作成
"""
save関数：保存したいファイル名を取得して，取得したファイル名で保存．
"""
def save():
    #保存ファイル名の取得・・・tkinter.filedialog(fd)
    #initialfileに指定した文字列は保存するファイル名を入力する欄に入れておくファイル名
    filename = fd.asksaveasfilename(title = '名前をつけて保存する．', initialfile = 'qrcode.png')
    #filenameがtrueかつqr_labelがqr_imgのとき
    #filenameがnullだとfalseが返ってくる
    #hasattr：attribute存在するかを確認．無ければfalse
    if filename and hasattr(qr_label, 'qr_img'):
        qr_label.qr_img.save(filename)

#exit関数
#exitを押すとbase画面を全てdestroy
def exit():
    base.destroy()

#menubarの設置
#メニューバーの作成
menubar = tk.Menu(base)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label = 'File', menu = filemenu)
#save, exit関数が呼び出せるように設定．
filemenu.add_command(label = 'Save', command = save)
filemenu.add_separator
filemenu.add_command(label = 'exit', command = exit)
base.config(menu = menubar)
base.mainloop()