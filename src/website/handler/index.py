#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
from website import api
from ..service import queryService

@api.route('/')
def doHandle():
    queryService.printAll()
    return 'ok'