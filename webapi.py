import GETPARAMS
from flask import Flask, render_template
restful = Flask(__name__)

def flaskThread():
    restful.run(host="0.0.0.0")

@restful.route('/')
def home():
    return render_template('index.html')


@restful.route('/getai/')
def get_all_ai():
    return str(GETPARAMS._ai_org_data[1][1])
    pass

#get /restful/<name>/item data: {name :}/item
@restful.route('/getai/<string:cardid>/<string:port>')
def get_item_in_ai(cardid,port):
    pass

@restful.route('/getdi/')
def get_all_di():
    return str(GETPARAMS._ai_org_data[1][1])
    pass

#get /restful/<name>/item data: {name :}/item
@restful.route('/getdi/<string:cardid>/<string:port>')
def get_item_in_di(cardid,port):
    pass


@restful.route('/getao/')
def get_all_ao():
    return str(GETPARAMS._ai_org_data[1][1])
    pass

#get /restful/<name>/item data: {name :}/item
@restful.route('/getao/<string:cardid>/<string:port>')
def get_item_in_ao(cardid,port):
    pass

@restful.route('/getdo/')
def get_all_do():
    return str(GETPARAMS._ai_org_data[1][1])
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
@restful.route('/setdo/<int:cardid>/<int:port>/<int:value>')
def set_act_in_do(cardid,port,value):
    GETPARAMS._doactflag=1
    GETPARAMS._do_write_data[int(cardid)-1][int(port)-1]=int(value)
    return "DO O:"+str(GETPARAMS._do_data)+"<br>DO W:"+str(GETPARAMS._do_write_data)