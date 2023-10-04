from ._anvil_designer import loginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class login(loginTemplate):
  def __init__(self, **properties):
    
    self.init_components(**properties)

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_1_click(self, **event_args):
    try: 
      userLoged = anvil.users.login_with_email(self.email.text, self.password.text, remember=True)
      open_form('home')
    except Exception as e: 
      print(e)
      
      if str(e) == 'Incorrect email address or password':
        email = app_tables.users.get(email=self.email.text)
        if email is None:
          self.emailErrorMessage.text = 'E-mail inválido'
          self.column_panel_2.visible = True
        else: 
          self.emailErrorMessage_password.text = 'Senha inválida'
          self.column_panel_3.visible = True
      elif str(e) == 'This account has not been enabled by an administrator':
          self.emailErrorMessage.text = 'Usuário desabilitado, contate o administrador'
          self.column_panel_2.visible = True
  
  
  def button_2_click(self, **event_args):
    open_form('register')

  def email_focus(self, **event_args):
    self.column_panel_2.visible = False

  def password_focus(self, **event_args):
    self.column_panel_3.visible = False

  def redirectRecoverPassword_click(self, **event_args):
    open_form('forgotPassword', previousPage = self)
    