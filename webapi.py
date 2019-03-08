import GETPARAMS,os,numpy as np
from GETPARAMS import _ai_org_data
from GETPARAMS import _ai_real_data
from GETPARAMS import _ao_data
from GETPARAMS import _di_data
from GETPARAMS import _do_data
from GETPARAMS import _do_write_data

from flask import Flask, render_template
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
restful = Flask(__name__,
            template_folder=os.path.join(PROJECT_PATH, 'templates'),
            static_folder=os.path.join(PROJECT_PATH, 'static')
            )

def flaskThread():
    restful.run()

@restful.route('/')
def home():
    return render_template('index.html')


@restful.route('/getai/')
def get_all_ai():
    return str(_ai_org_data[1][1])
    pass

#get /restful/<name>/item data: {name :}/item
@restful.route('/getai/<string:cardid>/<string:port>')
def get_item_in_ai(cardid,port):
    pass

@restful.route('/getdi/')
def get_all_di():
    return str(_ai_org_data[1][1])
    pass

#get /restful/<name>/item data: {name :}/item
@restful.route('/getdi/<string:cardid>/<string:port>')
def get_item_in_di(cardid,port):
    pass


@restful.route('/getao/')
def get_all_ao():
    return str(_ai_org_data[1][1])
    pass

#get /restful/<name>/item data: {name :}/item
@restful.route('/getao/<string:cardid>/<string:port>')
def get_item_in_ao(cardid,port):
    pass

@restful.route('/getdo/')
def get_all_do():
    return str(_ai_org_data[1][1])
    pass

#get /restful/<name>/item data: {name :}/item
@restful.route('/getdo/<string:cardid>/<string:port>')
def get_item_in_do(cardid,port):
    pass

#get /restful/<name>/item data: {name :}/item
@restful.route('/setao/<string:cardid>/<string:port>/<string:value>')
def set_act_in_ao(cardid,port,value):
    _aoflag=1
    pass

#get /restful/<name>/item data: {name :}/item
@restful.route('/setdo/<string:cardid>/<string:port>/<string:value>')
def set_act_in_do(cardid,port,value):
    _do_write_data[int(cardid)-1][int(port)-1]=int(value)
    #_result = ""
    #for cardid in range(GETPARAMS._doqty+1):
    #    _result=str(cardid)+":<br>"
    #    _result=_result+np.array2string(_do_data[cardid][::-1])+"<br>"
    return str(_do_data)