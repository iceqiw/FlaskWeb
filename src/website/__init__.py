#! /usr/bin/env python
# coding: utf-8

from flask import Blueprint

api = Blueprint('api', __name__)

from .handler import index
