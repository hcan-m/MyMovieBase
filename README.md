# MyMovieBase
MyMovieBase Python Web Application with Flask

Required Packages:
from flask import Flask, render_template, request, redirect, url_for, session
import re
import sqlite3 as sql
from sqlite3 import connect
import os.path

Path should be changed to new path of the folder in line 11.
BASE_DIR = os.path.dirname(os.path.abspath("New_Path\\MyMovieBase\\MyMovieBase_db.db"))

It should work with opening main.py if it will not work, can start manually via command prompt.
Cd C:\...\MyMovieBase
set FLASK_APP=main.py
flask run

username: test
password: test

