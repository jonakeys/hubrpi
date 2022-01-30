import wx


#
# Tab Water
#
class TabWat(wx.Panel):
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
        bestandsnaam = "graphics/waterverbruik.png"

        # Elektriciteitsverbruikplaatje laden
        wat_bmp = (wx.Image(bestandsnaam,
                            wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        waterverbruik_bmp = (wx.StaticBitmap(self, -1, wat_bmp))

        # Sizer en plaatje toevoegen
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(waterverbruik_bmp, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        self.Layout()
