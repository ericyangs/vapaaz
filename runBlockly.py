import GETPARAMS,threading
from TCPSERVER import ThreadedServer
from READVZIO import READ_VAPAAZ
from WEBSOCKET import WEBSOCKET_CLIENT
from webapi import flaskThread
#from vapaaAction import VapaaAction
import time

from blockly import blockly
blockly.run(host="0.0.0.0")


def processing():
    while(True):
        #VapaaAction()
        time.sleep(5)

def main():
  READ_VAPAAZ()
  WEBSOCKET_CLIENT()

  actionThread = threading.Thread(target=processing, args=())
  actionThread.daemon = True
  actionThread.start()

  ThreadedServer().listen()

if __name__ == '__main__':
  #查詢資料庫內各io卡的數量
  GETPARAMS.GETIOQTY()
  #restful.run()
  #載入參數後，啟動執行緒
  threading.Thread(target=flaskThread).start()
  main()
  while True:
      pass
