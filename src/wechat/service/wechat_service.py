#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
from model.tplModels import *
from core.logger import mylogging
import time

def parse(data):
    appid = data.find('ToUserName').text
    openid= data.find('FromUserName').text
    msgType = data.find('MsgType').text
    if msgType=='event':
        event = data.find('Event').text
        return processEvent(openid,appid,event)
    else:
        msg = data.find('Content').text
        return processMsg(openid,appid,msg)

def processEvent(openid,appid,event):
    try:
        t=Tpl.get(Tpl.tpl_key ==event)
        return reply(openid,appid,t.message)
    except:
        return "null"
    

def processMsg(openid,appid,msg):
    try:
       t=Tpl.get(Tpl.tpl_key ==msg)
       return reply(openid,appid,t.message)
    except:
        return "null"


def reply(openid,appid,tpl):
    if not tpl.strip():
        return "null"
    CreateTime = int(time.time())
    mylogging.info(tpl)
    out = tpl % (openid, appid, CreateTime)
    return out