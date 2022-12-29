'''
- Root widget is the first widget initialised in the first page of the app.  
QUESTIONS :
1) HOW TO ALLOW ONLY ONE OPTION/BUTTON TO BE PRESSED PER QUESTION
Ans : Can update the values only once the submit/next button is pressed in that question page. 

2) HOW TO NOT INCREMENT VALUES OF THE CHARACTER TRAITS EVEN IF THE BUTTON IS PRESSED MULTIPLE TIMES?
The Builder is responsible for creating a Parser for 
                                               parsing a kv file, merging the results into its internal
                                               rules, templates, etc.
'''


from cgitb import text
from typing import final
from unicodedata import name
import kivy
from kivy.app import App                
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.config import Config
from numpy import char, character
from poll_values import *


# HAVE TO UPDATE THE VALUE OF d THAT IS BEING CHANGED HERE IN THE POLL_VALUES FILE. 
class HomePage(Screen) :
    pass

class q1 (Screen) :
    def optionClicked(self, instance, value, option) :
        global d

        if option == 'A' :
            d['Alex']+= 1

        elif option == 'Cam' :
            d['Cam'] += 1
        
        elif option == 'G':
            d['Gloria'] += 1
            
        
        elif option == 'Cl' :
            d['Claire'] += 1
            

        elif option == 'M' :
            d['Manny'] += 1
        
        elif option == 'P' :
            d['Phil'] += 1
        
        with open('poll_values.py', 'r+') as f :
            lines = f.read().split('\n')
            lines[0] = 'd = ' + str(d)

            f.seek(0)

            f.writelines('\n'.join(lines))



class q2(Screen) :
    def optionClicked(self, instance, value, option) :
        global d

        if option == 'A' :
            d['Alex']+= 1

        elif option == 'Cam' :
            d['Cam'] += 1
        
        elif option == 'G':
            d['Gloria'] += 1
            
        
        elif option == 'Cl' :
            d['Claire'] += 1
            

        elif option == 'M' :
            d['Manny'] += 1
        
        elif option == 'P' :
            d['Phil'] += 1
        
        with open('poll_values.py', 'r+') as f :
            lines = f.read().split('\n')
            lines[0] = 'd = ' + str(d)

            f.seek(0)

            f.writelines('\n'.join(lines))

class q3(Screen) :
    def optionClicked(self, instance, value, option) :
        global d

        if option == 'A' :
            d['Alex']+= 1

        elif option == 'Cam' :
            d['Cam'] += 1
        
        elif option == 'G':
            d['Gloria'] += 1
            
        
        elif option == 'Cl' :
            d['Claire'] += 1
            

        elif option == 'M' :
            d['Manny'] += 1
        
        elif option == 'P' :
            d['Phil'] += 1
        
        with open('poll_values.py', 'r+') as f :
            lines = f.read().split('\n')
            lines[0] = 'd = ' + str(d)

            f.seek(0)

            f.writelines('\n'.join(lines))

class q4(Screen) :
    def optionClicked(self, instance, value, option) :
        global d

        if option == 'A' :
            d['Alex']+= 1

        elif option == 'Cam' :
            d['Cam'] += 1
        
        elif option == 'G':
            d['Gloria'] += 1
            
        
        elif option == 'Cl' :
            d['Claire'] += 1
            

        elif option == 'M' :
            d['Manny'] += 1
        
        elif option == 'P' :
            d['Phil'] += 1
        
        with open('poll_values.py', 'r+') as f :
            lines = f.read().split('\n')
            lines[0] = 'd = ' + str(d)

            f.seek(0)

            f.writelines('\n'.join(lines))

class q5 (Screen) :
    def optionClicked(self, instance, value, option) :
        global d

        if option == 'A' :
            d['Alex']+= 1

        elif option == 'Cam' :
            d['Cam'] += 1
        
        elif option == 'G':
            d['Gloria'] += 1
            
        
        elif option == 'Cl' :
            d['Claire'] += 1
            

        elif option == 'M' :
            d['Manny'] += 1
        
        elif option == 'P' :
            d['Phil'] += 1
        
        with open('poll_values.py', 'r+') as f :
            lines = f.read().split('\n')
            lines[0] = 'd = ' + str(d)

            f.seek(0)

            f.writelines('\n'.join(lines))

class q6 (Screen) :
    def optionClicked(self, instance, value, option) :
        global d

        if option == 'A' :
            d['Alex']+= 1

        elif option == 'Cam' :
            d['Cam'] += 1
        
        elif option == 'G':
            d['Gloria'] += 1
            
        
        elif option == 'Cl' :
            d['Claire'] += 1
            

        elif option == 'M' :
            d['Manny'] += 1
        
        elif option == 'P' :
            d['Phil'] += 1
        
        with open('poll_values.py', 'r+') as f :
            lines = f.read().split('\n')
            lines[0] = 'd = ' + str(d)

            f.seek(0)

            f.writelines('\n'.join(lines))
class calculating(Screen) :                 # this part is calculating the character with the highest poll value. 
    def result(self) :
        print ('you are' + find())
'''
        class finalPage(App) :
            def build(self) :
                self.window = GridLayout()
                self.window.add_widget(Label = text("you are" + find()))
                return self.window
            
        
        finalPage().run()
'''
        

class ScreenManagement(ScreenManager) : 
    pass  


class QuizApp(App) : 
    def build (self) :
        self.load_kv('Quiz.kv')
        
        
if __name__ == '__main__' :
    QuizApp().run()
    with open('poll_values.py', 'r+') as f :
        lines = f.read().split('\n')
        lines[0] = "d = {'Phil': 0, 'Alex': 0, 'Gloria': 0, 'Manny': 0, 'Cam': 0, 'Claire': 0}"
        f.seek(0)
        f.writelines('\n'.join(lines))










