from flask_wtf import FlaskForm
from wtforms import SelectField , SubmitField
from wtforms.validators import InputRequired

PRICE_OPTIONS = [(0,"low") , (1,"med") , (2,"high") , (3,"vhigh")]
MAINTENANCE_COST_OPTIONS = [(0,"low") , (1,"med") , (2,"high") , (3,"vhigh")]
SAFETY_OPTIONS = [(0,"low") ,( 1,"med") , (2,"high")]
NO_OF_DOORS_OPTIONS = [(2,"2") , (3,"3") ,(4,"4") , (5,"5more")]
CAPACITY_OPTIONS = [(2,"2"),(4,"4"),(5,"more")]
SIZE_OF_LUGGAGE_BOOT_OPTIONS = [(0,"small") , (1,"med") ,(2,"big")]


class CarDetailsForm(FlaskForm):
    price = SelectField(label = "Price" , choices = PRICE_OPTIONS , validators = [InputRequired()])
    maintenance = SelectField(label = "Maintenance Cost" , choices = MAINTENANCE_COST_OPTIONS , validators = [InputRequired()])
    capacity = SelectField(label = "Capacity" , choices = CAPACITY_OPTIONS , validators = [InputRequired()])
    size_of_luggage_boot = SelectField(label = "Luggage Boot Size" , choices = SIZE_OF_LUGGAGE_BOOT_OPTIONS , validators = [InputRequired()])
    no_of_doors = SelectField(label = "Luggage Boot Size" , choices = NO_OF_DOORS_OPTIONS , validators = [InputRequired()])
    safety = SelectField(label = "Safety" , choices = SAFETY_OPTIONS , validators = [InputRequired()])
    submit = SubmitField("Predict")