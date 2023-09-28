from ._anvil_designer import registerTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class register(registerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def registerButton_click(self, **event_args):

    emailValid = validRegisterInputEmail()

    if emailValid:
      returnRegister = anvil.server.call('register', self.inputEmail.text, self.inputPassword.text, self.DropDownServer.selected_value)
    
    if returnRegister['status']:
      open_form('login')
      alert('Cadastro realizado com sucesso')
    elif returnRegister['type'] == 'email':
      self.emailErrorMessage.text = returnRegister['message']
      self.column_panel_1.visible = True
    elif returnRegister['type'] == 'password':
      self.passwordErrorMessage.text = returnRegister['message']
      self.column_panel_2.visible = True
    elif returnRegister['type'] == 'server':
      self.serverErrorMessage.text = returnRegister['message']
      self.column_panel_3.visible = True

  def validRegisterInputEmail(self):
    checkExistingEmail = anvil.server.call('validEmailInput', self.inputEmail.text)

    if checkExistingEmail['status'] is False:
      self.emailErrorMessage.text = returnRegister['message']
      self.column_panel_1.visible = True
      return False
    else: 
      return True

  def inputEmail_focus(self, **event_args):
    self.column_panel_1.visible = False

    
      


