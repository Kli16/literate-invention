from flask import Flask, render_template, request, session, redirect, url_for

cw929 = Flask(__name__)
cw929.secret_key = 'random'

@cw929.route('/')
def root():
    if 'name' in session:
        #print "test"
        return render_template("response.html", name = session['name'], method = request.method)
    else:
        return render_template("form.html")

name = 'default'
password = 'password'

@cw929.route('/response', methods=['POST','GET'])
def response():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
    else:
        name = request.args['username']
        password = request.args['password']
    if (name == 'kevincyn' and password == 'secretpassword'):
        session['name'] = name
        return render_template("response.html", name = session['name'], method = request.method, password = password)
    else:
        if (name != 'kevincyn'):
            problem = 'username'
        else:
            problem = 'password'
        return render_template("loginfailed.html", problem = problem)

@cw929.route('/logout', methods=['POST','GET'])
def logout():
    if 'name' in session:
        session.pop('name')
        #print "testingg"
    return redirect(url_for('root'))

if __name__ == '__main__':
  cw929.debug = True
  cw929.run()
