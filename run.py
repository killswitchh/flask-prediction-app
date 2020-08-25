from flask import Flask , render_template , url_for
from forms import CarDetailsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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
        return render_template('result.html')
    else:
        message = "Select All Values"
    return render_template('car.html' , title='Car Classifier' , form = form , message= message)

if __name__ == "__main__":
    app.run(debug=True)

