from flask import Flask, render_template, redirect

import models.db_session
import models.user
import forms
import models.music
import models.all_music

from flask_login import LoginManager, login_required, login_user, logout_user

my_first_app = Flask(__name__)
my_first_app.config.from_object("config")
login_manager = LoginManager()
login_manager.init_app(my_first_app)
login_manager.login_view = 'login'

models.db_session.global_init("my_database.db")


@my_first_app.route('/', methods=['GET', 'POST'])
def signup():
    form = forms.RegistrationForm()
    db_session = models.db_session.create_session()
    if form.validate_on_submit():
        if db_session.query(models.user.User).filter_by(email=form.email.data).count() < 1:
            user = models.user.User(
                email=form.email.data,
                password=form.password.data
            )

            db_session.add(user)
            db_session.commit()
            return login()
        else:
            return render_template('signup.html', message="Пользователь с таким email уже существует", form=form)
    return render_template("signup.html", form=form)
    return render_template("signup.html")

@my_first_app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.AuthorizationForm()
    if form.validate_on_submit():
        db_session = models.db_session.create_session()
        user = db_session.query(models.user.User).filter(models.user.User.email == form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return home()
        else:
            return render_template('signin.html', message="Неправильный логин или пароль", form=form)
    return render_template("signin.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = models.db_session.create_session()
    return db_sess.query(models.user.User).get(user_id)


@my_first_app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@my_first_app.route('/home')
def home():
    db_sess = models.db_session.create_session()
    music = db_sess.query(models.all_music.All_music)
    return render_template("home_page.html", all_music = music)


@my_first_app.route('/statistic')
def about():
    db_sess = models.db_session.create_session()
    music = db_sess.query(models.music.Music)
    user = db_sess.query(models.user.User).filter(models.user.User.id == 1).first()
    return render_template("statistic.html", user = user, music = music)


if __name__ == "__main__":
    my_first_app.run(debug=True)
