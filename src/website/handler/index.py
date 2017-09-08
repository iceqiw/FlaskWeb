#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
from website import api
from ..service import queryService
from flask import jsonify
from flask import request
from core.logger import mylogging

@api.route('/user/login',methods=['POST'])
def doHandle():
    pwd=request.json['password']
    username=request.json['username']
    if pwd=='1':
        return jsonify(res = 1)
    queryService.printAll()
    return jsonify(res = 0)


@api.route('/jxSearch/<topic>')
def doSaveTpl(topic):
    mylogging.info(topic)
    alist=queryService.search(topic)
    return jsonify(alist)

