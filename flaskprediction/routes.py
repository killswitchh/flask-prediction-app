from flask import Flask , render_template , url_for
from flaskprediction import app
from flaskprediction.utils.predict import Predictor
from flaskprediction.forms import CarDetailsForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/titanic")
def titanic():
    return render_template('titanic.html')

@app.route("/car" , methods=['GET' , 'POST'])
def car():
    message = ""
    form = CarDetailsForm()
    if form.validate_on_submit():
        parameter_list = list(map(int,[form.price.data , form.maintenance.data,form.no_of_doors.data, form.capacity.data ,form.size_of_luggage_boot.data,form.safety.data]))
        predictor = Predictor()
        answer = predictor.calculate_probability(parameter_list)
        message = ""
        return render_template('car.html' , title='Car Classifier' , form = form , message= message,answer = answer)
    else:
        message = "Select All Values"
    return render_template('car.html' , title='Car Classifier' , form = form , message= message)
