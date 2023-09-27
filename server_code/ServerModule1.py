import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import bcrypt
import re

@anvil.server.callable

def encryptedPassword(email, password, server):
  regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  
  if re.match(regex, email):
    if app_tables.users.get(email=email) is None:
      passwordHash = password.encode()
      encryptedPassword = bcrypt.hashpw(passwordHash, bcrypt.gensalt())
      app_tables.users.add_row(
        email=email, 
        password_hash=encryptedPassword.decode('utf-8'), 
        server=server,
        confirmed_email=True,
        enabled=True
      )
      return {
        'status': True,
        'message': 'sucess'
      }
    else: 
      return {
        'status': False,
        'message': 'E=mail já cadastrado'
      }
  else:
    return {
      'status': False,
      'message': 'E=mail inválido'
    }
  

  
  
  
