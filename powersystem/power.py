# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 01:20:08 2021

@author: mwang
"""


from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def power():
    return "power station"

if __name__=='__main__':
    app.run()