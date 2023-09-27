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
    returnRegister = anvil.server.call('encryptedPassword', self.inputEmail.text, self.inputPassword.text, self.DropDownServer.selected_value)
    
    if returnRegister['status']:
      open_form('login')
      alert('Cadastro realizado com sucesso')
    else:
      self.emailErrorMessage.text = returnRegister['message']
      self.column_panel_2.visible = True

  def inputEmail_focus(self, **event_args):
    self.column_panel_2.visible = False




    
      


