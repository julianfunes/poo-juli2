from mailAutomation import EmailSender

# ⚙️ Datos del remitente
usuario = "pepo008400@gmail.com"
contraseña = "ygaz tqdj sbed vmsi"  # Contraseña de aplicación

# ✉️ Crear objeto y enviar
correo = EmailSender(usuario, contraseña)
correo.enviar_mail(
    destinatario="profenachosanchez@gmail.com",
    asunto="Prueba desde Python en ProA La Falda",
    mensaje="Hola! Este es un mail de prueba enviado desde un programa en Python 🐍 dia 3/11"
)
