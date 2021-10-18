
try:
    import smtplib
    import termcolor
    from termcolor import cprint
    import sys
    from time import sleep
except:
    import sys
    system("pip3 install smtplib")
    system("pip3 install termcolor")
    system("pip3 install time")
    system("pip3 install sys")
    system("pip3 install python3")

try:
    # connect to email server
    SERVER = smtplib.SMTP("smtp.gmail.com", 587)
    SERVER.starttls()
    
    # login into gmail account
    EMAIL = "hamidbigga2020@gmail.com"
    PASSWORD = "hamid2020"
    
    def login(email, passw):
        try:
            SERVER.login(email, passw)
            cprint("Login Successful . . .", "green")
            print()
        except AttributeError:
            cprint("Login Failed . . .", "red")
            exit()
            
    
    # send email        
    def send_mail():
        login(EMAIL, PASSWORD)
        msg = input(termcolor.colored("Compose Email: ", "yellow"))
        reciever = input(termcolor.colored("Enter Reciever Email: ", "yellow"))
        #subject = input(termcolor.colored("Enter Your Subject: ", "yellow"))
        try:
            sending= True
            while sending:
                SERVER.sendmail(EMAIL, reciever, msg)
                sleep(0.3)
                print()
                cprint(f"Message  Has Been Sent Successfully To {reciever} . . . . .", "green")
        except:
            cprint("Message Was Not Sent . . . . . .", "red")
            exit()
            
            
    send_mail()
except:
    cprint("Couldn't Connect To Gmail Server . . . . .", "red")