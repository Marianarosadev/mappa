from ._anvil_designer import resetPasswordTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class resetPassword(resetPasswordTemplate):
  def __init__(self, email, previousPage = None, **properties):
    self.previousPage = previousPage
    self.previousPage.nextPage = self
    self.email = email

    self.init_components(**properties)

  def button_1_click(self, **event_args):

    if self.inputPassword.text == self.inputConfirmPassword.text:
      saveNewPassword = anvil.server.call('resetPasswordService', self.email, self.inputPassword.text)
      if saveNewPassword:
        open_form('login')
        alert('Senha redefinida com sucesso, faça login para acessar o sistema')
      else:  
        alert('Ocorreu um erro inesperado, favor tente novamente')
    else:
      self.passwordErrorMessage.text = 'As senhas não correspondem'
      self.column_panel_2.visible = True

  def inputCode_focus(self, **event_args):
    self.column_panel_2.visible = False
