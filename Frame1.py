#Boa:Frame:Frame1
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs, sys

reload(sys)
sys.setdefaultencoding('utf-8')
import wx

global rustaticpart, ltstaticpart 
rustaticpart = '0x04'
ltstaticpart = '0x01'

def formruletters(staticpart):
    letterarray = []
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    for i in range(len(symbols)):
      for y in range(len(symbols)):  
        utfsymbol = staticpart + symbols[i] + symbols[y]
        letterarray.append(utfsymbol)
    return letterarray


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(150, 177), size=wx.Size(842, 433),
              style=wx.DEFAULT_FRAME_STYLE, title='wxPython_Unicode2UTF8')
        self.SetClientSize(wx.Size(834, 406))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(16, 8), size=wx.Size(800, 160),
              style=wx.TE_MULTILINE, value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(16, 216), size=wx.Size(800, 168),
              style=wx.TE_MULTILINE, value='')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label='Convert/Konvertuoti', name='button1', parent=self,
              pos=wx.Point(16, 184), size=wx.Size(160, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2,
              label='UpperCase/Did\xfeiosios raids', name='button2',
              parent=self, pos=wx.Point(208, 184), size=wx.Size(168, 23),
              style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3,
              label='Convert back/Konvertuoti atvirk\xf0\xe8iai',
              name='button3', parent=self, pos=wx.Point(408, 184),
              size=wx.Size(224, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.textCtrl1.SetValue(u'gra\u017Eus oras \u0161iandien lijo')

    def OnButton1Button(self, event):
        global rustaticpart, ltstaticpart
        texttoconvert = self.textCtrl1.GetValue()
        ruletters = formruletters(rustaticpart)
        ltletters = formruletters(ltstaticpart)
        for i in range(len(ruletters)):
          texttoconvert = texttoconvert.replace(unichr(int(ruletters[i], 16)), ruletters[i].replace('0x','\u'))
        for i in range(len(ltletters)):
          texttoconvert = texttoconvert.replace(unichr(int(ltletters[i], 16)), ltletters[i].replace('0x','\u'))          
        self.textCtrl2.SetValue(texttoconvert)

    def OnButton2Button(self, event):
        self.textCtrl1.SetValue(self.textCtrl1.GetValue().upper())

    def OnButton3Button(self, event):
        texttoconvert = self.textCtrl2.GetValue()
        texttoconvert =  texttoconvert.decode('unicode-escape')
        self.textCtrl1.SetValue(texttoconvert)
        #self.textCtrl1.SetValue(u'dd\u017Eudd')
