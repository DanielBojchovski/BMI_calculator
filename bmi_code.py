from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    try:
      weight = float(self.text_box_1.text)
      height = float(self.text_box_2.text) / 100
      bmi = round(weight / (height * height), 1)
      if bmi > 24.9:
        alert("Your bmi is " + str(bmi) + ". You should lose weight.")
      elif bmi < 18.5:
        alert("Your bmi is " + str(bmi) + ". You should gain weight.")
      else:
        alert("Your bmi is " + str(bmi) + ". You are in normal range.")
    except:
      alert("Enter only positive numeric values.")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.text = ""
    self.text_box_2.text = ""
