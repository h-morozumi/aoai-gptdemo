from blueprints import chatgpt

@chatgpt.route('/')
def index():
    return 'example1'


@chatgpt.route('/test')
def test():
    return 'test of example1'