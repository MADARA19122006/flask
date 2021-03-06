from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/training/<x>')
def index(x):
    s = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'климатолог']
    if x == 'ol':
        return render_template('ol(Список профессий).html', title='ol', s=s)
    elif x == 'ul':
        return render_template('ul(Список профессий).html', title='ul', s=s)
    else:
        return 'Неверные данные'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
