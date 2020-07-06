import smtplib

# Your Email credentials
with open("credentials","r+") as f:
	content = f.readlines()
	content = [x.strip() for x in content]


# connecting to SMTP and login to your email
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(content[0], content[1])

g = open("rcpt", "r+")
w = g.readlines()

for i in range(len(w)):
	w[i] = w[i].strip()
	name, to, xid = w[i].split('\t')
	email_subject = "Hi "+name+"!"
	email_body = "Dear "+ name+ ",\n\nThis is a test email using my mail merge program. Please acknowledge this email and report any bugs at sample@example.com.\n\nRegards,\nNick"
	message = "From: Nick <nick@example.com>\nTo: "+name+" <"+to+">\nSubject: "+email_subject+"\n\n"+email_body
	session.sendmail(content[0], to, message)
session.quit()
