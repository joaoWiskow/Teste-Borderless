from flask import Flask
from database import db,migrate

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']="sqlite://dbpunk"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    migrate.init_app(app,db)
    
    from controllers.punk_controller import punkbp
    app.register_blueprint(punkbp)

    with app.app_context():
        from models.punk_model import PunkModel
        db.create_all()
    return app