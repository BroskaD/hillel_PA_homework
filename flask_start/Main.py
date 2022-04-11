from flask import Flask, render_template

from Application import Application


flask_app = Flask(__name__)
app = Application()


@flask_app.route('/avr_data')
def get_average_data():

    # title of the tap
    title = 'Average Height & Weight'
    columns, data = app.get_average_height_weight()

    return render_template('result.html', title=title, columns=columns, data=data)


@flask_app.route('/requirements')
def get_requirements():

    # title of the tap
    title = 'Requirements'
    columns, data = app.get_requirements()

    return render_template('result.html', title=title, columns=columns, data=data)


if __name__ == '__main__':
    flask_app.run(debug=True)
