import os

from app import create_app

if __name__ == '__main__':
    env_name = os.getenv('FLASK_CONFIG') or 'default'
    app = create_app(env_name)
    app.run()