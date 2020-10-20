from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    return render_template('blog/admin.html')

# bp.route('/analytics')
# def analytics():
#     return render_template('blog/admin.html')

@bp.route('/map')
def geomap():
    return render_template('blog/geomap.html')

def handle_404(e):
    return render_template('blog/admin.html')