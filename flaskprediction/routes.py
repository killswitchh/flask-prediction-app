import secrets

from flask import Flask , render_template , url_for , send_from_directory  
from flaskprediction import app
from flaskprediction.utils.predict import Predictor
from flaskprediction.forms import CarDetailsForm , TitanicDetailsForm , BostonDetailsForm , HeightDetailsForm, CatImageForm
from PIL import Image

import os

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/classifier", methods=['GET' , 'POST'])
def classifier():
    return render_template('classification.html')

@app.route("/regressor", methods=['GET' , 'POST'])
def regressor():
    return render_template('regression.html')


@app.route("/classifier/titanic", methods=['GET' , 'POST'])
def titanic():
    message = ""
    form = TitanicDetailsForm()
    if form.validate_on_submit():
        parameter_list = [form.p_id.data , form.p_class.data, form.sex.data ,form.age.data,form.sibsp.data,form.parch.data,form.fare.data,form.embarked.data]
        predictor = Predictor()
        print(parameter_list)
        answer = predictor.calculate_probability_titanic(parameter_list)
        message = ""
        return render_template('titanic.html' , title='Titanic Classifier' , form = form , message= message,answer = answer)
    else:
        message = "Enter Passenger Details"
    return render_template('titanic.html' , title='Titanic Classifier' , form = form , message= message)

@app.route("/classifier/car" , methods=['GET' , 'POST'])
def car():
    message = ""
    form = CarDetailsForm()
    if form.validate_on_submit():
        parameter_list = list(map(int,[form.price.data , form.maintenance.data,form.no_of_doors.data, form.capacity.data ,form.size_of_luggage_boot.data,form.safety.data]))
        predictor = Predictor()
        answer = predictor.calculate_probability_car(parameter_list)
        message = ""
        return render_template('car.html' , title='Car Classifier' , form = form , message= message,answer = answer)
    else:
        message = "Select All Values"
    return render_template('car.html' , title='Car Classifier' , form = form , message= message)



@app.route("/regressor/boston" , methods=['GET' , 'POST'])
def boston():
    message = ""
    form = BostonDetailsForm()
    if form.validate_on_submit():
        parameter_list = [form.crim.data , form.zn.data, form.chas.data ,form.nox.data,form.rm.data,form.age.data,form.dis.data,form.ptratio.data , form.black.data , form.lstat.data]
        predictor = Predictor()
        answer = predictor.calculate_price_boston(parameter_list)
        message = ""
        return render_template('boston.html' , title='Boston Regressor' , form = form , message= message,answer = answer)
    else:
        message = "Select All Values"
    return render_template('boston.html' , title='boston Regressor' , form = form , message= message)


@app.route("/regressor/height" , methods=['GET' , 'POST'])
def height():
    message = ""
    form = HeightDetailsForm()
    if form.validate_on_submit():
        parameter_list = [form.sex.data , form.height.data]
        predictor = Predictor()
        answer = predictor.calculate_weight(parameter_list)
        message = ""
        return render_template('height.html' , title='Weight Prediction' , form = form , message= message,answer = answer)
    else:
        message = "Select All Values"
    return render_template('height.html' , title='Weight Prediction' , form = form , message= message)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)
    output_size = (64, 64)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_path

@app.route("/classifier/cat" , methods=['GET' , 'POST'])
def cat():
    message = ""
    
    form = CatImageForm()
    if form.validate_on_submit():
        picture_file = form.cat_picture.data
        
        image_file = save_picture(picture_file)
        predictor = Predictor()
        answer = predictor.find_cat(image_file)
        message = ""
        return render_template('cat.html' , title='Cat Prediction' , form = form , message= message,answer = answer)
    else:
        message = "Upload A Picture"
    return render_template('cat.html' , title='Cat Prediction' , form = form , message= message)