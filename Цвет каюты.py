from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/table/<sex>/<age>')
def login(sex, age):
    if sex == 'female':
        if int(age) >= 21:
            return render_template('Цвет каюты.html',
                                   wall=url_for('static', filename='img/wall.png'),
                                   picture=url_for('static', filename='img/adult.png'))
        else:
            return render_template('Цвет каюты.html',
                                   wall=url_for('static', filename='img/wall.png'),
                                   picture=url_for('static', filename='img/child.png'))
    else:
        if int(age) >= 21:
            return render_template('Цвет каюты.html',
                                   wall=url_for('static', filename='img/wall2.png'),
                                   picture=url_for('static', filename='img/adult.png'))
        else:
            return render_template('Цвет каюты.html',
                                   wall=url_for('static', filename='img/wall2.png'),
                                   picture=url_for('static', filename='img/child.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
