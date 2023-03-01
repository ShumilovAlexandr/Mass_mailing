import os

from flask import (render_template, 
                   request, 
                   flash)
from flask_mail import Message
from dotenv import load_dotenv
from celery import Celery


from config import (db, 
                    app, 
                    mail)
from forms import (RegistrationForm, 
                   MailingForm)
from models import User


load_dotenv()


app.config['MAIL_SENDER'] = os.getenv('EMAIL')


client = Celery(app.name,
                broker='redis://localhost/0', 
                backend='redis://localhost/0')
client.conf.update(app.config)


@app.route('/', methods=["POST", "GET"])
def signup():
    form = RegistrationForm()
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        number_phone = request.form.get('number_phone')
        date_of_birth = request.form.get('date_of_birth')
        if form.validate_on_submit():
            user = User(username=username, 
                        email=email,
                        password=password,
                        number_phone=number_phone,
                        date_of_birth=date_of_birth)
            db.session.add(user)
            db.session.commit()
            flash("Account created successfully")
    return render_template('signup.html', title='signup', form=form)


@client.task
def send_mail(data):
    """Function responsible for sending a message."""
    with app.app_context():
        msg = Message('PING!',
                      sender="admin.ping",
                      recipients=[data["email"]])
        msg.body = data["message"]
        mail.send(msg)


@app.route('/index', methods=["GET", "POST"])
def index():
    form = MailingForm()
    users = User.query.order_by(User.date_of_birth).all()
    if request.method == 'POST':
        data = {}
        data['destination'] = request.form.get('destination')
        data['email'] = request.form.get("email")
        data['message'] = request.form.get('message')
        duration = int(request.form.get('duration'))
        duration_unit = request.form.get('duration_unit')
        if duration_unit == 'minutes':
            duration *= 60
        elif duration_unit == 'hours':
            duration *= 3600
        elif duration_unit == 'days':
            duration *= 86400
        elif duration_unit == None:
            duration *= 1
        send_mail.apply_async(args=[data], countdown=duration)
    return render_template('main.html', title="main", form=form, users=users)


if __name__ == '__main__':
   app.run(debug = True)