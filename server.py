# from operator import index
import os
import csv

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


# print(__name__)

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['emailll']
#         subject = data['subjecttt']
#         message = data['messageee']
#         file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['emailll']
        subject = data['subjecttt']
        message = data['messageee']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting =csv.QUOTE_MINIMAL)
        #csv_writer.writerows('')
        csv_writer.writerow([email, subject, message])



@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again !!!'

# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')
#
# # @app.route('/<username>/<int:post_id>')
# # def hello_world(username=None, post_id=None):
# #     return render_template('index.html', name=username, post_id=post_id)
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
#
# @app.route('/blog')
# def blog():
#     return 'this are my thoughts on blogs'
#
# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'this is my dog'

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path,'static'), 'favicon.ico', mimetype='static/favicon.ico')
