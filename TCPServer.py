# coding: UTF-8
# サーバを作成
from socket import *
import requests
import json
import datetime

serverPort = 50000
serverAddress = '127.0.0.1'
# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う
serverSocket = socket(AF_INET, SOCK_STREAM)

# IPアドレスとポートを指定
serverSocket.bind((serverAddress, serverPort))
# 1 接続
serverSocket.listen(1)
print('The server is ready to receive')
# connection するまで待つ


while True:
    # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
    connectionSocket, addr = serverSocket.accept()
    
    # データを受け取る
    number = int(connectionSocket.recv(1024).decode())

    #現在の日時を取得する
    date = datetime.datetime.today().strftime("%Y/%m/%d")

    # APIのURL http://api.jugemkey.jp/api/horoscope/year/month/day の形式
    res = requests.get(url='http://api.jugemkey.jp/api/horoscope/free/'+ date)

    #番号に対しての占いの結果をAPIからjson形式で入手する
    responce = json.dumps(res.json()["horoscope"][date][number],indent = 2, ensure_ascii = False)
    connectionSocket.send(responce.encode())

    kaisetsu = '占いの解説\n     content : 占いの内容\n     money : 金運（5段階評価）\n \
    job : 仕事運（5段階評価）\n     love : 恋愛運（5段階評価）\n     total :総合運（5段階評価）\n \
    item : ラッキーアイテム\n     color : ラッキーカラー\n     rank : 12星座のうち何番目に運勢がいいか\n \
    sign : 星座名 \n     day : 日にち'
    connectionSocket.send(kaisetsu.encode())

    # クライアントにデータを返す
    connectionSocket.close()
