import threading,time
from GETPARAMS import _heartbit
from GETPARAMS import _ai_type_data
from GETPARAMS import _ai_org_data
from GETPARAMS import _ai_real_data
from GETPARAMS import _di_data
from GETPARAMS import _do_data
from GETPARAMS import _do_write_data
from GETPARAMS import _ao_data
from GETPARAMS import _ao_write_data

class WEBSOCKET_CLIENT(object):
    def __init__(self):
        self.stuff = 'Send to Websocket Server'
        self.interval = _heartbit
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            #print("send to websocket")
            '''
            print("=== AI TYPE===")
            print(_ai_type_data)
            print("=== AI ===")
            print(_ai_org_data)
            print("=== DI ===")
            print(_di_data)
            print("=== DO ===")
            print(_do_data)
            
            #ws = create_connection("ws://localhost:8080/websocket")
            #ws.send("Hello, World")
            #print("Sent")
            #print("Reeiving...")
            #result = ws.recv()
            #print("Received '%s'" % result)
            #ws.close()
            '''

            time.sleep(self.interval)

