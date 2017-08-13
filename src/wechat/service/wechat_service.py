#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com

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
    return 'event'
    

def processMsg(openid,appid,msg):
    return 'msg'


def reply(openid,appid,tpl):
    CreateTime = int(time.time())
    out = tpl % (openid, appid, CreateTime)
    return out