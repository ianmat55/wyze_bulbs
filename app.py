from flask import Flask, render_template, redirect
import os
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import config


app = Flask(__name__)
app.config['SECRET_KEY'] = config.key


@app.route('/', methods=['GET', 'POST'])
def index():
	render_template('base.html')
