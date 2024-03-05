from flask import Flask

from app.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    migrate.init_app(app, db)

    # Importe os Blueprints dentro da função create_app
    # para evitar importações circulares
    from app.domains.hello.controllers import hello_bp
    from app.domains.posts.controllers import post_bp
    from app.domains.user.controllers import user_bp

    app.register_blueprint(hello_bp, url_prefix='/hello')
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(post_bp, url_prefix='/posts')

    return app
