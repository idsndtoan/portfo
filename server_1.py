from flask import Flask, render_template, send_from_directory, url_for, request, redirect 
import os 
import csv  

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode ='a',encoding="utf-8") as database:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        file = database.write(f'\n{email},{name},{message}')

def write_to_csv(data):
    with open('database.csv', mode ='a',newline='',encoding="utf-8") as database2:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, name, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data) 
        return redirect('/thanku.html')
    else:
        return "something went wrong. Try again"