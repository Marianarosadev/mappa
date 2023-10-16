from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel_1
    # self.repeating_panel_1.items = [
    #     {'name': 'Alice', 'address': '1 Road Street'},
    #     {'name': 'Bob', 'address': '2 City Town'}
    # ]

    # Any code you write here will run before the form opens.
