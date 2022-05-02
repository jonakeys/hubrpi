import wx
from fortunate import Fortunate

FONT_NAAM = "IBM Plex Sans"
FONT_NAAM_TXT = "IBM Plex Serif"
KLEUR_TITEL = '#1d99f3'


#
# Tab Fortune
#
class TabFortune(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._on_clock_timer(None)
        self.update_timer = wx.Timer(self, -1)
        self.update_timer.Start(7219000)  # 7219 (=prime) = 2 uur
        self.Bind(wx.EVT_TIMER, self._on_clock_timer, self.update_timer)

    def _on_clock_timer(self, event):
        self.updateAll()

    # Volgende fortune oproepen
    def onClick(self, event):
        self.updateAll()

    def updateAll(self):
        # Tab leegmaken
        self.DestroyChildren()

        # Letterstijlen
        font_titel = wx.Font(24, wx.NORMAL, wx.NORMAL, wx.BOLD,
                             faceName=FONT_NAAM)
        font_tekst = wx.Font(16, wx.NORMAL, wx.NORMAL, wx.NORMAL,
                             faceName=FONT_NAAM_TXT)

        # Sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        centerSizer = wx.BoxSizer(wx.VERTICAL)
        bottomSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(topSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Label titel Fortune
        label_fortune = wx.StaticText(self, -1, label="Fortune")
        label_fortune.SetFont(font_titel)
        label_fortune.SetForegroundColour(KLEUR_TITEL)
        topSizer.Add(label_fortune, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Willekeurige fortune uit bestand laden
        str_fortune = ""
        generator = Fortunate('data/fortune.u8')
        # Eerst keer gaat altijd fout (fout module 'fortunate'?...)
        try:
            test = generator()
        except:
            pass
        try:
            str_fortune = generator()
        except:
            print("Kan Fortune niet vernieuwen.")

        # Fortune toevoegen aan TextCtrl
        fortune_tekst = wx.TextCtrl(self, -1, value="{}".format(str_fortune),
                                    style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH)
        fortune_tekst.SetFont(font_tekst)

        # Toevoegen aan sizer
        centerSizer.Add(fortune_tekst, 1, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(centerSizer, 1, wx.EXPAND | wx.ALL, 5)

        # Knop om volgende fortune op te roepen
        refreshBtn = wx.Button(self, -1, label="Volgende fortune",
                               size=(150, 60))
        refreshBtn.Bind(wx.EVT_BUTTON, self.onClick)
        bottomSizer.Add(refreshBtn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Sizers
        mainSizer.Add(bottomSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        self.Layout()
