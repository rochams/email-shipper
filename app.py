"""
Se você tomar um erro de autenticação, entre no link https://www.google.com/settings/security/lesssecureapps e habilite o servidor de e-mail para
ser acessado por aplicações de 'terceiros'.
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
msg['subject'] = 'Assunto do e-mail'

# especificando o corpo do email e o formato
corpo = MIMEText(content, 'html')   
msg.attach(corpo)

with open('imagem.png', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as prot:
    try:
        # porta e endereço variam de acordo com o provedor.
        prot.ehlo()
        prot.starttls()
        prot.login(my_email, my_pass)
        prot.send_message(msg)
        print('E-mail enviado com sucesso!')
    except Exception as erro:
        print('E-mail não enviado')
        print('Erro: ', erro)




