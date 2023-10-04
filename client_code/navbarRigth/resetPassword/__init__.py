from ._anvil_designer import resetPasswordTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class resetPassword(resetPasswordTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)

  def button_1_click(self, **event_args):

    if self.inputPassword.text == self.inputConfirmPassword.text:
      return True
    else:
      self.passwordErrorMessage.text = 'As senhas não correspondem'
      self.column_panel_2.visible = True
      return False
  
  def inputCode_focus(self, **event_args):
    self.column_panel_2.visible = False
