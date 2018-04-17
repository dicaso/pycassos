# -*- coding: utf-8 -*-
"""Run pycassos server

Loads app from main module and runs it.
"""
from pycassos import app

if __name__ == '__main__':
     app.run(port=4444) #debug=True, host='0.0.0.0'
