# 計算機網路作業

## 使用套件

   socket ->用於架設通訊
   
   os ->用於開檔 關檔 取得檔案大小等等

## 設定

   Host預設為 127.0.0.1 Port預設為 1234
   
   BUFFERSIZE預設為 1024 FORMAT預設為utf-8
   
   若須修改可於Server.py Client.py 4到7行修改
   
   切記Server和Client都需修改

## 使用方法

   先選擇使用TCP協定或UDP協定
   
   1.執行 Server.py
    
   ```
    python "(Server.py路徑)"
   ```
    
   2.輸入伺服端存放資料的地方其路徑
   
   3.執行 Client.py
   
   ```
    python "(Client.py路徑)"
   ```
    
   4.輸入欲傳輸資料的完整路徑
   
   5.若要結束程式 可於Client輸入 end
      伺服端和客戶端都會關閉

## 作者

   B10917027 四資工二A 吳柏叡
