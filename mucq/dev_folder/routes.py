from flask import render_template, url_for, redirect, request, Blueprint, flash
from flask_login import current_user, login_required
from mucq.main_folder.forms import SearchForm

dev = Blueprint('dev', __name__)

