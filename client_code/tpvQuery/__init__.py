from ._anvil_designer import tpvQueryTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.http
import anvil.media

class tpvQuery(tpvQueryTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    if self.date_picker_1.date is not None:
      response = anvil.server.call(
        'readTpv',
        self.date_picker_1.date,  
        self.date_picker_2.date, 
        self.text_box_1.text,
        self.text_box_2.text, 
      )
      print('response.data: ', response['data'])
      
      self.repeating_panel_1.items = response['data']
    else:
      self.label_5.text = 'Campo obrigatório'
      self.label_5.visible = True

  def button_2_click(self, **event_args):
    excel = anvil.server.call('dowloadExcelTpvQuery', self.repeating_panel_1.items)
    anvil.media.dowload(excel)
