from ._anvil_designer import usersTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class users(usersTemplate):
  def __init__(self, **properties):
   
    self.init_components(**properties)

    self.repeating_panel_1.items = app_tables.users.search()