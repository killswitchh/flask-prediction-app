from flask import Flask , render_template , url_for , send_from_directory  
from flaskprediction import app
from flaskprediction.utils.predict import Predictor
from flaskprediction.forms import CarDetailsForm , TitanicDetailsForm , BostonDetailsForm

import os

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/titanic", methods=['GET' , 'POST'])
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

@app.route("/car" , methods=['GET' , 'POST'])
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



@app.route("/boston" , methods=['GET' , 'POST'])
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