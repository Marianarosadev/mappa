from ._anvil_designer import registerUserTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class registerUser(registerUserTemplate):
  def __init__(self, userForm,**properties):
    self.init_components(**properties)
    self.userForm = userForm

  def registerButton_click(self, **event_args):
    nameValid = self.validRegisterInputName()
    emailValid = self.validRegisterInputEmail()
    assignment = self.velidRegisterAssignment()

    if nameValid and emailValid and assignment:
      returnRegister = anvil.server.call('registerUser', self.inputName.text, self.inputEmail.text, self.DropDownAssignment.selected_value)
      self.raise_event('x-close-alert')
      if returnRegister:
        self.userForm.refreshTable()
        alert('Novo usuário cadastrado com sucesso')
      else:
        alert('Ocorreu um erro ao cadastrar o usuário, tente novamente')
  
  def validRegisterInputName(self):
    regexEmpty =  r'^\s*$'

    if re.match(regexEmpty, self.inputName.text):
      self.nameErrorMessage.text = 'O campo Nome é obrigatório'
      self.column_panel_1.visible = True
      return False
    else:
      return True
      
  def validRegisterInputEmail(self):
    checkEmail = anvil.server.call('validEmailInput', self.inputEmail.text)

    if checkEmail['status'] is False:
      self.emailErrorMessage.text = checkEmail['message']
      self.column_panel_2.visible = True
      return False
    else:
      return True

  def velidRegisterAssignment(self):
    if self.DropDownAssignment.selected_value is None:
      self.assignmentErrorMessage.text = 'Escolha uma opção de Atribuição'
      self.column_panel_3.visible = True
      return False
    else:
      return True

  def inputName_focus(self, **event_args):
    self.column_panel_1.visible = False

  def inputEmail_focus(self, **event_args):
    self.column_panel_2.visible = False

  def DropDownAssignment_change(self, **event_args):
    self.column_panel_3.visible = False

  def inputEmail_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass


