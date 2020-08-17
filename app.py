from flask import ( Flask, g, redirect, render_template, request, session, url_for)


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    def __repr__(self):
        return f'<User: {self.username}>'
users = []
users.append(User(id=1, username='caleb', password='lexman'))
users.append(User(id=2, username='smart', password='smartman'))
#print(users[1].password)  //to show the password of the user at id 1

app = Flask(__name__)
app.secret_key = 'onlyishouldknow'

@app.before_request
def before_request():
    if 'user_id' in session:
        user = [x for x in users if x.id == session]['user_id'][0]
        g.user =user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
            # most sites soes this in that if u are already logged in it will remove your session and try to create a new session
        session.pop('user_id', None)
        username = request.form['userName']
        password = request.form['passWord']

            # it checks if what the user entered is amongst the database list of names
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            # for a session we can only pass in a complete id that is in figures not anything else baecause it is a cookie
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        # if the user and password is incorrect we will redirect them back to the login page to retry
        return redirect(url_for('index'))

    return render_template('index.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run()
