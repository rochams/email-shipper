"""
Se você tomar um erro de autenticação, entre no link https://www.google.com/settings/security/lesssecureapps e permita que o seervidor de e-mail
seja acessado por aplicações 'menos seguras'.
"""


from string import Template
from datetime import datetime
# importando bibliotecas que trabalham com os campos do e-mail, texto e imagens, respectivamente.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

# se você subir essa aplicação pro seu repositório, crie um módulo para importar as credenciais de e-mail.
my_email = 'seu_email@email.com'
my_pass = 'sua_senha'

with open('template.html', 'r') as html:
    template = Template(html.read())
    date = datetime.now().strftime('%d/%m/%Y')
    # pode-se usar substitute_safe em casos de haver diferença de quantidade entre as variáveis do template e do código python
    content = template.substitute(nome='usuário', date=date)

# preenchendo os campos do Multipart
msg = MIMEMultipart()
msg['from'] = 'remetente'
msg['to'] = 'destinatario@email.com'
msg['subject'] = 'E-mail teste Python'

# especificando o corpo do email e o formato
corpo = MIMEText(content, 'html')   
# anexando o corpo do texto ao e-mail
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as prot:
    # as portas e endereço variam de acordo com o provedor, consulte o desejado.
    prot.ehlo()
    prot.starttls()
    prot.login(my_email, my_pass)
    prot.send_message(msg)


    print('E-mail enviado com sucesso!')




