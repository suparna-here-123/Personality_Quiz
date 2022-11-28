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


import kivy
from kivy.app import App                
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.config import Config


Claire = 0              # initialising all character's votes to 0 before the start. 
Phil = 0
Alex = 0
Gloria = 0
Manny = 0
Cam = 0


class HomePage(Screen) :
    pass

class q1 (Screen) :
    def optionClicked(self, instance, value, option) :
        global Claire, Phil, Alex, Gloria, Manny, Cam


        if option == 'A' :
            Alex += 1
        
        elif option == 'Cam' :
            Cam += 1
        
        elif option == 'G' :
            Gloria += 1
        
        elif option == 'M' :
            Manny += 1
        
        elif option == 'Cl' :
            Claire += 1
        
        elif option == "P" :
           Phil += 1
        
        print ('Alex', Alex)
        print ('Claire', Claire)
        print ('phil', Phil)
        print ('Gloria', Gloria)
        print ('Manny', Manny)
        print ('cam', Cam)
        print ("_______________________")

class q2(Screen) :
    def optionClicked(self, instance, value, option) :
        global Claire, Phil, Alex, Gloria, Manny, Cam


        if option == 'A' :
            Alex += 1
        
        elif option == 'Cam' :
            Cam += 1
        
        elif option == 'G' :
            Gloria += 1
        
        elif option == 'M' :
            Manny += 1
        
        elif option == 'Cl' :
            Claire += 1
        
        elif option == "P" :
           Phil += 1
        
        print ('Alex', Alex)
        print ('Claire', Claire)
        print ('phil', Phil)
        print ('Gloria', Gloria)
        print ('Manny', Manny)
        print ('cam', Cam)
        print ("_______________________")


class ScreenManagement(ScreenManager) : 
    pass

file = Builder.load_file('Quiz.kv');     

class QuizApp(App) :                    
    def build (self) :
        return file


QuizApp().run()
