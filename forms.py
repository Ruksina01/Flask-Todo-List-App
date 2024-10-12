from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, EqualTo
from datetime import datetime

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    content = StringField('Task', validators=[DataRequired()])  # Task description
    priority = SelectField(
        'Priority', 
        choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], 
        validators=[DataRequired()]
    )  # Priority dropdown with options
    due_date = DateField(  # Changed to DateField for date-only input
        'Due Date', 
        default=datetime.today().date(),  # Set default to today's date
        format='%Y-%m-%d',  # Adjusted to match date format
        validators=[DataRequired()]
    )  # Field for due date input
    submit = SubmitField('Add Task')  # Button to submit the task form
