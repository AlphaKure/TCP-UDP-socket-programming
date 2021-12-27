import socket
import os

HOST='127.0.0.1'
PORT=1234
BUFFERSIZE=1024
FORMAT='utf-8'

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #創建socket

    '''
    socket.AF_UNIX:本機通訊
    socket.AF_INET:網路通訊 (較常用)
    socket.AF_INET6:IPv6的網路通訊
    socket.SOCK_STREAM:TCP協定 (較常用)
    socket.SOCK_DGRAM:UDP協定 (較常用)

    '''
    Flag=True
    RESULTPATH=input('請輸入接收檔案存放位置:')+'\\'
    print(f'[SETUP] 結果存放目錄:{RESULTPATH}')
    s.bind((HOST,PORT)) #綁定HOST和PORT
    s.listen(2) #最高連線數量設定
    print('[SETUP] 伺服器準備就緒!')
    while Flag:
        conn,addr=s.accept()
        print(f'[Connect] {addr}')
        while Flag:
            filename=conn.recv(BUFFERSIZE).decode(FORMAT)
            msg='目標檔案確認: '+filename
            conn.send(msg.encode(FORMAT))
            if filename=='end':
                Flag=False
                print('[SERVER] 伺服端收到停止指令 已關閉')
                os.system('PAUSE')
                break
            print(f'[Client] 傳輸檔案: {filename}')
            filesize=conn.recv(BUFFERSIZE).decode(FORMAT)
            msg='獲得檔案大小:'+filesize
            conn.send(msg.encode(FORMAT))
            with open(RESULTPATH+filename,'wb')as f:
                data=conn.recv(int(filesize))
                if not data:
                    f.close()
                f.write(data)
            resultsize=os.path.getsize(RESULTPATH+filename)
            print(f'[SERVER] 傳輸完成。\n原檔案大小:{filesize}\n接收檔案大小:{resultsize}')
            msg='伺服端完成接收檔案!'+filename
            conn.send(msg.encode(FORMAT))
            
            

if __name__=='__main__':
    main()