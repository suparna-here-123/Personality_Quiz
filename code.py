'''
- Root widget is the first widget initialised in the first page of the app.  
QUESTIONS :
1) HOW TO ALLOW ONLY ONE OPTION/BUTTON TO BE PRESSED PER QUESTION
2) HOW TO NOT INCREMENT VALUES OF THE CHARACTER TRAITS EVEN IF THE BUTTON IS PRESSED MULTIPLE TIMES?
3) IS THERE A WAY TO RETRIEVE THE VALUE OF THE BUTTON TEXT AND COMPARE ANS WITH THAT INSTEAD OF HAVING SO MANY FUNCTIONS PER BUTTON?
'''
import kivy
from kivy.app import App                # App is a
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config


'''
Config.set('graphics', 'resizable', '0')        # config determines the default settings of the app
Config.set('graphics', 'width', '412')
Config.set('graphics', 'height', '732')
'''

class HomePage(Screen) :
    pass

class Q1 (Screen) :
    pass

class ScreenManagement(ScreenManager) : 
    pass

file = Builder.load_file('Quiz.kv');      ''' The Builder is responsible for creating a Parser for 
                                               parsing a kv file, merging the results into its internal
                                               rules, templates, etc.'''
blue = 0
green = 0
yellow = 0
red = 0 

class QuizApp(App) :
    def build (self) :
        return file
    
    def blueButton (self) :
        global blue
        blue += 1
        print (blue)
    
    def greenButton (self) :
        global green
        green += 1
    
    def yellowButton (self) :
        global yellow
        yellow += 1
    
    def redButton (self) :
        global red
        red += 1


QuizApp().run()
