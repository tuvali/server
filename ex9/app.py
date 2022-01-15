from flask import Flask, redirect, url_for,render_template, request, session,jsonify
import requests
from interact_with_DB import interact_db
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

from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


# def getFields(id):
#     person_json = requests.get('https://reqres.in/api/users/%d' % id).json()
#     data = person_json.get('data')
#     return data

@app.route('/assignment11/api', methods=['GET', 'POST'])
def backend():
    if 'id' in request.args:
        id=int(request.args['id'])
        person_json = requests.get('https://reqres.in/api/users/%d' % id).json()
        data = person_json.get('data')
        print(data)
        id = data.get('id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        avatar = data.get('avatar')
        return render_template('/assignment11.html',id=id,first_name=first_name,last_name=last_name,email=email,avatar=avatar)
    return render_template('/assignment11.html')


@app.route('/assignment11/json_users', methods=['GET', 'POST'])
def json_users():
    query = "select * from ex10db.users"
    query_results = interact_db(query=query, query_type='fetch')
    print(query_results)
    return jsonify(query_results)

if __name__ == '__main__':
    app.run(debug=True)

