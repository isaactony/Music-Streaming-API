from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from auth.auth import auth
from routes.albums import albums_bp
from routes.artists import artists_bp
from routes.playlists import playlists_bp
from routes.users import users_bp
from routes.search import search_bp
import config

app = Flask(__name__)
app.config.from_object(config.Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(auth)
app.register_blueprint(albums_bp, url_prefix='/v1/albums')
app.register_blueprint(artists_bp, url_prefix='/v1/artists')
app.register_blueprint(playlists_bp, url_prefix='/v1/playlists')
app.register_blueprint(users_bp, url_prefix='/v1/users')
app.register_blueprint(search_bp, url_prefix='/v1/search')

if __name__ == '__main__':
    app.run(debug=True)
