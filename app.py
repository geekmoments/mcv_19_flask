from flask import Flask,request,make_response,redirect,render_template

app = Flask(__name__)

todos = ['Comprar 1', 'Llevar 2', 'Hacer 3']

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/get_ip'))
    response.set_cookie('user_ip',user_ip)

    return response


@app.route('/get_ip')
def get_ip():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':todos,
    }
    return render_template('hello.html',**context)


if __name__ == '__main__':
    app.run()
