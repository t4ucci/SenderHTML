import smtplib
import email.message

print("\nsender gmail.\n")

def menu():
    print("\n[1]Enviar apenas um\n[2]Enviar limitado")

def start_limited():
    
    body = f"""
    
    <font color='green'>
        <p><h5>Attacking.</h5></p>
    </font>
    
    """
    
    msg = email.message.Message()
    print()
    msg['Subject'] = input("Assunto: ")
    msg['From'] = input('Your Email: ') 
    msg["To"] = input("Destinatary: ")
    passw = input("Your Password: ")
    msg.add_header('Content-Type', 'text/html')
    
    msg.set_payload(body)
    
    #envio_de_email
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    server.login(msg['From'], passw)
    server.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print()
    print(f'\033[32m[+]\033[34mE-mail sending...!')

def start_quant():
    
    body2 = f"""
    
    <font color='green'>
        <p><h5>Attacking...</h5></p>
    </font>
   
    """
    
    msg2 = email.message.Message()
    print()
    msg2['Subject'] = input("Assunto: ")
    msg2['From'] = input('Your Email: ') 
    msg2["To"] = input("Destinatary: ")
    quant = int(input("Quantity of numbers: "))
    passw2 = input("Your Password: ")
    msg2.add_header('Content-Type', 'text/html')
    
    msg2.set_payload(body2)
    
    #envio_de_email
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    server.login(msg2['From'], passw2)
    for send in range(1, quant, +1):
        server.sendmail(msg2['From'], msg2['To'], msg2.as_string().encode('utf-8'))
        print()
        print(f'\033[32m[+]\033[34mE-mail sending...! of :: {send}')

while True:
        menu()
        opc = input("\n>>> Your Alternative: ")
        if opc == '1':
            start_limited()
        elif opc == '2':
            start_quant()
        else:
            print("Error Option")



