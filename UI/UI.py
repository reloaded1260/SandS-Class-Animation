import wx
import win32api


class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, -1))
        self.file_name = ''
        self.dir_name = ''
        self.CreateStatusBar()

        filemenu = wx.Menu()

        menuAbout = filemenu.Append(wx.ID_ABOUT, "关于", "关于此程序")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "退出", "结束程序")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&文件")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer5 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.sizer.Add(self.sizer1, 0, wx.GROW)
        self.sizer.Add(self.sizer2, 0, wx.GROW)
        self.sizer.Add(self.sizer3, 0, wx.GROW)
        self.sizer.Add(self.sizer4, 0, wx.GROW)
        self.sizer.Add(self.sizer5, 0, wx.GROW)
        self.sizer.Add(self.sizer6, 0, wx.GROW)

        self.button1 = wx.Button(self, -1, "相加")
        self.button2 = wx.Button(self, -1, "平移")
        self.button3 = wx.Button(self, -1, "反转")
        self.button4 = wx.Button(self, -1, "尺度变化")

        self.button5 = wx.Button(self, -1, "理解")
        self.button6 = wx.Button(self, -1, "理解1")
        self.button7 = wx.Button(self, -1, "采样定理")

        self.button8 = wx.Button(self, -1, "频率变化")

        self.button9 = wx.Button(self, -1, "拉氏变换到Z变换")

        self.button10 = wx.Button(self, -1, "录音及加噪")
        self.button11 = wx.Button(self, -1, "录音降噪")
        self.button12 = wx.Button(self, -1, "音频加噪")
        self.button13 = wx.Button(self, -1, "傅里叶变换降噪")

        self.button14 = wx.Button(self, -1, "图像加噪")
        self.button15 = wx.Button(self, -1, "加噪2")
        self.button16 = wx.Button(self, -1, "图像去噪")
        self.button17 = wx.Button(self, -1, "图像去噪2")

        self.sizer1.Add(self.button1, -1, wx.SHAPED)
        self.sizer1.Add(self.button2, -1, wx.SHAPED)
        self.sizer1.Add(self.button3, -1, wx.SHAPED)
        self.sizer1.Add(self.button4, -1, wx.SHAPED)

        self.sizer2.Add(self.button5, -1, wx.SHAPED)
        self.sizer2.Add(self.button6, -1, wx.SHAPED)
        self.sizer2.Add(self.button7, -1, wx.SHAPED)

        self.sizer3.Add(self.button8, -1, wx.SHAPED)

        self.sizer4.Add(self.button9, -1, wx.SHAPED)

        self.sizer5.Add(self.button10, -1, wx.SHAPED)
        self.sizer5.Add(self.button11, -1, wx.SHAPED)
        self.sizer5.Add(self.button12, -1, wx.SHAPED)
        self.sizer5.Add(self.button13, -1, wx.SHAPED)

        self.sizer6.Add(self.button14, -1, wx.SHAPED)
        self.sizer6.Add(self.button15, -1, wx.SHAPED)
        self.sizer6.Add(self.button16, -1, wx.SHAPED)
        self.sizer6.Add(self.button17, -1, wx.SHAPED)

        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button2)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button3)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button4)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button5)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button6)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button7)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button8)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button9)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button10)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button11)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button12)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button13)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button14)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button15)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button16)
        self.Bind(wx.EVT_BUTTON, self.OnLaunch, self.button17)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.sizer.Fit(self)
        self.Show(True)

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "此程序为信号与系统动画课程软件系统", "关于此程序")
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close(True)

    def OnLaunch(self, e):
        self.dir_name = ''
        dlg = wx.FileDialog(self, "选择一个程序", self.dir_name, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.file_name = dlg.GetFilename()
            self.dir_name = dlg.GetDirectory()
            win32api.ShellExecute(0, 'open', self.dir_name + '/' + self.file_name, '', '', 1)
            # print(self.dir_name + self.file_name)

        dlg.Destroy()


app = wx.App(False)
frame = MainFrame(None, title="信号与系统动画课程软件")
app.MainLoop()
