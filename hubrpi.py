#!/usr/bin/env python3
import wx
from modules import m_tabAgenda
from modules import m_tabFortune
from modules import m_tabEle
from modules import m_tabEnergie
from modules import m_tabGas
from modules import m_tabMuziek
from modules import m_tabTools
from modules import m_tabWat
from modules import m_tabWeer
from multiprocessing import Process


# Dictionary van Notebook die tabbladen bijhoudt
dict = {"nb": wx.Notebook}


class hubrpiApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        # init frame
        frame = MyFrame()
        frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, title="Hub Rpi"):
        super().__init__(None, title=title)
        # initialize the frame's contents
        self.InitFrame()

    def InitFrame(self):
        self.panel = MyPanel(self)
        self.SetSize((800, 480))
        self.Fit()


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.InitPanel()
        self._on_clock_timer(None)
        self.update_timer = wx.Timer(self, -1)
        self.update_timer.Start(31000)  # 31 (=prime) ongeveer halve minuut
        self.Bind(wx.EVT_TIMER, self._on_clock_timer, self.update_timer)

    def _on_clock_timer(self, event):
        if m_tabTools.B_ROTATE:
            self.switchTab()

    def StartWeerTab(self):
        tabWeer = m_tabWeer.TabWeer(dict['nb'])
        dict['nb'].AddPage(tabWeer, "Weer")

    def StartAgendaTab(self):
        tabAgenda = m_tabAgenda.TabAgenda(dict['nb'])
        dict['nb'].AddPage(tabAgenda, "Agenda")

    def StartFortuneTab(self):
        tabFortune = m_tabFortune.TabFortune(dict['nb'])
        dict['nb'].AddPage(tabFortune, "Fortune")

    def InitPanel(self):
        # Tabbladen toevoegen aan Notebook
        dict['nb'] = wx.Notebook(self)
        p1 = Process(target=self.StartWeerTab())
        p1.start()
        p2 = Process(target=self.StartAgendaTab())
        p2.start()
        p3 = Process(target=self.StartFortuneTab())
        p3.start()
        # tabWeer = m_tabWeer.TabWeer(dict['nb'])
        # tabAgenda = m_tabAgenda.TabAgenda(dict['nb'])
        # tabFortune = m_tabFortune.TabFortune(dict['nb'])
        tabGas = m_tabGas.TabGas(dict['nb'])
        tabEle = m_tabEle.TabEle(dict['nb'])
        tabWat = m_tabWat.TabWat(dict['nb'])
        tabEnergie = m_tabEnergie.TabEnergie(dict['nb'])
        tabMuziek = m_tabMuziek.TabMuziek(dict['nb'])
        tabTools = m_tabTools.TabTools(dict['nb'])
        p1.join()
        p2.join()
        p3.join()
        # dict['nb'].AddPage(tabWeer, "Weer")
        # dict['nb'].AddPage(tabAgenda, "Agenda")
        # dict['nb'].AddPage(tabFortune, "Fortune")
        dict['nb'].AddPage(tabGas, "Gas")
        dict['nb'].AddPage(tabEle, "Elektriciteit")
        dict['nb'].AddPage(tabWat, "Water")
        dict['nb'].AddPage(tabEnergie, "Energie")
        dict['nb'].AddPage(tabMuziek, "Muziek")
        dict['nb'].AddPage(tabTools, "Tools")
        # Laatste 'wissel'tab instellen, zodat app bij openen netjes
        # de eerste tab selecteert ;-)
        dict['nb'].ChangeSelection(2)

        # Sizers initialiseren
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        centerSizer = wx.BoxSizer()
        centerSizer.Add(dict['nb'], 1, wx.EXPAND)
        mainSizer.Add(centerSizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        self.Layout()

    # Wisselen van tabblad
    def switchTab(self):
        selected_page = dict['nb'].GetSelection()
        new_page = 0
        # Automatisch roteren bij selectie van eerste drie tabbladen
        if selected_page < 3:
            if selected_page < 2:
                new_page = selected_page + 1
            dict['nb'].ChangeSelection(new_page)


# Hoofdcode van app starten
if __name__ == "__main__":
    app = hubrpiApp()
    app.MainLoop()
