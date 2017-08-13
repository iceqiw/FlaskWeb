#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com

from wechat import wx
from flask import request
import hashlib
import xml.etree.ElementTree as ET
import logging
from ..service import wechat_service


@wx.route('/g',methods=['GET'])
def check_signature():
    try:
        token = '20124003'  # 微信配置所需的token
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        s = ''.join(sorted([timestamp, nonce, token]))
        sha1 = hashlib.sha1(s.encode('utf-8')).hexdigest()
        logging.debug(sha1)
        if sha1 == signature:
            return echostr
        else:
            return "error"
    except Exception as e:
            logging.error('微信sign校验,---Exception' + str(e))


@wx.route('/g',methods=['POST'])
def doHandle():
    xml = ET.fromstring(request.data)
    out=wechat_service.parse(xml)
    return out