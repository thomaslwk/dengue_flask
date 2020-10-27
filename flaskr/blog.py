from flask import Blueprint, flash, g, redirect, render_template, request, url_for, send_file
from source.denguegraph import avgrainfalllist, avgdenguelist, nea_data_big_c, nea_data_small_c
from source.matplot_functions import linear_reg_chart
from source.denguemap import make_folium_map, list_compare
from werkzeug.exceptions import abort


bp = Blueprint('blog', __name__)

@bp.route('/', methods=('GET','POST'))
def index():
    return render_template('blog/admin.html',
                           denguecases=avgdenguelist(),
                           rainfalltotal=avgrainfalllist(),
                           linearreg=linear_reg_chart(),
                           listcompare=list_compare(),
                           neadatabig=nea_data_big_c(),
                           neadatasmall=nea_data_small_c(),
                           )
    
@bp.route('/map')
def geomap():
    # return make_folium_map()
    make_folium_map().save('flaskr/templates/map.html')
    return render_template('blog/geomap.html',)

@bp.route('/linear_reg_img')
def get_lr_img():
    filename = 'static/images/LR_graph.png'
    return send_file(filename)

@bp.route('/map_img')
def get_mp_img():
    filename = 'static/images/Map.png'
    
    return send_file(filename)

@bp.route('/rainfall_img')
def get_rain_img():
    filename = 'static/images/Rainfall_graph.png'
    return send_file(filename)