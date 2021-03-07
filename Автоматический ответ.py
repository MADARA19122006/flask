from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def index():
    s = {'title': 'Анкета', 'surname': 'Иванов', 'name': 'Иван', 'education': 'высшее', 'profession': 'инженер', 'sex': 'мужской', 'motivation': 'исследование чего-то нового', 'ready': 'да'}
    return render_template('auto_answer.html', title=s['title'], s=s)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
