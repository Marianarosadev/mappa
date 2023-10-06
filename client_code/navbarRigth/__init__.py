from ._anvil_designer import navbarRigthTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import popover
from .resetPassword import resetPassword

class navbarRigth(navbarRigthTemplate):
  def __init__(self, **properties):
    self.user = anvil.users.get_user()
    self.button_1.text = self.user['email']
    column = LinearPanel()
    resetPasswordButton = Button(align='left', text='Redefinir Senha', foreground='black', icon='fa:lock')
    resetPasswordButton.add_event_handler('click', self.openResetPassword_click)
    logoutButton = Button(align='center', text='Logout', foreground='black', icon='fa:sign-out')
    logoutButton.add_event_handler('click', self.logoutButtom_click)
    column.add_component(resetPasswordButton, full_width_row=True)
    column.add_component(logoutButton, full_width_row=True)
    self.button_1.popover(column, placement='bottom', trigger='manual', auto_dismiss = True, max_width = '300px') 
    
    self.init_components(**properties)

  def openResetPassword_click(self, **event_args):
    self.button_1.pop('hide')
    modalResetPass = resetPassword()
    confirm = alert(modalResetPass, buttons=[('Confirmar', True), ('Cancelar', False)], large=True)

    while modalResetPass.button_1_click() is False:
      if comfirm:
        confirm = alert(modalResetPass, buttons=[('Confirmar', True), ('Cancelar', False)], large=True)
      else:
        break
  
    if confirm:
      saveNewPassword = anvil.server.call('resetPasswordService', self.user['email'], modalResetPass.inputPassword.text)
      if saveNewPassword:
        alert('Senha redefinida com sucesso!')
      else:
        alert('Ocorreu um erro inesperado, favor tente novamente')

  def logoutButtom_click(self, **event_args):
    self.button_1.pop('hide')
    anvil.users.logout()
    open_form('login')

  def button_1_click(self, **event_args):
    if self.button_1.pop('is_visible'):
      self.button_1.pop('hide')
    else:
      self.button_1.pop('show')
