from ._anvil_designer import tpvQueryTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.http

class tpvQuery(tpvQueryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    if self.date_picker_1.date is not None:
      url = 'https://api-datascience.cappta.com.br/transactions_by_docid_date_v1v2noxus'
      try:
        response = anvil.http.request( 
          url=url,
          method='GET',
        )
      except Exception as e:
        print('e: ', e)
    
      # anvil.server.call(
      #   'readTpv',
      #   self.date_picker_1.date,  
      #   self.date_picker_2.date, 
      #   self.text_box_1.text,
      #   self.text_box_2.text, 
      # )
    else:
      self.label_5.text = 'Campo obrigatório'
      self.label_5.visible = True

