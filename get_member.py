#Kohei Miyoshi
import csv#標準ライブラリーの中にcsvファイルの編集用のモジュールが入っている
new_profile = []#一番欲しいデータのリストを作る
yotei={}

want_date = "11/17(水)"
start_member = []
added_member = []
with open('C:/Users/koumi/Documents/densuke_get_date/11gatsu.csv','rt',newline='') as csvfile:#csvファイルを開く,　(\)ではなく(/)を使う＆ちゃんとディレクトリを書くとエラーが起きにくくなる
    reader = csv.reader(csvfile)
    profile = [row for row in reader]#行と列をしっかり分ける

new_profile = profile


x = new_profile.pop()#最終更新日時を消去

"""
print('使用した表:')
for hyo in new_profile:
    print(hyo)#一覧表を表示
"""
for i in range(1,len(new_profile)):
    if new_profile[i][0] == want_date:
        for j in range(len(new_profile[i])):
            if new_profile[i][j] == "○":
                start_member.append(new_profile[0][j])
            elif new_profile[i][j] == "△":
                added_member.append(new_profile[0][j])

print(f"参加者は「{start_member}」")
print(f"6限からの参加者は「{added_member}」")
                






