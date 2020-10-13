import os 
from flask import Flask 

def create_app(test_config=None):
    # create and configure app 
    app = Flask(__name__, instance_relative_config=True)
    
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/',endpoint='index.html')



    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

