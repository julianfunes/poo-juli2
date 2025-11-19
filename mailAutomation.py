import smtplib
from email.message import EmailMessage

class EmailSender:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
        self.smtp_server = "smtp.gmail.com"
        self.puerto = 587  # STARTTLS

    def enviar_mail(self, destinatario, asunto, mensaje):
        # Crear el mensaje
        email = EmailMessage()
        email["From"] = self.usuario
        email["To"] = destinatario
        email["Subject"] = asunto
        email.set_content(mensaje)

        # Conectarse al servidor y enviar
        try:
            with smtplib.SMTP(self.smtp_server, self.puerto) as server:
                server.starttls()  # Cifra la conexión
                server.login(self.usuario, self.password)
                server.send_message(email)
                print("✅ Correo enviado correctamente.")
        except Exception as e:
            print("⚠️ Error al enviar el correo:", e)
