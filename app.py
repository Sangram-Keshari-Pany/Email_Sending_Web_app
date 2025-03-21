from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Required for flash messages

# Email Configuration
SMTP_SERVER = 'smtp.gmail.com'  # Change for your email provider
SMTP_PORT = 587
EMAIL_ADDRESS = 'sangrampany3040@gmail.com'  # Replace with your email
EMAIL_PASSWORD = 'kkgk ykgb xvoz jnsq'  # Replace with your password

@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        
        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = recipient
            msg.attach(MIMEText(subject, 'plain'))
            
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, "hii")
            server.quit()
            
            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        
        return redirect('/') 
    
    return render_template('Form.html')

if __name__ == '__main__':
    app.run(debug=True)
