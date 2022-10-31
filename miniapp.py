from tkinter import *
from tkinter import tkk

# not finished

class Calculator:
    calc_value = 0.0
    div_trigger = False
    mul_trigger = False
    sub_trigger = False
    add_trigger = False

    def button_pressed(self, value):
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, entry_val)

    def is_float(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.is_float(str(self.number_entry.get())):
            self.add_trigger = False
            self.sub_trigger = False
            self.mul_trigger = False
            self.div_trigger = False
            self.calc_value = float(self.entry_value.get())
            if value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif value == "*":
                print("* Presseed")
                self.mul_trigger = True
            elif value == "+":
                print("+ Presseed")
                self.add_trigger = True
            else:
                print("- Presseed")
                self.sub_trigger = True

            self.number_entry.delete(0, "end")

    def equal_button_press(self):
        if self.add_trigger or self.sub_trigger or self.mul_trigger or self.div_trigger:
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
