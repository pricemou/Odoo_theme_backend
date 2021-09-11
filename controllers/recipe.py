# -*- coding: utf-8 -*-
from odoo import http
import json
from math import *


class JecuisineApi(http.Controller):
    
    def convert_float_to_int(self, number):
        data = ceil(round(float(number) * 60, 2))
        return data