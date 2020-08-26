from flask_wtf import FlaskForm
from wtforms import SelectField , SubmitField , StringField , DecimalField , IntegerField
from wtforms.validators import InputRequired , DataRequired , NumberRange

#CAR
PRICE = [(0,"low") , (1,"med") , (2,"high") , (3,"vhigh")]
MAINTENANCE_COST = [(0,"low") , (1,"med") , (2,"high") , (3,"vhigh")]
SAFETY = [(0,"low") ,( 1,"med") , (2,"high")]
NO_OF_DOORS = [(2,"2") , (3,"3") ,(4,"4") , (5,"5 or more")]
CAPACITY = [(2,"2"),(4,"4"),(5,"more")]
SIZE_OF_LUGGAGE_BOOT = [(0,"small") , (1,"med") ,(2,"big")]

#TITANIC
PASSENGER_CLASS = [(1,"Class 1"),(2,"Class 2"),(3,"Class 3")]
PASSENGER_SEX = [("male","Male"),("female" , "Female")]
EMBARKED_PORT = [("C" , "Cherbourg") , ("Q","Queenstown") , ("S","Southampton")]

class CarDetailsForm(FlaskForm):
    price = SelectField(label = "Price" , choices = PRICE , validators = [InputRequired()])
    maintenance = SelectField(label = "Maintenance Cost" , choices = MAINTENANCE_COST , validators = [InputRequired()])
    capacity = SelectField(label = "Capacity" , choices = CAPACITY , validators = [InputRequired()])
    size_of_luggage_boot = SelectField(label = "Luggage Boot Size" , choices = SIZE_OF_LUGGAGE_BOOT , validators = [InputRequired()])
    no_of_doors = SelectField(label = "Luggage Boot Size" , choices = NO_OF_DOORS , validators = [InputRequired()])
    safety = SelectField(label = "Safety" , choices = SAFETY , validators = [InputRequired()])
    submit = SubmitField("Predict")

class TitanicDetailsForm(FlaskForm):
    p_id = IntegerField(label="Passenger ID", validators=[InputRequired()])
    p_class = SelectField(label="Passenger class", choices=PASSENGER_CLASS , validators = [InputRequired()])
    name = StringField(label="Passenger Name" , validators=[InputRequired()])
    sex = SelectField(label = "Passenger Sex" , choices=PASSENGER_SEX, validators = [InputRequired()])
    age = IntegerField(label = "Passenger Age" , validators =[NumberRange(min=1, max=100) , InputRequired()])
    sibsp = IntegerField(label = "Number of Siblings / Spouse(s)" , validators =[NumberRange(min=0, max=10) , InputRequired()])
    parch = IntegerField(label = "Number of Parents / Children" , validators =[NumberRange(min=0, max=10) , InputRequired()])
    fare = DecimalField(label="Ticket Fare", validators = [NumberRange(min=0, max=1000) , InputRequired()])
    embarked = SelectField(label="Embarked from", choices=EMBARKED_PORT , validators = [InputRequired()])
    submit = SubmitField("Predict")