import smtplib
s = smtplib.SMTP('smtp.dhanushdhanu5427@gmail.com', 587)
s.starttls()
s.login("dhanushdhanu5427@gmail.com", "*********8")
message = "hi wat r u doing"
s.sendmail("dhanushdhanu5427@gmail.com", "dhanushdhanu5427@gmail.com", message)
s.quit()
