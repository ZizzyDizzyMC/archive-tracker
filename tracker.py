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

@app.route('/')
def hello():
    return 'Hello, World!'



