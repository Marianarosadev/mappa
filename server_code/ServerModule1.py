import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import bcrypt
import re
import secrets
import datetime
import uuid

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
def registerUser(name, email, assignment):
  try:
    app_tables.users.add_row(
      email=email, 
      name=name,
      assignment=assignment,
      confirmed_email=True,
      enabled=True,
      id=str(uuid.uuid4())
    )
    return True
  except Exception as e:
    print('e', e)
    return False

@anvil.server.callable
def sendRecoverEmail(email):
  user = app_tables.users.get(email=email)

  if user['recover_code_send'] is None or user['recover_code_send'].replace(tzinfo=None) > datetime.datetime.now()+datetime.timedelta(minutes=15):
    recoderCode = secrets.token_urlsafe(4)
    user.update(recover_code=recoderCode, recover_code_send=datetime.datetime.now())
  else:
    recoderCode = user['recover_code']

  print('recoverCode', recoderCode)
  
  return {
    'status': True,
    'content': recoderCode
  }

@anvil.server.callable
def resetPasswordService(email, password):
  try:
    passwordHash = password.encode()
    encryptedPassword = bcrypt.hashpw(passwordHash, bcrypt.gensalt())
    user = app_tables.users.get(email=email)
    user.update(password_hash=encryptedPassword.decode('utf-8'), n_password_failures=0)
    return True
  except Exception as e:
    print('e', e)
    return False

@anvil.server.callable
def editUser(id, name, email, assignment):
    try:
      user = app_tables.users.get(id=id)
      user.update(
        email=email, 
        name=name,
        assignment=assignment,
      )
      return True
    except Exception as e:
      print('e', e)
      return False

