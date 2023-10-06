from ._anvil_designer import usersTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from .registerUser import registerUser

class users(usersTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.refreshTable()

  def button_1_click(self, **event_args):
    alert(registerUser(self), large=True, buttons=None)

  def refreshTable(self):
    usersRegistered = app_tables.users.search()
    usersRegistered = [ dict(u) | {'userForm': self} for u in usersRegistered]
    self.repeating_panel_1.items = usersRegistered