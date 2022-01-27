from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os
from PyPDF2 import PdfFileMerger


class Concator(GridLayout):
    def __init__(self, **kwargs):
        super(Concator, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 3

        # first label
        self.inside.add_widget(Label(text=' Enter File Path --->'))

        # first text input
        self.input = TextInput()
        self.inside.add_widget(self.input)

        # first button
        self.search = Button(text='search')
        self.search.bind(on_press=self.pressed)
        self.inside.add_widget(self.search)

        self.add_widget(self.inside)

        # second label
        self.files = Label(text='nothing here',
                           pos_hint={'center_x': 0.8, 'center_y': 0.2},
                           font_size='15sp',
                           halign='left',
                           valign='top',
                           text_size=(700, None)

                           )
        self.add_widget(self.files)

        # third button
        self.concatpdf = Button(text="Concat_Pdf")
        self.concatpdf.bind(on_press=self.to_one)
        self.add_widget(self.concatpdf)

    def pressed(self, *args):
        try:
            path = str(os.listdir(str(self.input.text)))

        except:
            self.input.text = ""
            self.files.text = 'wrong path is entered!'
        try:
            self.tocwd=self.input.text
            self.input.text = ""
            self.files.text = path
        except:
            pass

    def to_one(self, *args):
        os.chdir(str(self.tocwd))
        self.l = os.listdir(str(self.tocwd))
        self.listpdf = []
        for i in self.l:
            if i.endswith('pdf'):
                self.listpdf.append(i)

        self.merger = PdfFileMerger()
        
        if len(self.listpdf) > 1:
            no = 1
            for pdf in self.listpdf:
                self.merger.append(pdf)
                no += 1

            self.merger.write("result" + str(no) + ".pdf")
            self.merger.close()
            self.files.text = 'successfully concated all pdf files\n  and saved in ' + self.tocwd + '\n as result' + str(
                no) + '.pfd'
        if len(self.listpdf) < 2:
            self.files.text = 'only one pdf file is present in the given directory\n cannot concat one pdf'


class Concat_PDF(App):
    def build(self):
        return Concator()


if __name__ == '__main__':
    Concat_PDF().run()


