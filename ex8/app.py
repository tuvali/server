from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)

