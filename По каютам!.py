from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def login():
    s = ['Mark', 'Scott', 'Wendy', 'Kolyan4ik']
    return render_template('По каютам!.html', s=s)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
