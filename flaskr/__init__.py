import os 
from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure app 
    app = Flask(__name__, instance_relative_config=True)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/',endpoint='index.html')
    app.register_error_handler(404, handle_404)
    
    return app

def handle_404(e):
    return render_template('blog/admin.html'),404

