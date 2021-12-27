import socket
import os

HOST = '127.0.0.1'
PORT = 1234
BUFFERSIZE=1024
FORMAT='utf-8'

def main():
    Flag=True
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while Flag:
        source=input('請輸入傳輸檔案完整路徑(輸入end結束):')
        if source=='end':
            s.sendto('end'.encode(FORMAT),(HOST,PORT))
            print('[Client] 客戶端已結束!')
            os.system('PAUSE')
            Flag=False
            break
        try:
            filesize=str(os.path.getsize(source))
            s.sendto(source.encode(FORMAT),(HOST,PORT))
            s.sendto(filesize.encode(FORMAT),(HOST,PORT))
            with open(source,'rb')as f:
                while True:
                    data=f.read()
                    if not data:
                        f.close()
                        break
                    s.sendto(data,(HOST,PORT))
            print('[Client] 檔案傳輸完成')
            msg=s.recv(BUFFERSIZE).decode(FORMAT)
            print(f'[SERVER] {msg}')
        except:
            print('[ERROR] 檔案開啟失敗或路徑有問題')

            
if __name__=='__main__':
    main()