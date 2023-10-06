from ._anvil_designer import userRowTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...navbarRigth.resetPassword import resetPassword
from ..registerUser import registerUser

class userRow(userRowTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.currentUser = anvil.users.get_user()

  def button_row_delete_click(self, **event_args):
    if self.currentUser['email'] == self.item['email']:
      alert(
        'Não é possivel excluir seu próprio usuário',
        title='Excluir usuário' 
      )
    else: 
      delete = alert(
        'Tem certeza que deseja exluir o usuario "{}" ?'.format(self.item['email']),
        title='Excluir usuário',
        buttons=[('Excluir', True), ('Cancelar', False)]
      )
      if delete:
        user = app_tables.users.get(email=self.item['email'])
        user.delete()
        self.item['userForm'].refreshTable()
        alert('Usuário excluido com sucesso!')

  def button_row_reset_password_click(self, **event_args):
    modalResetPass = resetPassword()
    confirm = alert(modalResetPass, buttons=[('Confirmar', True), ('Cancelar', False)], large=True)

    while modalResetPass.button_1_click() is False:
      if comfirm:
        confirm = alert(modalResetPass, buttons=[('Confirmar', True), ('Cancelar', False)], large=True)
      else:
        break
  
    if confirm:
      saveNewPassword = anvil.server.call('resetPasswordService', self.item['email'], modalResetPass.inputPassword.text)
      if saveNewPassword:
        alert('Senha redefinida com sucesso!')
      else:
        alert('Ocorreu um erro inesperado, favor tente novamente')

  def button_row_edit_click(self, **event_args):
    alert(registerUser(self), large=True, buttons=None)
