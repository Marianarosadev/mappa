from ._anvil_designer import registerTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class register(registerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def registerButton_click(self, **event_args):
    emailValid = self.validRegisterInputEmail()
    passwordValid = self.validRegisterInputPassword()

    print('emailValid', emailValid)
    print('passwordValid', passwordValid)
    
    if emailValid and passwordValid:
      returnRegister = anvil.server.call('registerUser', self.inputEmail.text, self.inputPassword.text, self.DropDownServer.selected_value)
    
  def validRegisterInputEmail(self):
    checkEmail = anvil.server.call('validEmailInput', self.inputEmail.text)
    
    if checkEmail['status'] is False:
      self.emailErrorMessage.text = checkEmail['message']
      self.column_panel_1.visible = True
      return False
    else: 
      return True

  def validRegisterInputPassword(self, **event_args):
    regexEmpty =  r'^\s*$'

    if re.match(regexEmpty, self.inputPassword.text):
      self.passwordErrorMessage.text = 'O campo senha é obrigatório'
      self.column_panel_2.visible = True
      return False
    else: 
      return True

  def inputEmail_focus(self, **event_args):
    self.column_panel_1.visible = False

  def inputPassword_focus(self, **event_args):
    self.column_panel_2.visible = False



    
      


