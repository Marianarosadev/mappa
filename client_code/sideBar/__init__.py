from ._anvil_designer import sideBarTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class sideBar(sideBarTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.admin.visible = anvil.users.get_user()['assignment'] == 'Administrador'
    
  def button_1_click(self, **event_args):
    open_form('home')

  def button_2_click(self, **event_args):
    anvil.users.logout()
    open_form('login')

  def button_3_click(self, **event_args):
    open_form('users')


