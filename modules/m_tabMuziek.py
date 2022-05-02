import wx
import psutil
import subprocess

FONT_NAAM = "IBM Plex Sans"
FONT_NAAM_TXT = "IBM Plex Sans"
KLEUR_TITEL = '#1d99f3'

music_items = {0: "keygenfm",
               1: "radiocaprice",
               2: "radiomontecarlo",
               3: "kisskissradio",
               4: "musicforcats",
               5: "milindchittal",
               6: "ancientbeautyoftheveena",
               7: "bansuri",
               8: "divali",
               9: "surajitdas",
               10: "amorfm",
               11: "divinecomedy",
               12: "bluestrash",
               13: "reverend"}
PID = 0


#
# Tab Muziek
#
class TabMuziek(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.updateAll()
        self._on_clock_timer(None)
        self.update_timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self._on_clock_timer, self.update_timer)

    # Stop met spelen als termijn verstreken
    def _on_clock_timer(self, event):
        self.StopMuziek(lambda event: self.StopMuziek(event, PID), PID)

    def updateAll(self):
        self.DestroyChildren()
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        centerSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer = wx.GridBagSizer(2, 2)
        # Letterstijlen
        font_titel = wx.Font(24, wx.NORMAL, wx.NORMAL, wx.BOLD,
                             faceName=FONT_NAAM)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(topSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        label_muziek = wx.StaticText(self, -1, label="Muziek")
        label_muziek.SetFont(font_titel)
        label_muziek.SetForegroundColour(KLEUR_TITEL)
        topSizer.Add(label_muziek, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Knoppen voor muziekitems maken
        for i in range(len(music_items)):
            if i < 5:
                row = 0
                col = i
            elif i < 10:
                row = 1
                col = i - 5
            else:
                row = 2
                col = i - 10
            bmpNaam = "graphics/{}.bmp".format(music_items[i])
            bitmap_item = wx.Bitmap(bmpNaam)
            itemBtn = wx.BitmapButton(self, -1, bitmap_item, (100, 100))
            shNaam = "muziek/{}.sh".format(music_items[i])
            itemBtn.Bind(wx.EVT_BUTTON,
                         lambda event, temp=shNaam: self.PlayMuziek(
                             event, PID, temp))
            buttonSizer.Add(itemBtn, flag=wx.ALL, pos=(row, col), border=2)

        # Stopknop
        stopBtn = wx.Button(self, -1, label="Stop muziek", size=(100, 100))
        stopBtn.Bind(wx.EVT_BUTTON,
                     lambda event: self.StopMuziek(event, PID))
        if PID == 0:
            stopBtn.Disable()
        buttonSizer.Add(stopBtn, flag=wx.ALIGN_CENTER | wx.ALL,
                        pos=(2, 4), border=5)

        centerSizer.Add(buttonSizer, 1, wx.EXPAND | wx.ALL, 5)
        mainSizer.Add(centerSizer, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        self.Layout()

    # Speel muziek
    def PlayMuziek(self, e, procID, command):
        try:
            if procID == 0:
                process = subprocess.Popen(command)
                global PID
                PID = process.pid
                self.update_timer.Start(14426000)  # 7213 (=prime) = 4 uren
        except:
            pass
        self.updateAll()

    # Stop muziek
    def StopMuziek(self, e, procID):
        if procID != 0:
            parent = psutil.Process(procID)
            for child in parent.children(recursive=True):
                child.kill()
            global PID
            PID = 0
        self.updateAll()
