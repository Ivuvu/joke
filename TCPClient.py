# coding: UTF-8
# クライアントを作成
from socket import *

serverAddress = '127.0.0.1'
serverPort = 50000

# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う
#ソケットの作成(socket)
clientSocket = socket(AF_INET, SOCK_STREAM)

# サーバを指定(connect)
clientSocket.connect((serverAddress, serverPort))
number = input(
'あなたの星座に対応する番号を以下から入力してください\n \
おひつじ座: 0 \n おうし座: 1 \n ふたご座: 2 \n かに座: 3 \n しし座: 4 \n \
おとめ座: 5 \n てんびん座: 6 \n さそり座: 7 \n いて座: 8 \n やぎ座: 9 \n \
みずがめ座: 10 \n うお座: 11 \n '
)

# サーバに番号を送る(send)
clientSocket.send(number.encode())
# 

#番号に応じた占いの結果を受け取る
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())


#ソケットをクローズ(close)
clientSocket.close()
