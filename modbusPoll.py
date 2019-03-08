from GETPARAMS import _ai_type_data
from GETPARAMS import _ai_org_data
from GETPARAMS import _ai_real_data
from GETPARAMS import _di_data
from GETPARAMS import _do_data
from GETPARAMS import _do_write_data
from GETPARAMS import _ao_data
from GETPARAMS import _ao_write_data

def read_TYPE(id):
    #AI
    if id >= 97 and id <= 112 :
        protocol=format(id, 'x')+"0200000004"

    protocol = LRC(protocol)
    return proc_PROTOCOL(protocol)

def read_IO(id):
    #AI
    if id >= 97 and id <= 112 :
        protocol=format(id,'x')+"0400000004"
    #AO
    if id >= 129 and id <= 144 :
        protocol=format(id,'x')+"0300050004"
    #DI
    if id >= 65 and id <= 80 :
        protocol=format(id,'x')+"0200000008"
    #DO
    if id >= 33 and id <= 48 :
        protocol=format(id,'x')+"0100000004"

    protocol=LRC(protocol)
    return proc_PROTOCOL(protocol)

def write_IO(id,data):
    #DO
    if id >= 33 and id <= 48 :
        protocol=format(id, 'x')+"0F0000000401"+format(format(data, "x").zfill(2))

    '''
     #AO
    if id >= 129 and id <= 144 :
        protocol=format(id,'x')+"1000"+(5+port-1).zfill(2)+"000102"+format(hex(data*100).zfill(4),"x")
    '''
    protocol=LRC(protocol)
    return proc_PROTOCOL(protocol)

def proc_PROTOCOL(protocol):
    _readarray = bytearray()
    _readarray.append(58)     #起始值
    for i in protocol:
        _readarray.append(ord(i))     #起始值
    _readarray.append(13)  #0D
    _readarray.append(10)  #0A
    return _readarray

def EXEC_AI_ValueByCurrent(smax,smin,data):
        return (smax-smin)/16 *(data-4)+smin

def EXEC_AI_ValueByVoltage(smax,smin,data):
    return (smax-smin)/16 *(data)+smin

def LRC(protocol):
    checksum=0
    i=0
    while i<len(protocol)-1:
        checksum=checksum+int(protocol[i:i+2],16)
        i+=2
    checksum=protocol+format(255-checksum+1,"x")
    return checksum.upper()

def PROCESS(data):
  try:
    _modbus=[]
    i = 0
    while i < len(data)-1:
        _modbus.append(data[i:i+2])
        i += 2

    #AI Data
    if(int(_modbus[0],16) >= int("0x61", 16) and int(_modbus[0],16) <= int("0x70", 16)):
        #AI TYPE
      if(int(_modbus[1], 16)==int("0x2",16)):
        j=0
        for i in reversed(format(int(_modbus[3], 16), 'b').zfill(4)):
            _ai_type_data[int(_modbus[0], 16)-int("0x61", 16)][j]=i
            j += 1
      else:
        #AI DATA
        j=0
        for i in range(3,3+int(_modbus[2], 16),2):
            _ai_org_data[int(_modbus[0], 16)-int("0x61", 16)][j]=round(int(_modbus[i]+_modbus[i+1], 16)/1000, 2)
            j += 1

    #DI Data
    if(int(_modbus[0],16)>=int("0x41", 16) and int(_modbus[0],16)<=int("0x50", 16)):
      if(int(_modbus[1], 16)==int("0x2",16)):
        j=0
        for i in reversed(format(int(_modbus[3], 16), 'b').zfill(8)):
            _di_data[int(_modbus[0], 16)-int("0x41", 16)][j]=i
            j+=1

    #DO Data
    if(int(_modbus[0],16)>=int("0x21", 16) and int(_modbus[0],16)<=int("0x30", 16)):
        if(int(_modbus[1], 16)==int("0x1",16)):
            j=0
            #取得資料長度
            for i in reversed(format(int(_modbus[3], 16), 'b').zfill(4)):
                _do_data[int(_modbus[0], 16)-int("0x21", 16)][j]=i
                j+=1

  except Exception as e:
      print("modbuspoll error:"+str(e))

def READ_ORG_AI(cardid,port):
    return _ai_org_data[cardid-1][port-1];

def READ_AI(cardid,port):
    return _ai_real_data[cardid-1][port-1];

def READ_DI(cardid,port):
    return _di_data[cardid-1][port-1];

def READ_DO(cardid,port):
    return _do_data[cardid-1][port-1];

def READ_AO(cardid,port):
    return _ao_data[cardid-1][port-1];