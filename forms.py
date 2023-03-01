from flask_wtf import (FlaskForm)
from wtforms import (StringField,
                     IntegerField, 
                     PasswordField,
                     DateField,
                     TextField)
from wtforms.validators import (DataRequired, 
                                Email, 
                                Length)


class RegistrationForm(FlaskForm):
    """Form for the registration page of new users."""
    username = StringField(label='Username', 
                           validators=[DataRequired()])
    email = StringField(label='Email address', 
                        validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=3, max=9)])
    number_phone = IntegerField(label='Phone number',
                                validators=[DataRequired()])
    date_of_birth = DateField(label='Date_of_Birth', validators=[DataRequired()])
    

class MailingForm(FlaskForm):
    """Form for sending a new letter."""
    destination = StringField('Destination', validators=[DataRequired()])
    email = StringField('Email', 
                        validators=[Email(), DataRequired()])
    message_text = TextField('Message', validators=[DataRequired()])
    duration = IntegerField('Time_of_dispatch', 
                                    validators=[DataRequired()])

