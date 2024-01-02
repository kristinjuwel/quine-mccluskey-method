from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'system')
Config.set('graphics', 'resizable', False)
from random import sample

import kivy
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen

kivy.require('1.9.0')
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager


import print
import globals
screen_helper = '''
#:import utils kivy.utils

ScreenManager:
    Menu:
        name: 'Menu'
    Input_User:
        name: 'Input'
    Results:
        name: 'Results'
    Results2:
        name: 'Results2'
    Results3:
        name: 'Results3'

<Menu>:
    Widget:
        canvas:
            Color:
                rgba: 231/255, 255/255, 246/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        #title
        Image:
            source: 'cubs.png'
            pos_hint: {'center_x': .50, 'center_y': .46}
            size_hint: (.65,.65)

        Label:
            text: "Quine McCluskey Method"
            pos_hint: {'center_x': .52, 'center_y': .85} 
            size_hint: 1, 0.1
            font_size: self.width/15
            font_name:"Thirsty Script"
            color: '#000000'
        Label:
            text: "-----------------------------------------"
            pos_hint: {'center_x': .52, 'center_y': .78} 
            size_hint: 1, 0.1
            font_size: self.width/40
            font_name:"mamabear"
            color: '#000000'
        Label:
            text: "by: Abram Dorado & Kristine Malimban"
            pos_hint: {'center_x': .52, 'center_y': .75} 
            size_hint: 1, 0.1
            font_size: self.width/43
            font_name:"mamabear"
            color: '#0B223A'
            
        Button:
            text: "START"
            background_color :'#000000'
            font_size: self.width/15
            size_hint: (.25,.10)
            font_name:"mamabear"
            pos_hint: {'center_x': .35, 'center_y': .13}
            background_normal: ""

            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Input'

        Button:
            text: "QUIT"
            background_color :'#000000'
            font_size: self.width/15
            size_hint: (.25,.10)
            font_name:"mamabear"
            pos_hint: {'center_x': .65, 'center_y': .13}
            background_normal: ""

            on_press:
                quit()

<Input_User>:
    Widget:
        canvas:
            Color:
                rgba: 231/255, 255/255, 246/255, 1
            Rectangle:
                size: self.size
                pos: self.pos   
    FloatLayout:
        Image:
            source: 'bears.png'
            pos_hint: {'center_x': .50, 'center_y': .80}
            size_hint: (.90,.90)
        Button:
            text: "Enter minterms:"
            background_color :'#000000'
            size_hint: (.50,.07)
            font_size: self.width/20
            font_name:"mamabear"
            pos_hint: {'center_x': .50, 'center_y': .68}
            background_normal: ""
        Button:
            size_hint: (.50,.07)
            pos_hint: {'center_x': .50, 'center_y': .60}
            background_color :'#FFFFFF'
            background_normal: ""   

        Label:
            text: "Chosen variables: "
            size_hint: (.50,.07)
            font_size: self.width/30
            color: '#000000'
            font_name:"mamabear"
            pos_hint: {'center_x': .65, 'center_y': .50}
        Button:
            size_hint: (.24,.07)
            pos_hint: {'center_x': .65, 'center_y': .42}
            background_color :'#FFFFFF'
            background_normal: ""
      
        Label:
            text: "Don't care terms(if there is): "
            size_hint: (.50,.07)
            font_size: self.width/30
            font_name:"mamabear"
            color: '#000000'
            pos_hint: {'center_x': .35, 'center_y': .50}
        Button:
            size_hint: (.24,.07)
            pos_hint: {'center_x': .35, 'center_y': .42}
            background_color :'#FFFFFF'
            background_normal: ""

        Label:
            text: "Number of variables: "
            size_hint: (.50,.07)
            font_size: self.width/30
            font_name:"mamabear"
            color: '#000000'
            pos_hint: {'center_x': .50, 'center_y': .35}
        Button:
            size_hint: (.24,.07)
            pos_hint: {'center_x': .50, 'center_y': .27}
            background_color :'#FFFFFF'
            background_normal: ""
        
        Button:
            text: "SEE RESULTS"
            background_color :'#000000'
            background_normal: ""
            size_hint: (.25,.10)
            font_size: self.width/15
            font_name:"mamabear"
            pos_hint: {'center_x': .35, 'center_y': .13}
            
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Results'
                root.manager.get_screen('Results').ids.final_output.text = root.inputs(variableChoice.text, mintermInput.text, dontCare.text, sizing.text)
                root.manager.get_screen('Results2').ids.final_output1.text = root.input1(variableChoice.text, mintermInput.text, dontCare.text, sizing.text)
                root.manager.get_screen('Results3').ids.final_output2.text = root.input2(variableChoice.text, mintermInput.text, dontCare.text,sizing.text)
        Button:
            text: "RETURN"
            background_color :'#000000'
            background_normal: ""
            font_size: self.width/15
            size_hint: (.25,.10)
            font_name:"mamabear"
            pos_hint: {'center_x': .65, 'center_y': .13}

            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Menu'
                
    
        MDTextField: 
            id: mintermInput
            icon_right_color: app.theme_cls.primary_color
            background_color :'#A6C3D4'
            background_normal: ""
            hint_text: "Enter minterms: (2 4 6 8 10)"
            font_name:"mamabear"
            pos_hint:{'center_x': 0.5, 'center_y': 0.60}
            size_hint_x:None
            width:375

        MDTextField: 
            id: variableChoice
            icon_right_color: app.theme_cls.primary_color
            background_color :'#A6C3D4'
            background_normal: ""
            hint_text: "Enter starting letter(Ex. A)"
            font_name:"mamabear"
            pos_hint: {'center_x': .65, 'center_y': .42}
            size_hint_x:None
            width:150

        MDTextField:
            id: dontCare
            icon_right_color: app.theme_cls.primary_color
            background_color :'#A6C3D4'
            background_normal: ""
            hint_text: "Enter don't care terms"
            font_name:"mamabear"
            pos_hint: {'center_x': .35, 'center_y': .42}
            size_hint_x:None
            width:150
        
        MDTextField:
            id: sizing
            icon_right_color: app.theme_cls.primary_color
            background_color :'#A6C3D4'
            background_normal: ""
            hint_text: "Enter no. of variables"
            font_name:"mamabear"
            pos_hint: {'center_x': .50, 'center_y': .27}
            size_hint_x:None
            width:150
        
        
             
<Results>:
    Widget:
        canvas:
            Color:
                rgba: 231/255, 255/255, 246/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        Label:
            id: final_output
            text: ""
            multiline: True
            color:'#000000'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"mamabear"
            size_hint: (.25,.10)
            pos_hint: {'center_x': .50, 'center_y': .53} 
            font_size: self.width/15

        Image:
            source: 'line.png'
            pos_hint: {'center_x': .17, 'center_y': .50}
            size_hint: (.90,.90)
        Image:
            source: 'up.png'
            size_hint: (.15,.15)
            pos_hint: {'center_x': .10, 'center_y': .90} 
        Image:
            source: 'up.png'
            size_hint: (.15,.15)
            pos_hint: {'center_x': .10, 'center_y': .10} 
        Label:
            text:
                """
                F
                I
                R
                S
                T
                |
                T
                A
                B
                L
                E
                """
            color:'#205566'
            font_name:"mamabear"
            font_size: self.width/20
            size_hint: (.80,.07)
            pos_hint: {'center_x': .10, 'center_y': .50} 
            
        Button:
            background_normal: '4.png'
            size_hint: (.20,.20)
            pos_hint: {'center_x': .90, 'center_y': .70} 
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Input'

        Button:
            background_normal: '2.png'
            size_hint: (.20,.20)
            pos_hint: {'center_x': .90, 'center_y': .50} 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Results2'

        Button:
            background_normal: '1.png'
            size_hint: (.20,.20)
            pos_hint: {'center_x': .90, 'center_y': .30}
            on_press:
                quit()
        
<Results2>:
    Widget:
        canvas:
            Color:
                rgba: 231/255, 255/255, 246/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        Label:
            id: final_output1
            text: ""
            multiline: True
            color:'#000000'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"mamabear"
            size_hint: (.25,.10)
            pos_hint: {'center_x': .50, 'center_y': .53} 
            font_size: 10

        Image:
            source: 'line.png'
            pos_hint: {'center_x': .17, 'center_y': .50}
            size_hint: (.90,.90)
        Image:
            source: 'up.png'
            size_hint: (.15,.15)
            pos_hint: {'center_x': .10, 'center_y': .90} 
        Image:
            source: 'up.png'
            size_hint: (.15,.15)
            pos_hint: {'center_x': .10, 'center_y': .10} 
        Label:
            text: 
                """
                N
                E
                X
                T
                |
                T
                A
                B
                L
                E
                """
            color:'#205566'
            font_name:"mamabear"
            font_size: self.width/20
            size_hint: (.80,.07)
            pos_hint: {'center_x': .10, 'center_y': .50} 
            
        Button:
            background_normal: 'return.png'
            size_hint: (.20,.20)
            pos_hint: {'center_x': .90, 'center_y': .70} 
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Results'
        
        Button:
            background_normal: '2.png'
            size_hint: (.20,.20)
            pos_hint: {'center_x': .90, 'center_y': .50} 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Results3'

        Button:
            background_normal: '1.png'
            size_hint: (.20,.20)
            pos_hint: {'center_x': .90, 'center_y': .30}
            on_press:
                quit()
<Results3>:
    Widget:
        canvas:
            Color:
                rgba: 231/255, 255/255, 246/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        Label:
            id: final_output2
            text: ""
            multiline: True
            color:'#000000'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"mamabear"
            size_hint: (.25,.10)
            pos_hint: {'center_x': .50, 'center_y': .50} 
            font_size: self.width/20

        Image:
            source: 'line.png'
            pos_hint: {'center_x': .17, 'center_y': .50}
            size_hint: (.90,.90)
        Image:
            source: 'up.png'
            size_hint: (.15,.15)
            pos_hint: {'center_x': .10, 'center_y': .90} 
        Image:
            source: 'up.png'
            size_hint: (.15,.15)
            pos_hint: {'center_x': .10, 'center_y': .08} 
        Label:
            text: 
                """
                F
                I
                N
                A
                L
                |
                T
                A
                B
                L
                E"""
            color:'#205566'
            font_name:"mamabear"
            font_size: self.width/20
            size_hint: (.80,.07)
            pos_hint: {'center_x': .10, 'center_y': .50} 
            
        Button:
            background_normal: 'return.png'
            font_name:"mamabear"
            size_hint: (.20,.20)
            pos_hint: {'center_x': .90, 'center_y': .60} 
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Results2'

        Button:
            background_normal: '1.png'
            size_hint: (.20,.20)
            pos_hint: {'center_x': .90, 'center_y': .40}
            on_press:
                quit()

'''
#fonts
LabelBase.register(name='Thirsty Script', 
                   fn_regular='ThirstyScriptExtraBoldDemo.otf')
LabelBase.register(name='mamabear', 
                   fn_regular='mamabear.otf')


class Menu(Screen):
    pass
  
class Input_User(Screen):
    def __init__(self, **kwargs):
        super(Input_User, self).__init__(**kwargs)

    def inputs(self, variable, minterms, dontCare, sizing):
        globals.initialize() 
        globals.unmarked1
        print.driver(variable, minterms, dontCare,sizing)
        ntext = globals.var4.replace(u'\t', u' ' * 8)
        return ntext
        
    def input1(self, variable, minterms, dontCare, sizing):
        globals.initialize() 
        print.driver(variable, minterms, dontCare, sizing)
        ntext = globals.vari4.replace(u'\t', u' ' * 8)
        return ntext
    
    def input2(self, variable, minterms, dontCare, sizing):
        globals.initialize() 
        print.driver(variable, minterms, dontCare, sizing)
        ntext = globals.chart.replace(u'\t', u' ' * 8)
        variable2 = globals.txt2
        return globals.status+globals.unmarked1+globals.space+variable2 + ntext + globals.error
    
class Results(Screen):

    pass

class Results2(Screen):
    pass

class Results3(Screen):
    pass
    

screen_manager = ScreenManager()


# Add the screens to the manager and then supply a name
# that is used to switch screens

screen_manager.add_widget(Menu(name ="Menu"))
screen_manager.add_widget(Input_User(name ="Input"))
screen_manager.add_widget(Results(name ="Results"))
screen_manager.add_widget(Results2(name ="Results2"))
screen_manager.add_widget(Results3(name ="Results3"))

class TabulationMethod(MDApp):
    def build(self): 
        screen = FloatLayout()
        Window.clearcolor = (1,0,0,1)
        self.theme_cls.primary_palette = "Teal"
        Window.size = (1000, 770)
        self.screen = Builder.load_string(screen_helper)
        screen.add_widget(self.screen)       
        return screen


# run the app
if __name__ == "__main__":
    app = TabulationMethod()
    app.run()