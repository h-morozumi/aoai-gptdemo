import application
import os

port = int(os.environ['PORT'])
print('Starting app on port %d' % port)
app = application.create_app()
print(app.url_map)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)