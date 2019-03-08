import GETPARAMS,threading
from TCPSERVER import ThreadedServer
from READVZIO import READ_VAPAAZ
from WEBSOCKET import WEBSOCKET_CLIENT
from webapi import restful

def main():
  READ_VAPAAZ()
  WEBSOCKET_CLIENT()
  ThreadedServer().listen()


if __name__ == '__main__':
  #查詢資料庫內各io卡的數量
  GETPARAMS.GETIOQTY()
  #restful.run()
  #載入參數後，啟動執行緒
  threading.Thread(target=restful.run).start()
  main()


  while True:
      pass

