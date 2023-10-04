from ._anvil_designer import navbarRigthTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import 

class navbarRigth(navbarRigthTemplate):
  def __init__(self, **properties):
    user = anvil.users.get_user()
    self.button_1.text = user['email']
    
    self.init_components(**properties)

