from flask import Blueprint

chatgpt = Blueprint('chatgpt', import_name='openai_api.views.chatgpt', url_prefix='/chatgpt')
example1 = Blueprint('example1', import_name='flask_sample.views.example1', url_prefix='/example1')
example2 = Blueprint('example2', import_name='flask_sample.views.example2', url_prefix='/example2')



all_blueprints = (
    example1,
    example2,
    chatgpt,
)