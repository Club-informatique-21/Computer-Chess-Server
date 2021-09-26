#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Computer Chess Server
=====================
Main module.
"""
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
