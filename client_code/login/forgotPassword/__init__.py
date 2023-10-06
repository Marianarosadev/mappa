from ._anvil_designer import forgotPasswordTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.email

class forgotPassword(forgotPasswordTemplate):
  def __init__(self, previousPage = None, **properties):
    self.previousPage = previousPage

    self.init_components(**properties)
  
  def button_1_click(self, **event_args):
    emailValid = self.validRegisterInputEmail()

    if emailValid:
      sendCode = anvil.server.call('sendRecoverEmail', self.inputEmail.text)
      if sendCode['status'] is True:
        open_form('login.recoverCode', self.inputEmail.text, previousPage = self)
      else:
        alert('Falha ao enviar código, tente novamente')

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

      