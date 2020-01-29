import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/test', methods=['GET'])
def test():
    return 'Hello, World'

if __name__ == '__main__':
    app.run()

