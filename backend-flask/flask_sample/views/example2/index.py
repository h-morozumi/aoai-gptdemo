from blueprints import example2

@example2.route('/')
def index():
    return 'example2'


@example2.route('/hoge')
def test():
    return 'hoge of example2'