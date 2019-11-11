# src/app.py
import os
import markdown

from flask import Flask

import config
from src.models import db
from src.views.JobView import job_api as job_blueprint

def create_app(env_name):
    """
    Create app
    """
    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(config.app_config[env_name])

    db.init_app(app)

    app.register_blueprint(job_blueprint, url_prefix='/modulelog/')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
            content = markdown_file.read()
            return markdown.markdown(content)

    return app


# app = create_app.(app_config[env_name])
