import smtplib

# Erstellen Sie ein SMTP-Objekt für den Server
server = smtplib.SMTP('localhost')

# Senden Sie eine einfache E-Mail
from_addr = 'absender@example.com'
to_addr = 'empfaenger@example.com'
message = 'Subject: Testnachricht\n\nDies ist eine Testnachricht.'
server.sendmail(from_addr, to_addr, message)

# Schließen Sie die Verbindung zum Server
server.quit()