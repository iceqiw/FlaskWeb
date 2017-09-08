#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com

from flask import Flask
from wechat import wx
from website import api

def createAPP():
    app = Flask(__name__)
    app.register_blueprint(wx, url_prefix='/wechat')
    app.register_blueprint(api, url_prefix='/api')
    return app

app=createAPP()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=19999)