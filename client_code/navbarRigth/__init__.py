from ._anvil_designer import navbarRigthTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import popover
from ..login.resetPassword import resetPassword

class navbarRigth(navbarRigthTemplate):
  def __init__(self, **properties):
    user = anvil.users.get_user()
    self.button_1.text = user['email']
    column = ColumnPanel()
    resetPasswordButton = Button(align='center', text='Redefinir Senha')
    
    self.button_1.popover 
    
    self.init_components(**properties)

  def openResetPassword_click(self, **event_args):
    alert('reset')