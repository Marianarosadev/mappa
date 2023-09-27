import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import bcrypt
import re

@anvil.server.callable

def encryptedPassword(email, password, server):
  regexMail = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  regexPassword =  r'^\s*$'
  
  if re.match(regexMail, email):
    if app_tables.users.get(email=email) is None :
      
      if re.match(regexPassword, password):
        return {
          'status': False,
          'message': 'Campo obrigatório',
          'type': 'password'
        }

      if server is None:
        return {
          'status': False,
          'message': 'Selecione uma opção',
          'type': 'server'
        }
        
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
        'message': 'sucess',
        'type': 'sucess'
      }
    
    else: 
      return {
        'status': False,
        'message': 'E=mail já cadastrado',
        'type': 'email'
      }
  else:
    return {
      'status': False,
      'message': 'E=mail inválido',
      'type': 'email'
    }
  

  
  
  
