from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import glob

from main import extract_details


app = Flask(__name__)
app.secret_key = "detectform"

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#MAIN APP MAKING
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST' and 'documents' in request.files:
        for f in request.files.getlist('documents'):
            file = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file))

    f = []
    f1 = []
    f2 = []
    f3 = []
    f4 = []
    f5 = []
    f6 = []
    f7 = []
    f8 = []
    f9 = []
    f10 = []
    f11 = []
    f12 = []
    f13 = []


    global org
    global cat
    global fname
    global mname
    global lname
    global dob
    global ssn
    global email
    global tele
    global street
    global city
    global state
    global sex
    global accno



    for file_name in glob.iglob("uploads/**/*.pdf", recursive=True):
        org, cat, fname, mname, lname, dob, ssn, email, tele, street, city, state, sex, accno = extract_details(file_name)

        f.append(org)
        f1.append(cat)
        f2.append(fname)
        f3.append(mname)
        f4.append(lname)
        f5.append(dob)
        f6.append(ssn)
        f7.append(email)
        f8.append(tele)
        f9.append(street)
        f10.append(city)
        f11.append(state)
        f12.append(sex)
        f13.append(accno)

    os.system("cls")
    print(f)
    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)
    print(f8)
    print(f9)
    print(f10)
    print(f11)
    print(f12)
    print(f13)
    # EMPTY UPLOAD FOLDER
    BASE_DIR = os.getcwd()
    dir = os.path.join(BASE_DIR, "uploads")

    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(dir, file)
            os.remove(path)
    return render_template('predict.html', org=org, cat=cat, fname=fname, mname=mname, lname=lname, dob=dob, ssn=ssn, email=email, tele=tele, street=street,city=city, state=state, sex=sex, accno=accno)


if __name__ == "__main__":
    app.run(debug=True)