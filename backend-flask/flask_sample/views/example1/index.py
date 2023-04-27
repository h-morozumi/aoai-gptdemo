from blueprints import example1

@example1.route('/')
def index():
    return 'example1'


@example1.route('/test')
def test():
    return 'test of example1'