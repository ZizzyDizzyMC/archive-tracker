from threading import Thread
import re
import random
import time
import requests
import websockets
import json
import sqlite3
import threading
import os
import configparser
import sys
from datetime import datetime
import jsonpickle
from flask import Flask


# Create the first app, this just gives me hello world.
# I have no idea what I'm doing part 1:

app = Flask(__name__)

# Is this even needed?
threads = []
lock = threading.Lock()
threadlimiter = threading.BoundedSemaphore(10)



# Hello
@app.route('/')
def hello():
    return 'Hello, World!'

# Get some stuff resembling WERK.  That's right, go back to work I know you're not on break.
@app.route('/get-work')
async def get_work():
    item = ('none',)
    conn = sqlite3.connect('database.db')
    db = conn.cursor()
    db.execute('SELECT url FROM link_urls WHERE status="None" LIMIT 10')
    result = db.fetchall()
    conn.close()
    return str(result)
