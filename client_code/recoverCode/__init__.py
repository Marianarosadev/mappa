from ._anvil_designer import recoverCodeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class recoverCode(recoverCodeTemplate):
  def __init__(self, email, previousPage = None, **properties):
    self.previousPage = previousPage
    self.previousPage.nextPage = self
    self.timer = 60
    self.email = email
    
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    user = app_tables.users.get(email=self.email)
    
    if user['recover_code'] == self.inputCode.text:
      open_form('resetPassword', self.email, previousPage = self)
    else:
      self.codeErrorMessage.text = 'Código inválido'
      self.column_panel_2.visible = True

  def button_2_click(self, **event_args):
    open_form(self.previousPage)

  def timer_1_tick(self, **event_args):
    if self.timer == 0:
      self.button_3.enabled = True
      self.button_3.text = 'Reenviar código'
      self.timer_1.interval = 0
    else:
      self.button_3.text = 'Reenviar código ({})'.format(self.timer)
      self.timer-=1

  def button_3_click(self, **event_args):
    sendCode = anvil.server.call('sendRecoverEmail', self.inputEmail.text)
    if sendCode['status'] is True:
      self.timer = 60
      self.button_3.text = 'Reenviar código ({})'.format(self.timer)
      self.timer_1.interval = 1
      alert('Código reenviado com sucesso')
    else:
      alert('Falha ao reenviar código, tente novamente')

  def inputCode_focus(self, **event_args):
    self.column_panel_2.visible = False




    

