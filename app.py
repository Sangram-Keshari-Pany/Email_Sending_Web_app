from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')  

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True  
app.config['MAIL_USE_SSL'] = False  
app.config['MAIL_USERNAME'] = 'sangrampany546@gmail.com'  
app.config['MAIL_PASSWORD'] = 'ixaw dkkp yflx lpyb'  
app.config['MAIL_DEFAULT_SENDER'] = 'sangrampany546@gmail.com'  

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        recipient_email = request.form['recipient']
        subject = request.form['subject']
        html_content = render_template("index.html", subject=subject)
        file_path = 'sangram_keshari_pany.pdf'

        if not os.path.exists(file_path):
            flash(f'File {file_path} does not exist!', 'danger')
            return redirect('/')
        
        try:
            with open(file_path, 'rb') as fp:
                msg = Message(subject=subject,recipients=[recipient_email],html=html_content)
                msg.attach(filename='sangram_keshari_pany.pdf',  content_type='application/pdf',  data=fp.read() )
                mail.send(msg)
                flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Error sending email: {str(e)}', 'danger')
        return redirect('/')
    return render_template('Form.html')

if __name__ == '__main__':
    app.run(debug=True)
