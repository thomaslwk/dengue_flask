from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from source.denguegraph import test
from source.denguemap import make_folium_map
from werkzeug.exceptions import abort


bp = Blueprint('blog', __name__)

@bp.route('/', methods=('GET','POST'))
def index():
    return render_template('blog/admin.html')
    

@bp.route('/map')
def geomap():
    # return make_folium_map()
    make_folium_map().save('flaskr/templates/map.html')
    return render_template('blog/geomap.html')
    
