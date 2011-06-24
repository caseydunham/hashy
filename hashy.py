import os
import sys
import argparse
import wx
import hashy


class HashyFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, hashy.VERSION_STR)

        self.panel = wx.Panel(self, wx.ID_ANY)
 
        labelSize = (50, -1)
        
        fileBtn = wx.Button(self.panel, wx.ID_ANY, 'File')
        self.labelFile = wx.StaticText(self.panel, wx.ID_ANY, '', size=labelSize)
        
        labelOne = wx.StaticText(self.panel, wx.ID_ANY, 'sha256', size=labelSize)
        self.inputTxtOne = wx.TextCtrl(self.panel, wx.ID_ANY, '', size=(550,-1), style=wx.TE_READONLY)
        
        labelTwo = wx.StaticText(self.panel, wx.ID_ANY, 'md5', size=labelSize)
        self.inputTxtTwo = wx.TextCtrl(self.panel, wx.ID_ANY, '', style=wx.TE_READONLY)
 
        labelThree = wx.StaticText(self.panel, wx.ID_ANY, 'sha224', size=labelSize)
        self.inputTxtThree = wx.TextCtrl(self.panel, wx.ID_ANY, '', style=wx.TE_READONLY)
 
        labelFour = wx.StaticText(self.panel, wx.ID_ANY, 'sha384', size=labelSize)
        self.inputTxtFour = wx.TextCtrl(self.panel, wx.ID_ANY, '', style=wx.TE_READONLY)
 
        labelFive = wx.StaticText(self.panel, wx.ID_ANY, 'sha1', size=labelSize)
        self.inputTxtFive = wx.TextCtrl(self.panel, wx.ID_ANY, '', style=wx.TE_READONLY)
        
        labelSix = wx.StaticText(self.panel, wx.ID_ANY, 'sha512', size=labelSize)
        self.inputTxtSix = wx.TextCtrl(self.panel, wx.ID_ANY, '', style=wx.TE_READONLY)
        
        topSizer = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputThreeSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFiveSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputSixSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        titleSizer.Add(fileBtn, 0, wx.ALL, 5)
        titleSizer.Add(self.labelFile, 0, wx.ALL, 5)
 
        inputOneSizer.Add(labelOne, 0, wx.ALL, 5)
        inputOneSizer.Add(self.inputTxtOne, 1, wx.ALL|wx.EXPAND, 5)
 
        inputTwoSizer.Add(labelTwo, 0, wx.ALL, 5)
        inputTwoSizer.Add(self.inputTxtTwo, 1, wx.ALL|wx.EXPAND, 5)

        inputThreeSizer.Add(labelThree, 0, wx.ALL, 5)
        inputThreeSizer.Add(self.inputTxtThree, 1, wx.ALL|wx.EXPAND, 5)

        inputFourSizer.Add(labelFour, 0, wx.ALL, 5)
        inputFourSizer.Add(self.inputTxtFour, 1, wx.ALL|wx.EXPAND, 5)
 
        inputFiveSizer.Add(labelFive, 0, wx.ALL, 5)
        inputFiveSizer.Add(self.inputTxtFive, 1, wx.ALL|wx.EXPAND, 5)
        
        inputSixSizer.Add(labelSix, 0, wx.ALL, 5)
        inputSixSizer.Add(self.inputTxtSix, 1, wx.ALL|wx.EXPAND, 5)
 
        topSizer.Add(titleSizer, 0, wx.LEFT)
        topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputOneSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputTwoSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputThreeSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputFourSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputFiveSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputSixSizer, 0, wx.ALL|wx.EXPAND, 5)
        
        self.panel.SetSizer(topSizer)
        topSizer.Fit(self)
        
        self.Centre()
        
        self.Bind(wx.EVT_BUTTON, self.on_file, fileBtn)

    def on_file(self, event):
        self.dirname = ''
        self.filename = ''
        dlg = wx.FileDialog(self, 'Choose a file', self.dirname)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetCursor(wx.StockCursor(wx.CURSOR_WAIT))
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            abspath = os.path.join(self.dirname, self.filename)
            self.labelFile.SetLabel(abspath)
            h = hashy.hash(abspath, 'sha256')
            self.inputTxtOne.SetValue(h)
            h = hashy.hash(abspath, 'md5')
            self.inputTxtTwo.SetValue(h)
            h = hashy.hash(abspath, 'sha224')
            self.inputTxtThree.SetValue(h)
            h = hashy.hash(abspath, 'sha384')
            self.inputTxtFour.SetValue(h)
            h = hashy.hash(abspath, 'sha1')
            self.inputTxtFive.SetValue(h)
            h = hashy.hash(abspath, 'sha512')
            self.inputTxtSix.SetValue(h)
            self.SetCursor(wx.StockCursor(wx.CURSOR_DEFAULT))
        dlg.Destroy()


class HashyApp(wx.App):

    def OnInit(self):
        frame = HashyFrame()
        frame.Show(True)
        return True

   
if __name__ == '__main__':
    if len(sys.argv) == 1:
        app = HashyApp()
        app.MainLoop()
    else:
        parser = argparse.ArgumentParser(description='hash a file')
        parser.add_argument('--version', help='print version information', action='version', version=hashy.VERSION_STR)
        parser.add_argument('-verify', type=str, help='compute file hash and compare against passed in hash', metavar='verify')
        parser.add_argument('-hash', type=str, help='hash algorithm to use. can be one of ' + hashy.algorithms, metavar='hash',
            default=hashy.DEFAULT_ALGORITHM, choices=hashy.algorithms)
        parser.add_argument('file', type=str, help='file to compute hash')

        args = parser.parse_args()
        h = hashy.hash(args.file, args.hash)
        if h:
            if args.verify:
                if h == args.verify:
                    print 'hashes match'
                else:
                    print 'hashes are not the same!'
            else:
                print '%s:%s' % (args.hash, h)
