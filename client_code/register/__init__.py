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
    encryptedPassword = anvil.server.call('encryptedPassword', self.inputEmail.text, self.inputPassword.text, self.DropDownServer.selected_value)
    

