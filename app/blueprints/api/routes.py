from flask import jsonify, request, redirect, flash, url_for
from . import bp as app
from app.blueprints.main.models import Pet
from flask_login import current_user
from app import db

# user = current_user.id

