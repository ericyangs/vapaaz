import psycopg2
import numpy as np
from websocket import create_connection

_readsleep=0.1
_heartbit=5
_doactflag=0
_aoactflag=0

wsurl="ws://iot.vapaa.tw:18650/websocket"

_ai_type_data=np.zeros((16, 4),int)
_ai_org_data=np.zeros((16, 4))
_ai_real_data=np.zeros((16, 4))
_ai_min_level_data=np.zeros((16, 4))
_ai_max_level_data=np.zeros((16, 4))
_di_data=np.zeros((16, 8),int)
_ao_data=np.zeros((16, 8))
_ao_write_data=np.zeros((16, 8))
_do_data=np.zeros((16, 4),int)
_do_write_data=np.zeros((16, 4),int)

_aiqty=0
_aoqty=0
_diqty=0
_doqty=0

_tcphost = ''
_tcpport = 26500

_uuid=""

_dbname="vapaaz"
_username="pi"
_userpwd="asdwsX123"
_host="127.0.0.1"
_port=5432
_connpsql= psycopg2.connect(database=_dbname, user=_username, password=_userpwd, host=_host, port=_port)

def GETIOQTY():
  _cur=_connpsql.cursor()
  _cur.execute("select * from infobase")
  rows = _cur.fetchall()
  for row in rows:
    global _aiqty,_aoqty,_diqty,_doqty,_uuid
    _uuid=row[0]
    _aiqty=row[1]
    _aoqty=row[2]
    _diqty=row[3]
    _doqty=row[4]
