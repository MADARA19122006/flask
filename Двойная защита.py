from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username2 = StringField('Id капитана', validators=[DataRequired()])
    password2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('Двойная защита.html', title='Аварийный доступ', form=form,
                           picture=url_for('static', filename='img/MARS-2-7.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
