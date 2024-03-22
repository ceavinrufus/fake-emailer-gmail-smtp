import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
import base64
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + "!#$%^&*"
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

smtpserver = 'local.domain.name'
to = ['18221062@std.stei.itb.ac.id', '18221162@std.stei.itb.ac.id']
# to = ['yudis@staff.stei.itb.ac.id', '18221062@std.stei.itb.ac.id', '18221162@std.stei.itb.ac.id']
fromAddr = '18221162@std.stei.itb.ac.id'
# fromAddr = 'yudis@staff.stei.itb.ac.id'
subject = "Score Match! Invitation"

# membuat email
emailMsg = MIMEMultipart()
emailMsg['From'] = f"Yudistira Asnar <{fromAddr}>"
emailMsg['To'] = ', '.join(to)
emailMsg['Subject'] = subject
emailMsg['Message-ID'] = f"<{generate_random_string(32)}@gmail.com>"
body = """Selamat pagi mahasiswa sekalian,

Berhubungan masa UTS akan segera dimulai, saya mengundang mahasiswa sekalian untuk melawan saya dalam permainan Score Match! Anda boleh berkelompok dengan teman kelompok yang telah dibentuk dan lakukan dengan mencari kelemahan dari sistem security formasi tim saya (lihat foto formasi.jpg).

Yang kalah harus mempraktikkan tepuk-holland (lihat tepuk-holland.mp4) dan kirimkan ke email saya.

Terima kasih."""
emailMsg.attach(MIMEText(body, 'plain'))

# definisi attachment function
def Add_Attachment(msg,Attachment):
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open("./files/"+Attachment, "rb").read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename={}'.format(Attachment))
	msg.attach(part)
	return msg

# attach file
Add_Attachment(emailMsg, 'tepuk-holland.mp4')
Add_Attachment(emailMsg, 'formasi.jpg')
Add_Attachment(emailMsg, 'undangan.txt')

# send email dengan MX atau smtp dari gmail.com
server = smtplib.SMTP('gmail-smtp-in.l.google.com', 25)
server.sendmail(fromAddr,to,emailMsg.as_string())
server.quit()