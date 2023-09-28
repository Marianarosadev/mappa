import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import bcrypt
import re

@anvil.server.callable
def validEmailInput(email):
  regexMail = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  regexEmpty =  r'^\s*$'

  if re.match(regexEmpty, email):
    return {
      'status': False,
      'message': 'O campo e-mail é obrigatório',
      'type': 'email'
    }
  elif not re.match(regexMail, email): 
    return {
      'status': False,
      'message': 'E-mail inválido',
      'type': 'email'
    }
  elif app_tables.users.get(email=email):
    return {
      'status': False,
      'message': 'E-mail já cadastrado',
      'type': 'email'
    }
  else:
    return {
      'status': True,
      'message': '',
      'type': 'email'
    }

@anvil.server.callable
def registerUser(email, password, server):
  try:
    passwordHash = password.encode()
    encryptedPassword = bcrypt.hashpw(passwordHash, bcrypt.gensalt())
    app_tables.users.add_row(
      email=email, 
      password_hash=encryptedPassword.decode('utf-8'), 
      server=server,
      confirmed_email=True,
      enabled=True
    )
  except Exception as e:
    print('e', e)