import socket
import os

HOST = '127.0.0.1'
PORT = 1234
BUFFERSIZE=1024
FORMAT='utf-8'

def main():
    Flag=True
    RESULTPATH=input('請輸入存放檔案位置:')
    if not RESULTPATH.endswith('\\'):
        RESULTPATH=RESULTPATH+'\\'
    print(f'[SETUP] 存放檔案路徑:{RESULTPATH}')
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
    s.bind((HOST,PORT))
    print('[SERVER] 伺服器端準備就緒!')
    while Flag:
        conn,addr=s.recvfrom(BUFFERSIZE)
        conn=conn.decode(FORMAT)
        if conn=='end':
            Flag=False
            print('[SERVER] 收到結束指令。伺服端已關閉!')
            break
        filename=os.path.basename(conn)
        print(f'[SERVER] 來自:{addr[0]}:{addr[1]}\n[SERVER] 收到檔案名稱:{filename}')
        filesize=int(s.recv(BUFFERSIZE).decode(FORMAT))
        try:
            with open(RESULTPATH+filename,'wb')as f:
                data=s.recv(filesize)
                print('[Client] 接收資料傳輸中')
                f.write(data)
                if not data:
                    f.close()
            print('[SERVER] 資料傳輸完畢')
            msg='伺服端資料傳輸完成'
            s.sendto(msg.encode(FORMAT),addr)
        except:
            msg='資料傳輸失敗'
            s.sendto(msg.encode(FORMAT),addr)
    os.system('PAUSE')
        

if __name__=='__main__':
    main()