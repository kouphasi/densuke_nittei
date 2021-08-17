#kouphasi
import csv#標準ライブラリーの中にcsvファイルの編集用のモジュールが入っている
import os,sys
from tkinter import *
import tkinter.ttk as ttk
import tkinter.filedialog as tf
from tkinter import messagebox

filePath = ""
max_value1 = 0
max_key1 = ""
max_value2 = 0
max_key2 = ""
max_value3 = 0
max_key3 = ""
def filedialog_clicked():#ファイルダイアログの表示
    fTyp = [("", "*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = tf.askopenfilename(filetype = fTyp, initialdir = iFile)
    entry2.set(iFilePath)

def toNextpage():#点数入力画面への切り替え
    file_path = entry2.get()
    filePath = str(file_path)
    v = int(v1.get())
    if v:
            
        if filePath:
            try:
                if filePath[-3:] == "csv":

                    if int(v1.get()) ==3:
                        for frame in backframes_3:
                            frame.tkraise()
                    elif int(v1.get()) == 2:
                        for frame in backframes_2:
                            frame.tkraise()
                    elif int(v1.get()) == 1:
                        for frame in backframes_1:
                            frame.tkraise()
                else:
                    messagebox.showerror("error","csvファイルを選択してください")
            
            except:
                messagebox.showerror("error", "適切なパスを入力してください")
        else:
            messagebox.showerror("error", "パスの指定がありません。")
    else:
        messagebox.showerror("error","形式が選択されていません")

def callNewframe(mk1,mv1,mk2,mv2,mk3,mv3):
    root1 = Tk()
    root1.geometry("400x300")
    root1.title("おすすめの決行日")
    #結果表示用ページ
    # Backframe4-1

    bf4_1 = ttk.Frame(root1, padding = 10)
    bf4_1.grid(row=0, column=1, sticky=NSEW)

    # back labe4-1

    bl4_1 = ttk.Label(bf4_1, text="第一候補の日程は："+str(mk1)+"　得点は"+str(mv1), padding=(5, 2))
    bl4_1.pack(side = LEFT)

    # Backframe4-2

    bf4_2 = ttk.Frame(root1, padding = 10)
    bf4_2.grid(row = 2,column = 1,sticky = NSEW)

    # back label4-2

    bl4_2 = ttk.Label(bf4_2, text="第二候補の日程は："+str(mk2)+"　得点は"+str(mv2), padding=(5, 2))
    bl4_2.pack(side = LEFT)

    # Backframe4-3

    bf4_3 = ttk.Frame(root1, padding = 10)
    bf4_3.grid(row=5, column=1, sticky=NSEW)

    # back label4-3
    bl4_3 = ttk.Label(bf4_3, text="第三候補の日程は："+str(mk3)+"　得点は"+str(mv3), padding=(5, 2))
    bl4_3.pack(side = LEFT)

    # Backframe4-4

    bf4_4 = ttk.Frame(root1, padding = 10)
    bf4_4.grid(row=7, column=1, sticky=NSEW)

    # back label4-4
    bl4_4 = ttk.Label(bf4_4, text="最適な日にちは："+str(mk1), padding=(5, 2))
    bl4_4.pack(side = LEFT)



    backframes_4 = [bf4_1,bf4_2,bf4_3,bf4_4]

    root1.mainloop()

def anaSheet(d,maru,batsu,sankaku=0,niju=0):
    new_profile = []#一番欲しいデータのリストを作る
    yotei={}
    
    with open(d,'rt',newline='') as csvfile:#csvファイルを開く,　(\)ではなく(/)を使う＆ちゃんとディレクトリを書くとエラーが起きにくくなる
        reader = csv.reader(csvfile)
        profile = [row for row in reader]#行と列をしっかり分ける
    """#何も除去しないのでこれは消去
    i = profile[0].index('名前')

    for f in profile:
        x = f.pop(i)#その人の部分を削除
        new_profile.append(f)
    """
    new_profile = profile

    x = new_profile.pop()#最終更新日時を消去

    """#今回は表を表示しない予定
    print('使用した表:')
    for hyo in new_profile:
        print(hyo)#一覧表を表示
    """

    keys = []#キーを格納するリストを作成
    values = []#値を格納するリストを作成
    for nittei in new_profile[1:]:
        keys.append(nittei[0])#キーを格納するリストの中に日付を格納する
        point = 0
        
        for sign in nittei[1:]:
            if int(v1.get()) == 1:
                if sign == "○":#○の時
                    point+=maru
                elif sign == "×":#xの時
                    point+=batsu
            elif int(v1.get()) ==2:
                if sign == "○":#○の時
                    point+=maru
                elif sign == "△":#△の時
                    point+=sankaku
                else:#×の時
                    point+=batsu
            elif int(v1.get()) ==3:
                if sign == '◎':#◎の時
                    point+=niju
                elif sign == "○":#○の時
                    point+=maru
                elif sign == "△":#△の時
                    point+=sankaku
                else:#×の時は0点
                    point+=batsu
        values.append(point)#値を格納するリストの中に得点を格納する


    yotei.update(zip(keys, values))#辞書型を完成させる


    #print("\n\n")
    #print("日付ごとの得点：")
    
    max_value1 = 0#値の最大値を格納する変数を定義
    max_key1 = ""#最大値の時のキーを格納するための変数を定義
    for key, value in yotei.items():
        #print(key, value)
        if value > max_value1:
            max_value1 = value
            max_key1 = key

    x = yotei.pop(max_key1)#第二候補のために最大値を消去する

    #print("\n第1候補の日にちは")
    #print(str(max_key1)+"（得点が"+str(max_value1)+"点）")

    max_value2 = 0#変数のリセット
    max_key2 = ""
    for key, value in yotei.items():
        if value > max_value2:
            max_value2 = value
            max_key2 = key

    x = yotei.pop(max_key2)

    #print("\n第2候補の日にちは")
    #print(str(max_key2)+"（得点が"+str(max_value2)+"点）")

    max_value3 = 0
    max_key3= ""
    for key, value in yotei.items():
        if value > max_value3:
            max_value3 = value
            max_key3 = key

    #print("\n第3候補の日にちは")
    #print(str(max_key3)+"（得点が"+str(max_value3)+"点）")

    #print(max_key1,max_value1,max_key2,max_value2,max_key3,max_value3)
    callNewframe(max_key1,max_value1,max_key2,max_value2,max_key3,max_value3)



    
def conductMain():
    file_path3 = entry2.get()
    filePath = str(file_path3)
    if int(v1.get()) ==1:
        maru = int(entryo1.get())#引数の習得
        batsu = int(entryx1.get())
        anaSheet(filePath,maru,batsu)
    elif int(v1.get()) ==2:
        maru = int (entryo2.get())
        batsu = int(entryx2.get())
        sankaku = int(entryt2.get())
        anaSheet(filePath,maru,batsu,sankaku)
    elif int(v1.get()) == 3:
        maru = int(entryo2.get())
        batsu = int(entryx3.get())
        sankaku = int(entryt3.get())
        niju = int(entryd3.get())
        anaSheet(filePath,maru,batsu,sankaku,niju)

    #for frame in backframes_4:#結果表示画面を開く
        #frame.tkraise()
    



# アプリのウィンドウを作る
root = Tk()
root.geometry("400x300")
root.title("ファイルを選択してください")


# Frame2の作成
frame2 = ttk.Frame(root, padding=10)
frame2.grid(row=0, column=1, sticky=NSEW)

# 「ファイル参照」ラベルの作成
IFileLabel1 = ttk.Label(frame2, text="ファイル参照＞＞", padding=(5, 2))
IFileLabel1.pack(side=LEFT)
# 「ファイル参照」エントリーの作成
entry2 = StringVar()
IFileEntry = ttk.Entry(frame2, textvariable=entry2, width=30)
IFileEntry.pack(side=LEFT)

# 「ファイル参照」ボタンの作成
IFileButton = ttk.Button(frame2, text="参照", command=filedialog_clicked)
IFileButton.pack(side=LEFT)
IFileButton.pack()

#Frame4の作成
frame4 = ttk.Frame(root,padding = 10)
frame4.grid(row=2, column=1, sticky=NSEW)

    

# 「形式を選択してください」ラベルの作成
IFileLabel2 = ttk.Label(frame4, text="形式を選択してください", padding=(5, 2))
IFileLabel2.pack()

# Frame5の作成
frame5 = ttk.Frame(root, padding=10)
frame5.grid(row=5,column=1,sticky=NSEW)

# 「  」ラベルの作成
IFileLabel3 = ttk.Label(frame5, text="         ", padding=(5, 2))
IFileLabel3.pack(side = LEFT)

# Radiobutton 1
v1 = StringVar()
v1.set('0') # 初期化
rb1 =ttk.Radiobutton(
    frame5,  text='○×           ',
    value = 1,
    variable=v1)

rb1.pack(side = LEFT)

     
# Radiobutton 2
rb2 =ttk.Radiobutton(
    frame5,  text='○△×         ',
    value = 2,
    variable=v1)

rb2.pack(side = LEFT)

# Radiobutton 3
rb3 =ttk.Radiobutton(
    frame5,  text='◎○△×',
    value = 3,
    variable=v1)

rb3.pack(side = LEFT)


# Frame3の作成
frame3 = ttk.Frame(root, padding=10)
frame3.grid(row = 7,column = 1,sticky = NSEW)

file_path2 = entry2.get()
filePath = str(file_path2)

# 次へボタンの設置
button1 = ttk.Button(frame3, text="次へ", command=toNextpage)
button1.pack(fill = "x", padx=30, side = "right")

# Frame6の作成
frame6 = ttk.Frame(root, padding=10)
frame6.grid(row = 9,column = 1,sticky = NSEW)

# Frame7の作成
frame7 = ttk.Frame(root, padding=10)
frame7.grid(row = 11,column = 1,sticky = NSEW)


button1.pack()


front_frames = [frame2,frame3,frame4,frame5,frame6,frame7]


#ox用ページ
# Backframe1-1

bf1_1 = ttk.Frame(root, padding = 10)
bf1_1.grid(row=0, column=1, sticky=NSEW)

# back label1-1

bl1_1 = ttk.Label(bf1_1, text="点数を入力してください", padding=(5, 2))
bl1_1.pack()



# Backframe1-2

bf1_2 = ttk.Frame(root, padding = 10)
bf1_2.grid(row = 2,column = 1,sticky = NSEW)

# back label1-2

bl1_2 = ttk.Label(bf1_2, text="○ 　=  ", padding=(5, 2))
bl1_2.pack(side = LEFT)

# 「o」エントリーの作成
entryo1 = StringVar()
IFileEntryo1 = ttk.Entry(bf1_2, textvariable=entryo1, width=10)
IFileEntryo1.insert(END,"1")
IFileEntryo1.pack(side=LEFT)
# Backframe1-3

bf1_3 = ttk.Frame(root, padding = 10)
bf1_3.grid(row=5, column=1, sticky=NSEW)

# back label1-3
bl3 = ttk.Label(bf1_3, text=" ✕    =  ", padding=(5, 2))
bl3.pack(side = LEFT)




# 「x」エントリーの作成
entryx1 = StringVar()
IFileEntryx1 = ttk.Entry(bf1_3, textvariable=entryx1, width=10)
IFileEntryx1.insert(END,"0")
IFileEntryx1.pack(side=LEFT)
# Backframe1-4

bf1_4 = ttk.Frame(root, padding = 10)
bf1_4.grid(row=7, column=1, sticky=NSEW)


points1 = [entryo1,entryx1]

# 実行ボタンの設置
button2 = ttk.Button(bf1_4, text="実行" ,command = conductMain)
button2.pack(fill = "x", padx=30, side = "right")

backframes_1 = [bf1_1,bf1_2,bf1_3,bf1_4]

#o△x用ページ
# Backframe2-1

bf2_1 = ttk.Frame(root, padding = 10)
bf2_1.grid(row=0, column=1, sticky=NSEW)

# back labe2-1

bl2_1 = ttk.Label(bf2_1, text="一個当たりの点数を入力してください", padding=(5, 2))
bl2_1.pack()

# Backframe2-2

bf2_2 = ttk.Frame(root, padding = 10)
bf2_2.grid(row = 2,column = 1,sticky = NSEW)

# back label2-2

bl2_2 = ttk.Label(bf2_2, text="o   =  ", padding=(5, 2))
bl2_2.pack(side = LEFT)

# 「o」エントリーの作成
entryo2 = StringVar()
IFileEntryo2 = ttk.Entry(bf2_2, textvariable=entryo2, width=10)
IFileEntryo2.insert(END,"2")
IFileEntryo2.pack(side=LEFT)

# Backframe2-3

bf2_3 = ttk.Frame(root, padding = 10)
bf2_3.grid(row=5, column=1, sticky=NSEW)

# back label2-3
bl2_3 = ttk.Label(bf2_3, text="△  =  ", padding=(5, 2))
bl2_3.pack(side = LEFT)

# 「△」エントリーの作成
entryt2 = StringVar()
IFileEntryt2 = ttk.Entry(bf2_3, textvariable=entryt2, width=10)
IFileEntryt2.insert(END,"1")
IFileEntryt2.pack(side=LEFT)

# Backframe2-4

bf2_4 = ttk.Frame(root, padding = 10)
bf2_4.grid(row=7, column=1, sticky=NSEW)

# back label2-4
bl2_4 = ttk.Label(bf2_4, text="x   =  ", padding=(5, 2))
bl2_4.pack(side = LEFT)

# 「x」エントリーの作成
entryx2 = StringVar()
IFileEntryx2 = ttk.Entry(bf2_4, textvariable=entryx2, width=10)
IFileEntryx2.insert(END,"0")
IFileEntryx2.pack(side=LEFT)

#Backframe2-5

bf2_5 = ttk.Frame(root,padding = 10)
bf2_5.grid(row = 11,column = 1 ,sticky = NSEW)

# 実行ボタンの設置
button2_2 = ttk.Button(bf2_5, text="実行" ,command = conductMain)
button2_2.pack(fill = "x", padx=30, side = "right")


backframes_2 = [bf2_1,bf2_2,bf2_3,bf2_4,bf2_5]




#◎o△x用ページ
# Backframe3-1

bf3_1 = ttk.Frame(root, padding = 10)
bf3_1.grid(row=0, column=1, sticky=NSEW)

# back labe3-1

bl3_1 = ttk.Label(bf3_1, text="一個当たりの点数を入力してください", padding=(5, 2))
bl3_1.pack()

# Backframe3-2

bf3_2 = ttk.Frame(root, padding = 10)
bf3_2.grid(row = 2,column = 1,sticky = NSEW)

# back label3-2

bl3_2 = ttk.Label(bf3_2, text="◎  =  ", padding=(5, 2))
bl3_2.pack(side = LEFT)

# 「◎」エントリーの作成
entryd3 = StringVar()
IFileEntryd3 = ttk.Entry(bf3_2, textvariable=entryd3, width=10)
IFileEntryd3.insert(END,"2")
IFileEntryd3.pack(side=LEFT)

# Backframe3-3

bf3_3 = ttk.Frame(root, padding = 10)
bf3_3.grid(row=5, column=1, sticky=NSEW)

# back label3-3
bl3_3 = ttk.Label(bf3_3, text="o   =  ", padding=(5, 2))
bl3_3.pack(side = LEFT)

# 「o」エントリーの作成
entryo3 = StringVar()
IFileEntryo3 = ttk.Entry(bf3_3, textvariable=entryo3, width=10)
IFileEntryo3.insert(END,"1")
IFileEntryo3.pack(side=LEFT)

# Backframe3-4

bf3_4 = ttk.Frame(root, padding = 10)
bf3_4.grid(row=7, column=1, sticky=NSEW)

# back label3-4
bl3_4 = ttk.Label(bf3_4, text="△  =  ", padding=(5, 2))
bl3_4.pack(side = LEFT)

# 「△」エントリーの作成
entryt3 = StringVar()
IFileEntryt3 = ttk.Entry(bf3_4, textvariable=entryt3, width=10)
IFileEntryt3.insert(END,"0")
IFileEntryt3.pack(side=LEFT)

#backframe3-5
bf3_5 = ttk.Frame(root,padding = 10)
bf3_5.grid (row = 9, column = 1, sticky = NSEW)

#back label 3-5
bl3_5 = ttk.Label(bf3_5,text = "   x   =   ")
bl3_5.pack(side = LEFT)

# 「x」エントリーの作成
entryx3 = StringVar()
IFileEntryx3 = ttk.Entry(bf3_5, textvariable=entryx3, width=10)
IFileEntryx3.insert(END,"-1")
IFileEntryx3.pack(side=LEFT)

#backframe3-6
bf3_6 = ttk.Frame(root,padding = 10)
bf3_6.grid (row = 11, column = 1, sticky = NSEW)

# 実行ボタンの設置
button2_3 = ttk.Button(bf3_6, text="実行" ,command = conductMain)
button2_3.pack(fill = "x", padx=30, side = "right")



backframes_3 = [bf3_1,bf3_2,bf3_3,bf3_4,bf3_5,bf3_6]

"""
#結果表示用ページ
# Backframe4-1

bf4_1 = ttk.Frame(root, padding = 10)
bf4_1.grid(row=0, column=1, sticky=NSEW)

# back labe4-1

bl4_1 = ttk.Label(bf4_1, text="第一候補の日程は："+str(max_key1)+"　得点は"+str(max_value1), padding=(5, 2))
bl4_1.pack(side = LEFT)

# Backframe4-2

bf4_2 = ttk.Frame(root, padding = 10)
bf4_2.grid(row = 2,column = 1,sticky = NSEW)

# back label4-2

bl4_2 = ttk.Label(bf4_2, text="第二候補の日程は："+str(max_key2)+"　得点は"+str(max_value2), padding=(5, 2))
bl4_2.pack(side = LEFT)

# Backframe4-3

bf4_3 = ttk.Frame(root, padding = 10)
bf4_3.grid(row=5, column=1, sticky=NSEW)

# back label4-3
bl4_3 = ttk.Label(bf4_3, text="第三候補の日程は："+str(max_key3)+"　得点は"+str(max_value3), padding=(5, 2))
bl4_3.pack(side = LEFT)

# Backframe4-4

bf4_4 = ttk.Frame(root, padding = 10)
bf4_4.grid(row=7, column=1, sticky=NSEW)

# back label4-4
bl4_4 = ttk.Label(bf4_4, text="最適な日にちは：", padding=(5, 2))
bl4_4.pack(side = LEFT)



backframes_4 = [bf4_1,bf4_2,bf4_3,bf4_4]
"""

for frame in front_frames:
    frame.tkraise()

root.mainloop()
