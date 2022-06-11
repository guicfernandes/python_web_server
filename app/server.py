from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def my_home():
    return render_template('./index.html')
    # return "<p>Hello, World!</p>"


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data.get('email', None)
        subject = data.get('subject', None)
        message = data.get('message', None)
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as csv_database:
        email = data.get('email', None)
        subject = data.get('subject', None)
        message = data.get('message', None)
        csv_writer = csv.writer(
            csv_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save on the database'
    else:
        return 'something went wrong. Try again!'
