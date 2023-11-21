import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
"""
Nombre: Johan Emmanuel Garay Garza
Matricula: 2001776
""""
# correo electronico
correo_emisor = '...'
contrasena = '...'

# Destinatario
correo_destinatario = 'gerardo.bernal@uanl.edu.mx'

# Ruta de la imagen
ruta_imagen = 'C:/Users/jgara/OneDrive/Escritorio/FACULTAD/CUARTO SEMESTRE/LABORATORIO/012- ENVIO DE CORREOS/fcfm_cool.png'

# mensaje
mensaje = MIMEMultipart()
mensaje['From'] = correo_emisor
mensaje['To'] = correo_destinatario
mensaje['Subject'] = 'Prueba de envio 2001776'

# Contenido 
contenido_html = """
<html>
<body>
<h1>Practica 12</h1>
<p>Ejercicio de la practica 12 para envio de correos</p>
<p>Alumno Johan Emmanuel Garay Garza</p>
<p>Matricula 2001776</p>
</body>
</html>
"""

# Adjuntar el contenido 
mensaje.attach(MIMEText(contenido_html, 'html'))

# Adjuntar la imagen
with open(ruta_imagen, 'rb') as archivo_imagen:
    imagen = MIMEImage(archivo_imagen.read(), name='fcfm_cool.png')
    mensaje.attach(imagen)

# Iniciar una conexion SMTP
try:
    servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_smtp.starttls()
    servidor_smtp.login(correo_emisor, contrasena)
    servidor_smtp.sendmail(correo_emisor, correo_destinatario, mensaje.as_string())
    servidor_smtp.quit()
    print('Correo enviado con exito')
except Exception as e:
    print(f'Error al enviar el correo: {str(e)}')
