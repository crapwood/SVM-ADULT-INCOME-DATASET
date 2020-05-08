import os
import smtplib


def sendemail(message):
    from_addr = os.environ.get('USER_EMAIL')
    subject = 'Finished The Program'
    # login = os.environ.get('USER_EMAIL')
    password = os.environ.get('USER_EMAIL_PASS')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        msg = f"Subject: {subject}\n\n{message}"
        smtp.login(from_addr, password)

        smtp.sendmail(from_addr, 'johnjamesbenitez06@gmail.com', msg)
        smtp.quit()
