import os
import socket

HOST = '127.0.0.1'
PORT = 1234
BUFFERSIZE=1024
FORMAT='utf-8'

def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#創建socket
        print(f'[Connect] 連線至: {HOST}:{PORT}')
        s.connect((HOST, PORT))
        print(f'[Connect] 連線成功.')
        flag=True
    except:
        print('[ERROR] 連接失敗.')
        os.system('PAUSE')
        flag=False

    while flag:
        file=input('請輸入傳輸檔案路徑(輸入 end 結束):')
        if file =='end':
            s.send('end'.encode(FORMAT))
            flag=False
            print('[Client] 客戶端已關閉')
            s.close()
            os.system('PAUSE')
        else:
            filename=os.path.basename(file)
            s.send(filename.encode(FORMAT))
            msg=s.recv(BUFFERSIZE).decode(FORMAT)
            print(f'[SERVER] {msg}')
            filesize=str(os.path.getsize(file))
            s.send(filesize.encode(FORMAT))
            msg=s.recv(BUFFERSIZE).decode(FORMAT)
            print(f'[SERVER] {msg}')
            try:
                with open(file,'rb')as f:
                    while True:
                        read=f.read()
                        s.send(read)
                        if not read:
                            break
                f.close()
                print('[Client] 檔案傳輸完成')
                msg=s.recv(BUFFERSIZE).decode(FORMAT)
                print(f'[SERVER] {msg}')
            except:
                print('[ERROR] 讀取檔案失敗')


if __name__=='__main__':
    main()