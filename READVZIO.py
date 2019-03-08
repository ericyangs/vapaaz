import modbusPoll,serial,time,threading
import RPi.GPIO as GPIO
import GETPARAMS
EN_485 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485, GPIO.OUT)
conn = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.3)

def handle_data(data):
    print(data)
    modbusPoll.PROCESS(data)

def SEND_DATA(id,type,value):
    GPIO.setup(EN_485, GPIO.OUT)
    GPIO.output(EN_485, GPIO.HIGH)

    if conn.isOpen()==False:
        conn.open()

    if type.upper() == 'TYPE':
        if id >= 97 and id <= 112:
            conn.write(modbusPoll.read_TYPE(id))

    if type.upper() == 'DATA':
        conn.write(modbusPoll.read_IO(id))

    if type.upper()=='WRITEDO':
        conn.write(modbusPoll.write_IO(id, value))
        time.sleep(0.02)
        SEND_DATA(id, 'data',"0")
    #if type.upper()=="WRITEAO":
    #    print("write ao")
    GETPARAMS._doactflag=0
    time.sleep(0.02)

def RECEIVE_DATA():
    GPIO.setup(EN_485, GPIO.OUT)
    GPIO.output(EN_485, GPIO.LOW)
    _resp = conn.readline()
    return _resp

def RECONNECT_485():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    conn = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.2)

def CHECK_DOACTION():
    do='21'
    if GETPARAMS._do_data.any()!=GETPARAMS._do_write_data.any():
       time.sleep(0.1)
       GETPARAMS._doactflag=1
       for cardid in range(GETPARAMS._doqty):
           if GETPARAMS._do_data[cardid].any() != GETPARAMS._do_write_data[cardid].any():
             b=GETPARAMS._do_write_data[cardid]
             SEND_DATA(int(do,16)+cardid, 'writedo', b.dot(2**GETPARAMS.np.arange(b.size)))
    GETPARAMS._doactflag=0

class READ_VAPAAZ(object):
    def __init__(self):
        self.stuff = 'Read Vapaaio'
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()

    def run(self):
        try:
            read_ai_type=0
            while True:
                if GETPARAMS._aiqty>0:
                    if read_ai_type>5:
                        read_ai_type=0
                    ai='61'
                    for i in range(GETPARAMS._aiqty):
                        CHECK_DOACTION()
                        if GETPARAMS._doactflag==0:
                            if read_ai_type==0:
                              SEND_DATA(int(ai,16)+i, 'type',0)
                              _resp=RECEIVE_DATA()
                              if len(_resp) > 0:
                                _data=(_resp.decode("utf-8", "ignore")).strip().split(":")
                                if len(_data) > 1:
                                    handle_data(_data[1])
                                time.sleep(GETPARAMS._readsleep)
                              else:
                                conn.close()
                                RECONNECT_485()

                            SEND_DATA(int(ai,16)+i, 'data',0)
                            _resp=RECEIVE_DATA()
                            if len(_resp) > 0:
                              _data=(_resp.decode("utf-8", "ignore")).strip().split(":")
                              if len(_data) > 1:
                                handle_data(_data[1])
                                time.sleep(GETPARAMS._readsleep)
                            else:
                              conn.close()
                              RECONNECT_485()

                    read_ai_type+=1

                #GET DI
                if GETPARAMS._diqty>0:
                    di='41'
                    for i in range(GETPARAMS._diqty):
                        CHECK_DOACTION()
                        if GETPARAMS._doactflag==0:
                          SEND_DATA(int(di, 16)+i, 'data',0)
                          _resp=RECEIVE_DATA()
                          if len(_resp) > 0:
                             _data=(_resp.decode("utf-8", "ignore")).strip().split(":")
                             if len(_data) > 1:
                                handle_data(_data[1])
                                time.sleep(GETPARAMS._readsleep)
                          else:
                            conn.close()
                            RECONNECT_485()

                #GET DO
                if GETPARAMS._doqty > 0:
                    do = '21'
                    for i in range(GETPARAMS._doqty):
                        CHECK_DOACTION()
                        if GETPARAMS._doactflag==0:
                          SEND_DATA(int(do, 16)+i, 'data',"0")
                          _resp=RECEIVE_DATA()
                          if len(_resp) > 0:
                             _data=(_resp.decode("utf-8", "ignore")).strip().split(":")
                             if len(_data) > 1:
                                handle_data(_data[1])
                                time.sleep(GETPARAMS._readsleep)
                             else:
                                conn.close()
                                RECONNECT_485()

        except Exception as e:
            print(str(e))