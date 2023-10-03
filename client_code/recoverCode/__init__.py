from ._anvil_designer import recoverCodeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class recoverCode(recoverCodeTemplate):
  def __init__(self, previousPage = None, **properties):
    self.previousPage = previousPage
    self.previousPage.nextPage = self
    self.timer = 60
    
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    emailValid = self.validRegisterInputEmail()

    if emailValid:
      open_form('resetPassword', previousPage = self)

  def validRegisterInputEmail(self):
    checkEmail = anvil.server.call('validEmailInput', self.inputEmail.text)

    if checkEmail['message'] == 'E-mail já cadastrado':
      return True
    else:
      self.emailErrorMessage.text = 'E-mail não cadastrado no sistema'
      self.column_panel_2.visible = True
      return False

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
        open_form('recoverCode', previousPage = self)
      else:
        alert('Falha ao enviar código, tente novamente')


    

