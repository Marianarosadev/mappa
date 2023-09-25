import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import bcrypt

@anvil.server.callable

def encryptedPassword(email, password, server):
  passwordHash = password.encode()
  encryptedPassword = bcrypt.hashpw(passwordHash, bcrypt.gensalt())
  app_tables.users.add_row(email=email, password_hash=encryptedPassword.decode('utf-8'), server=server)
