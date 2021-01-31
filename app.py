import os
# library containing basic funct of python
from flask import (Flask, flash, render_template, redirect, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, chech_password_hash


app = Flask(__name__)

