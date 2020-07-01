from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
#import database modules and other db tools here depends on the specs.
#from app.db import get_db

bp = Blueprint('maintenance', __name__)

@bp.route('/')
@login_required
def index():
	data_2 = [{"Select":"<input type='checkbox' id='checkbox1' name='checbox1' value=''>", "題名_1":"data", "題名_2":"46", "題名_3":"46", "題名_4":"データ", "題名_5":"7/1/2020"},
					   {"Select":"<input type='checkbox' id='checkbox1' name='checbox1' value=''>", "題名_1":"data", "題名_2":"46", "題名_3":"46", "題名_4":"データ", "題名_5":"7/1/2020"},
					   {"Select":"<input type='checkbox' id='checkbox1' name='checbox1' value=''>", "題名_1":"data", "題名_2":"46", "題名_3":"46", "題名_4":"データ", "題名_5":"7/1/2020"}]
	return render_template('maintenance/index.html', data_2=data_2, menu_1 = True)

@bp.route('/index_a')
@login_required
def index_a():
    return render_template('maintenance/index_a.html') #sample subpage of index

@bp.route('/index_b')
@login_required
def index_b():
	return render_template('maintenance/index_b.html', dropdown=True, menu_2 = True) #sample subpage of index


