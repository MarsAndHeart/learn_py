from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'


@app.route('/hello')
def hello_wrold():
    return 'hello world!'


@app.route('/projects/')
def projects():
    return 'the project page'


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_page()


if __name__ == '__main__':
    app.run(debug=True)
