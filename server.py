from flask import Flask, render_template, url_for, request, redirect
# import json
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

# @app.route("/index.html")
# def my_home2():
#     return render_template('index.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/components.html")
# def components():
#     return render_template('components.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')

@app.route("/<string:page_name>")
def work(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        # with open('database.txt', 'w') as file:
        #     file.write(json.dumps(data))
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong"
    
def write_to_file(data):
    with open('database.txt', 'a') as add_data:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = add_data.write(f"Email: {email}\nSubject: {subject}\nMessage: {message}\n\n\n")

def write_to_csv(data):
    with open('database.csv','a', newline='') as database :
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject,message])