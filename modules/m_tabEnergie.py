import pandas as pd
import wx

FONT_NAAM = "TI-Nspire Sans"
KLEUR_TITEL = '#1d99f3'
KLEUR_KOP = '#1d99f3'
KLEUR_GETAL = '#f39c1f'

DF = ''


#
# Tab Energieverbruik
#
class TabEnergie(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._on_clock_timer(None)
        self.update_timer = wx.Timer(self, -1)
        self.update_timer.Start(43242000)  # 7207 (=prime) * 6 = 12 uren
        self.Bind(wx.EVT_TIMER, self._on_clock_timer, self.update_timer)

    def _on_clock_timer(self, event):
        self.updateAll()

    def updateAll(self):
        # Tab leegmaken
        self.DestroyChildren()

        # Letterstijlen
        font_titel = wx.Font(24, wx.NORMAL, wx.NORMAL, wx.BOLD,
                             faceName=FONT_NAAM)
        font_kop = wx.Font(16, wx.NORMAL, wx.NORMAL, wx.BOLD,
                           faceName=FONT_NAAM)
        font_tekst = wx.Font(16, wx.NORMAL, wx.NORMAL, wx.NORMAL,
                             faceName=FONT_NAAM)
        font_tekst_italic = wx.Font(16, wx.NORMAL, wx.ITALIC, wx.NORMAL,
                                    faceName=FONT_NAAM)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        dataSizer = wx.BoxSizer(wx.HORIZONTAL)
        jr2021lSizer = wx.BoxSizer(wx.VERTICAL)
        jr2021rSizer = wx.BoxSizer(wx.VERTICAL)
        jr2021GSizer = wx.BoxSizer(wx.HORIZONTAL)
        jr2021ESizer = wx.BoxSizer(wx.HORIZONTAL)
        jr2021WSizer = wx.BoxSizer(wx.HORIZONTAL)
        jr2022lSizer = wx.BoxSizer(wx.VERTICAL)
        jr2022rSizer = wx.BoxSizer(wx.VERTICAL)
        jr2022GSizer = wx.BoxSizer(wx.HORIZONTAL)
        jr2022ESizer = wx.BoxSizer(wx.HORIZONTAL)
        jr2022WSizer = wx.BoxSizer(wx.HORIZONTAL)
        vrschlSizer = wx.BoxSizer(wx.VERTICAL)
        vrschrSizer = wx.BoxSizer(wx.VERTICAL)
        vrschGSizer = wx.BoxSizer(wx.HORIZONTAL)
        vrschESizer = wx.BoxSizer(wx.HORIZONTAL)
        vrschWSizer = wx.BoxSizer(wx.HORIZONTAL)
        leftSizer = wx.BoxSizer(wx.VERTICAL)
        rightSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Label titel
        titel_energieverbruik = wx.StaticText(self, -1,
                                              label="Energieverbruik 2022")
        titel_energieverbruik.SetFont(font_titel)
        titel_energieverbruik.SetForegroundColour(KLEUR_TITEL)
        topSizer.Add(titel_energieverbruik, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Databestand laden in Pandas dataframe
        try:
            global DF
            DF = pd.read_csv("data/energie_hubrpi.csv")
        except:
            print("Kan data/energie_hubrpi.csv niet openen.")

        # 2021
        label2021 = wx.StaticText(self, -1, label="2021")
        label2021.SetFont(font_kop)
        label2021.SetForegroundColour(KLEUR_KOP)
        lGas1 = wx.StaticText(self, -1, label="gas ")
        lGas1.SetFont(font_tekst)
        lGas_2021 = wx.StaticText(self, -1, label="{}".format(
            str(DF['vrbr_2021'][0])))
        lGas_2021.SetFont(font_tekst)
        lGas_2021.SetForegroundColour(KLEUR_GETAL)
        lGas_hoev = wx.StaticText(self, -1, label=" m3")
        lGas_hoev.SetFont(font_tekst)
        lEle1 = wx.StaticText(self, -1, label="elektriciteit ")
        lEle1.SetFont(font_tekst)
        lEle_2021 = wx.StaticText(self, -1, label="{}".format(
            str(DF['vrbr_2021'][1])))
        lEle_2021.SetFont(font_tekst)
        lEle_2021.SetForegroundColour(KLEUR_GETAL)
        lEle_hoev = wx.StaticText(self, -1, label=" kWh")
        lEle_hoev.SetFont(font_tekst)
        lWat1 = wx.StaticText(self, -1, label="water ")
        lWat1.SetFont(font_tekst)
        lWat_2021 = wx.StaticText(self, -1, label="{}".format(
            str(DF['vrbr_2021'][2])))
        lWat_2021.SetFont(font_tekst)
        lWat_2021.SetForegroundColour(KLEUR_GETAL)
        lWat_hoev = wx.StaticText(self, -1, label=" m3")
        lWat_hoev.SetFont(font_tekst)
        jr2021lSizer.Add(label2021, 0, wx.ALL, 5)
        jr2021GSizer.Add(lGas1, 0, wx.ALL, 0)
        jr2021GSizer.Add(lGas_2021, 0, wx.ALL, 0)
        jr2021GSizer.Add(lGas_hoev, 0, wx.ALL, 0)
        jr2021rSizer.Add(jr2021GSizer, 0, wx.ALL, 0)
        jr2021ESizer.Add(lEle1, 0, wx.ALL, 0)
        jr2021ESizer.Add(lEle_2021, 0, wx.ALL, 0)
        jr2021ESizer.Add(lEle_hoev, 0, wx.ALL, 0)
        jr2021rSizer.Add(jr2021ESizer, 0, wx.ALL, 0)
        jr2021WSizer.Add(lWat1, 0, wx.ALL, 0)
        jr2021WSizer.Add(lWat_2021, 0, wx.ALL, 0)
        jr2021WSizer.Add(lWat_hoev, 0, wx.ALL, 0)
        jr2021rSizer.Add(jr2021WSizer, 0, wx.ALL, 0)
        leftSizer.Add(jr2021lSizer, 1, wx.ALL, 5)
        rightSizer.Add(jr2021rSizer, 1, wx.ALL, 5)

        # 2022
        label2022 = wx.StaticText(self, -1, label="2022")
        label2022.SetFont(font_kop)
        label2022.SetForegroundColour(KLEUR_KOP)
        lGas2 = wx.StaticText(self, -1, label="gas ")
        lGas2.SetFont(font_tekst)
        lGas_2022 = wx.StaticText(self, -1, label="{}".format(
            str(DF['sch_2022'][0])))
        lGas_2022.SetFont(font_tekst)
        lGas_2022.SetForegroundColour(KLEUR_GETAL)
        lGas_hoev = wx.StaticText(self, -1, label=" m3")
        lGas_hoev.SetFont(font_tekst)
        lEle2 = wx.StaticText(self, -1, label="elektriciteit ")
        lEle2.SetFont(font_tekst)
        lEle_2022 = wx.StaticText(self, -1, label="{}".format(
            str(DF['sch_2022'][1])))
        lEle_2022.SetFont(font_tekst)
        lEle_2022.SetForegroundColour(KLEUR_GETAL)
        lEle_hoev = wx.StaticText(self, -1, label=" kWh")
        lEle_hoev.SetFont(font_tekst)
        lWat2 = wx.StaticText(self, -1, label="water ")
        lWat2.SetFont(font_tekst)
        lWat_2022 = wx.StaticText(self, -1, label="{}".format(
            str(DF['sch_2022'][2])))
        lWat_2022.SetFont(font_tekst)
        lWat_2022.SetForegroundColour(KLEUR_GETAL)
        lWat_hoev = wx.StaticText(self, -1, label=" m3")
        lWat_hoev.SetFont(font_tekst)
        jr2022lSizer.Add(label2022, 0, wx.ALL, 5)
        jr2022GSizer.Add(lGas2, 0, wx.ALL, 0)
        jr2022GSizer.Add(lGas_2022, 0, wx.ALL, 0)
        jr2022GSizer.Add(lGas_hoev, 0, wx.ALL, 0)
        jr2022rSizer.Add(jr2022GSizer, 0, wx.ALL, 0)
        jr2022ESizer.Add(lEle2, 0, wx.ALL, 0)
        jr2022ESizer.Add(lEle_2022, 0, wx.ALL, 0)
        jr2022ESizer.Add(lEle_hoev, 0, wx.ALL, 0)
        jr2022rSizer.Add(jr2022ESizer, 0, wx.ALL, 0)
        jr2022WSizer.Add(lWat2, 0, wx.ALL, 0)
        jr2022WSizer.Add(lWat_2022, 0, wx.ALL, 0)
        jr2022WSizer.Add(lWat_hoev, 0, wx.ALL, 0)
        jr2022rSizer.Add(jr2022WSizer, 0, wx.ALL, 0)
        leftSizer.Add(jr2022lSizer, 1, wx.ALL, 5)
        rightSizer.Add(jr2022rSizer, 1, wx.ALL, 5)

        # Verschil
        labelVrsch = wx.StaticText(self, -1, label="Verschil")
        labelVrsch.SetFont(font_kop)
        labelVrsch.SetForegroundColour(KLEUR_KOP)
        lGas3 = wx.StaticText(self, -1, label="gas ")
        lGas3.SetFont(font_tekst)
        lGas_vrsch = wx.StaticText(self, -1, label="{}".format(
            str(DF['vrsch_vrbr'][0])))
        lGas_vrsch.SetFont(font_tekst)
        lGas_vrsch.SetForegroundColour(KLEUR_GETAL)
        lGas_cent1 = wx.StaticText(self, -1, label=" m3")
        lGas_cent1.SetFont(font_tekst)
        lGas_cent2 = wx.StaticText(self, -1, label="[ € ")
        lGas_cent2.SetFont(font_tekst_italic)
        lGas_vbedr = wx.StaticText(self, -1, label="{}".format(
            str(DF['vrsch_bedr'][0])))
        lGas_vbedr.SetFont(font_tekst_italic)
        lGas_vbedr.SetForegroundColour(KLEUR_GETAL)
        lGas_vcent = wx.StaticText(self, -1, label=" @ ")
        lGas_vcent.SetFont(font_tekst_italic)
        lGas_tar = wx.StaticText(self, -1, label="{}".format(
            str(DF['tar'][0])))
        lGas_tar.SetFont(font_tekst_italic)
        lGas_tar.SetForegroundColour(KLEUR_GETAL)
        lGas_vend = wx.StaticText(self, -1, label=" / m3 ]")
        lGas_vend.SetFont(font_tekst_italic)
        lEle3 = wx.StaticText(self, -1, label="elektriciteit ")
        lEle3.SetFont(font_tekst)
        lEle_vrsch = wx.StaticText(self, -1, label="{}".format(
            str(DF['vrsch_vrbr'][1])))
        lEle_vrsch.SetFont(font_tekst)
        lEle_vrsch.SetForegroundColour(KLEUR_GETAL)
        lEle_cent1 = wx.StaticText(self, -1, label=" kWh")
        lEle_cent1.SetFont(font_tekst)
        lEle_cent2 = wx.StaticText(self, -1, label=" [ € ")
        lEle_cent2.SetFont(font_tekst_italic)
        lEle_vbedr = wx.StaticText(self, -1, label="{}".format(
            str(DF['vrsch_bedr'][1])))
        lEle_vbedr.SetFont(font_tekst_italic)
        lEle_vbedr.SetForegroundColour(KLEUR_GETAL)
        lEle_vcent = wx.StaticText(self, -1, label=" @ ")
        lEle_vcent.SetFont(font_tekst_italic)
        lEle_tar = wx.StaticText(self, -1, label="{}".format(
            str(DF['tar'][1])))
        lEle_tar.SetFont(font_tekst_italic)
        lEle_tar.SetForegroundColour(KLEUR_GETAL)
        lEle_vend = wx.StaticText(self, -1, label=" / kWh ]")
        lEle_vend.SetFont(font_tekst_italic)
        lWat3 = wx.StaticText(self, -1, label="water ")
        lWat3.SetFont(font_tekst)
        lWat_vrsch = wx.StaticText(self, -1, label="{}".format(
            str(DF['vrsch_vrbr'][2])))
        lWat_vrsch.SetFont(font_tekst)
        lWat_vrsch.SetForegroundColour(KLEUR_GETAL)
        lWat_cent1 = wx.StaticText(self, -1, label=" m3")
        lWat_cent1.SetFont(font_tekst)
        lWat_cent2 = wx.StaticText(self, -1, label=" [ € ")
        lWat_cent2.SetFont(font_tekst_italic)
        lWat_vbedr = wx.StaticText(self, -1, label="{}".format(
            str(DF['vrsch_bedr'][2])))
        lWat_vbedr.SetFont(font_tekst_italic)
        lWat_vbedr.SetForegroundColour(KLEUR_GETAL)
        lWat_vcent = wx.StaticText(self, -1, label=" @ ")
        lWat_vcent.SetFont(font_tekst_italic)
        lWat_tar = wx.StaticText(self, -1, label="{}".format(
            str(DF['tar'][2])))
        lWat_tar.SetFont(font_tekst_italic)
        lWat_tar.SetForegroundColour(KLEUR_GETAL)
        lWat_vend = wx.StaticText(self, -1, label=" / m3 ]")
        lWat_vend.SetFont(font_tekst_italic)

        vrschlSizer.Add(labelVrsch, 0, wx.ALL, 5)
        vrschGSizer.Add(lGas3, 0, wx.ALL, 0)
        vrschGSizer.Add(lGas_vrsch, 0, wx.ALL, 0)
        vrschGSizer.Add(lGas_cent1, 0, wx.ALL, 0)
        vrschGSizer.Add(lGas_cent2, 0, wx.ALL, 0)
        vrschGSizer.Add(lGas_vbedr, 0, wx.ALL, 0)
        vrschGSizer.Add(lGas_vcent, 0, wx.ALL, 0)
        vrschGSizer.Add(lGas_tar, 0, wx.ALL, 0)
        vrschGSizer.Add(lGas_vend, 0, wx.ALL, 0)
        vrschrSizer.Add(vrschGSizer, 0, wx.ALL, 0)
        vrschESizer.Add(lEle3, 0, wx.ALL, 0)
        vrschESizer.Add(lEle_vrsch, 0, wx.ALL, 0)
        vrschESizer.Add(lEle_cent1, 0, wx.ALL, 0)
        vrschESizer.Add(lEle_cent2, 0, wx.ALL, 0)
        vrschESizer.Add(lEle_vbedr, 0, wx.ALL, 0)
        vrschESizer.Add(lEle_vcent, 0, wx.ALL, 0)
        vrschESizer.Add(lEle_tar, 0, wx.ALL, 0)
        vrschESizer.Add(lEle_vend, 0, wx.ALL, 0)
        vrschrSizer.Add(vrschESizer, 0, wx.ALL, 0)
        vrschWSizer.Add(lWat3, 0, wx.ALL, 0)
        vrschWSizer.Add(lWat_vrsch, 0, wx.ALL, 0)
        vrschWSizer.Add(lWat_cent1, 0, wx.ALL, 0)
        vrschWSizer.Add(lWat_cent2, 0, wx.ALL, 0)
        vrschWSizer.Add(lWat_vbedr, 0, wx.ALL, 0)
        vrschWSizer.Add(lWat_vcent, 0, wx.ALL, 0)
        vrschWSizer.Add(lWat_tar, 0, wx.ALL, 0)
        vrschWSizer.Add(lWat_vend, 0, wx.ALL, 0)
        vrschrSizer.Add(vrschWSizer, 0, wx.ALL, 0)
        leftSizer.Add(vrschlSizer, 1, wx.ALL, 5)
        rightSizer.Add(vrschrSizer, 1, wx.ALL, 5)

        # Toevoegen aan sizer
        dataSizer.Add(leftSizer, 0, wx.EXPAND | wx.ALL, 5)
        dataSizer.Add(rightSizer, 1, wx.EXPAND | wx.ALL, 5)
        mainSizer.Add(dataSizer, 1, wx.ALL, 10)
        self.SetSizerAndFit(mainSizer)
        self.Layout()
