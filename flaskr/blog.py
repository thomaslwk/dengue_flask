from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from source.denguegraph import test
from source.denguemap import make_folium_map
from werkzeug.exceptions import abort


bp = Blueprint('blog', __name__)

@bp.route('/', methods=('GET','POST'))
def index():
   
    if request.method == 'GET': 
        return render_template('blog/admin.html')
    elif request.method == 'POST':
        testcall = test(request.form['test'])
        return render_template('blog/admin.html')

@bp.route('/map')
def geomap():
    # start_coords = (46.9540700, 142.7360300)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    return make_folium_map()
    # return render_template('blog/geomap.html'), folium_map._repr_html_()
    # make_folium_map()
    # return render_template('blog/geomap.html')

# @bp.route('/', methods=('GET', 'POST'))
# def homepage():
#     if request.method == 'GET':
#         return render_template('homepage.html', stations=station_list)

#     elif request.method == 'POST':
#         gender = sanitize_gender(request.form['gender'])
#         start_station = request.form['start_station']
#         end_station = request.form['end_station']
#         hour = get_hour_from_time_string(request.form['time'])
#         trip_data = find_intersecting_routes_and_save_map_html(gender, hour, start_station, end_station)
#         return redirect(url_for('index.intersect',
#                                 gender=trip_data['gender'],
#                                 years=trip_data['age'],
#                                 date=trip_data['date'],
#                                 location=trip_data['location']))

# @bp.route('/intersect', methods=('GET', 'POST'))
# def intersect():
#     if request.method == 'GET':
#         gender = request.args['gender']
#         years = request.args['years']
#         date = request.args['date']
#         location = request.args['location']
#         return render_template('intersecting_routes.html',
#                                gender=gender,
#                                years=years,
#                                date=date,
#                                location=location)
#     elif request.method == 'POST':
#         return redirect('/')