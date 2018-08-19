'''
___init__.py
main config  file
'''

from flask_api import FlaskAPI
from app.config import CONFIG
from app.views.answer import answer_blueprint
from app.views.question import question_blueprint


def create_app(config):
    ''' function that receives configaration and creates the app'''
    app = FlaskAPI(__name__)
    app.config.from_object(CONFIG[config])
    app.url_map.strict_slashes = False

    app.register_blueprint(answer_blueprint, url_prefix='/api/v1')
    app.register_blueprint(question_blueprint, url_prefix='/api/v1')
    return app
