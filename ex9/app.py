from flask import Flask, redirect, url_for,render_template, request, session
app = Flask(__name__)
app.secret_key = '1234'
users = {'user1': {'name': 'tuv', 'email': 'tuv@gmail.com'},
         'user2': {'name': 'tuvi', 'email': 'tuvi@gmail.com'},
         'user3': {'name': 'tuvali', 'email': 'tuvali@gmail.com'},
         'user4': {'name': 'tuva', 'email': 'tuva@gmail.com'},
         'user5': {'name': 'tuval', 'email': 'tuval@gmail.com'},
         }

@app.route('/')
@app.route('/cv')
def HomePage():
    return render_template('cv.html')

@app.route('/newCV')
def newCV():
    return render_template('newCV.html')

@app.route('/assignment8')
def music():
    print ("im in about ")
    name = 'tuvali'
    fname= 'ron'
    return render_template('assignment8.html',
                           profile={'name':'tuvali','second_name':'ron'},
                           university='BGU',
                           degree=['BSc','MS'],
                           hobbies=('art','music','sql'))
    return render_template('assignment8.html')

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    print(users.values())
    if request.method == 'GET':
        if 'username' in session and session['username']:
            if 'search' in request.args:
                search = request.args['search']
                return render_template('assignment9.html', username=session['username']
                                                         , search=search
                                                         , users=users)
            return render_template('assignment9.html', users=users, username=session['username'])
        return render_template('assignment9.html', users=users)
    if request.method == 'POST':

        #DB
        username = request.form['username']
        Password = request.form['password']
        found = True
        if found:
            session['username'] = username ## DELETE
            session['user_login'] = True  ##SESSION GLOBAL VARIABLE - CAN POST IN ANOTHER PAGES
            return render_template('assignment9.html', username=username, users=users)
        else:
            return render_template('assignment9.html')


@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')

if __name__ == '__main__':
    app.run(debug=True)

