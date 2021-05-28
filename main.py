from flask import Flask, render_template

import models.db_session
import models.user
import forms

my_first_app = Flask(__name__)
my_first_app.config.from_object("config")

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
            return home()
        else:
            return render_template('signup.html', message="Пользователь с таким email уже существует", form=form)
    return render_template("signup.html", form=form)
    return render_template("signup.html")


@my_first_app.route('/home')
def home():
    return render_template("home_page.html")


@my_first_app.route('/statistic')
def about():
    return render_template("statistic.html")


if __name__ == "__main__":
    my_first_app.run(debug=True)
