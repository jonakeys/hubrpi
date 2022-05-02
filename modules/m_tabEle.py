import wx

FONT_NAAM = "IBM Plex Sans"
FONT_NAAM_TXT = "IBM Plex Sans"
KLEUR_TITEL = '#1d99f3'


#
# Tab Elektriciteit
#
class TabEle(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._on_clock_timer(None)
        self.update_timer = wx.Timer(self, -1)
        self.update_timer.Start(43242000)  # 7207 (=prime) * 6 = 12 uren
        self.Bind(wx.EVT_TIMER, self._on_clock_timer, self.update_timer)

    def _on_clock_timer(self, event):
        self.updateAll()

    def updateAll(self):
        self.DestroyChildren()
        bestandsnaam = "graphics/elektriciteitsverbruik.png"
        # Letterstijlen
        font_titel = wx.Font(24, wx.NORMAL, wx.NORMAL, wx.BOLD,
                             faceName=FONT_NAAM)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(topSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        label_ele = wx.StaticText(self, -1, label="Elektriciteit")
        label_ele.SetFont(font_titel)
        label_ele.SetForegroundColour(KLEUR_TITEL)
        topSizer.Add(label_ele, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Elektriciteitsverbruikplaatje laden
        ele_bmp = (wx.Image(bestandsnaam,
                            wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        elektriciteitsverbruik_bmp = (wx.StaticBitmap(self, -1, ele_bmp))

        # Sizer en plaatje toevoegen
        mainSizer.Add(elektriciteitsverbruik_bmp, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        self.Layout()
