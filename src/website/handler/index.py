#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
from website import api
from ..service import queryService
from flask import jsonify

@api.route('/g')
def doHandle():
    queryService.printAll()
    return jsonify(res = 0)