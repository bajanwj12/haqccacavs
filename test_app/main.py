from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

# 固定窗口大小，避免变形
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')

class CalculatorGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(CalculatorGridLayout, self).__init__(** kwargs)
        
        # 设置网格布局：6行4列
        self.cols = 4
        self.rows = 6
        
        # 添加输入框（跨4列）
        self.display = TextInput(
            multiline=False, 
            readonly=True, 
            halign='right', 
            font_size=40,
            size_hint=(1, 0.8)
        )
        self.add_widget(self.display)
        
        # 按钮布局（按行定义）
        buttons = [
            ['C', 'D', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        
        # 添加按钮到布局
        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    font_size=30,
                    background_color=(0.8, 0.8, 0.8, 1) if label not in ['+', '-', '*', '/', '='] else (0.9, 0.5, 0.1, 1)
                )
                # 绑定按钮点击事件
                button.bind(on_press=self.on_button_press)
                self.add_widget(button)
    
    def on_button_press(self, instance):
        button_text = instance.text
        
        # 清除显示
        if button_text == 'C':
            self.display.text = ''
        
        # 删除最后一个字符
        elif button_text == 'D':
            self.display.text = self.display.text[:-1]
        
        # 计算结果
        elif button_text == '=':
            try:
                # 使用eval计算表达式，实际应用中需注意安全问题
                result = str(eval(self.display.text))
                self.display.text = result
            except Exception:
                self.display.text = '?'
        
        # 正负号切换
        elif button_text == '±':
            if self.display.text and self.display.text[0] == '-':
                self.display.text = self.display.text[1:]
            elif self.display.text:
                self.display.text = '-' + self.display.text
        
        # 其他按钮直接添加到显示
        else:
            self.display.text += button_text

class CalculatorApp(App):
    def build(self):
        return CalculatorGridLayout()

if __name__ == '__main__':
    CalculatorApp().run()
#