#! /usr/bin/env python
# coding: utf-8

from flask import Blueprint

wx = Blueprint('wx', __name__)

from .handler import enter_handle
