import wx

B_ROTATE = True
FONT_NAAM = "TI-Nspire Sans"
KLEUR_TITEL = '#1d99f3'


class TabTools(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.updateAll()

    def updateAll(self):
        self.DestroyChildren()

        # Letterstijlen
        font_titel = wx.Font(24, wx.NORMAL, wx.NORMAL, wx.BOLD,
                             faceName=FONT_NAAM)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Label titel
        label_titel = wx.StaticText(self, -1, label="Tools")
        label_titel.SetFont(font_titel)
        label_titel.SetForegroundColour(KLEUR_TITEL)
        topSizer.Add(label_titel, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Afsluiten app
        exitBtn = wx.Button(self, wx.ID_EXIT, label="Afsluiten", size=(150, 60))
        exitBtn.Bind(wx.EVT_BUTTON, self.OnExit)
        buttonSizer.Add(exitBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        # Roteren tabs in- of uitschakelen
        if B_ROTATE:
            btnLabel = "Stop loop"
        else:
            btnLabel = "Start loop"
        rotateBtn = wx.Button(self, -1, label=btnLabel, size=(150, 60))
        rotateBtn.Bind(wx.EVT_BUTTON, self.OnRotate)
        buttonSizer.Add(rotateBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        mainSizer.Add(buttonSizer, 1, wx.EXPAND | wx.ALL, 15)
        self.SetSizerAndFit(mainSizer)
        self.Layout()

    def OnExit(self, e):
        wx.Exit()

    def OnRotate(self, e):
        global B_ROTATE
        B_ROTATE = not B_ROTATE
        self.updateAll()
