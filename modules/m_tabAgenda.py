import wx
import wx.adv
import caldav
from datetime import datetime
import pytz
from dateutil.relativedelta import relativedelta


FONT_NAAM = "IBM Plex Sans"
KLEUR_DAG = '#1d99f3'
KLEUR_MAAND = '#1cdc9a'
KLEUR_TIJD = '#f39c1f'

# Gegevens van caldav-url, gebruikersnaam en wachtwoord
caldav_url = 'caldav_url'
username = 'username'
password = 'password'

#
# Dictionary van agenda-data
#
agenda_data = {}


#
# Tabblad Agenda
#
class TabAgenda(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._on_clock_timer(None)
        self.update_timer = wx.Timer(self, -1)
        self.update_timer.Start(14422000)  # 7211 (=prime) * 2 = vier uur
        self.Bind(wx.EVT_TIMER, self._on_clock_timer, self.update_timer)

    def _on_clock_timer(self, event):
        self.updateAll()

    def updateAll(self):
        # Tab leegmaken
        self.DestroyChildren()
        # Synchroniseer kalenderdata
        syncCalendar()

        # Instellen letterstijlen
        font_titel = wx.Font(24, wx.NORMAL, wx.NORMAL, wx.BOLD,
                             faceName=FONT_NAAM)
        font_dag = wx.Font(16, wx.NORMAL, wx.NORMAL, wx.BOLD,
                           faceName=FONT_NAAM)
        font_maand = wx.Font(18, wx.NORMAL, wx.NORMAL, wx.BOLD,
                             faceName=FONT_NAAM)
        font_tijd = wx.Font(18, wx.NORMAL, wx.NORMAL, wx.NORMAL,
                            faceName=FONT_NAAM)
        font_descr = wx.Font(18, wx.NORMAL, wx.NORMAL, wx.BOLD,
                             faceName=FONT_NAAM)

        # Vandaag en morgen datetime
        vandaag = datetime.today()
        morgen = vandaag + relativedelta(days=1)

        # Sizers initialiseren
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        contentSizer = wx.BoxSizer(wx.HORIZONTAL)
        rechtsSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Label vandaag
        label_vandaag = wx.StaticText(self, -1, label="{}".format(
            vandaag.strftime("%A %d %B %Y")))
        label_vandaag.SetFont(font_titel)
        label_vandaag.SetForegroundColour(KLEUR_DAG)
        topSizer.Add(label_vandaag, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        #
        # Gegevens van agenda ordenen en weergeven
        #
        kalender = wx.TextCtrl(self, -1, value="",
                               style=wx.TE_RICH | wx.TE_READONLY | wx.TE_MULTILINE)
        prev_date = 0
        maand = vandaag.month

        for event in agenda_data:
            # Starttijd
            estart = str(agenda_data[event][0].strftime("%H:%M"))

            # Omschrijving
            edescr = agenda_data[event][2]
            event_descr = "\t{}\n".format(str(edescr))

            # Afhankelijk van eindtijd op dezelfde of latere dag een andere
            # presentatie in string
            if agenda_data[event][0].day == agenda_data[event][1].day:
                eindtijd = "%H:%M"
            else:
                eindtijd = "%H:%M (%d/%m)"
            eeinde = str(agenda_data[event][1].strftime(eindtijd))
            # Weergave 'hele dag' bij dagevenement
            if agenda_data[event][3]:
                event_tijd = "\thele dag\n"
            else:
                event_tijd = "\t{} - {}\n".format(estart, eeinde)

            edatum = agenda_data[event][0].date()
            if edatum.month != maand:
                maand = edatum.month
                nieuwe_maand = str(agenda_data[event][0].strftime("%B")).upper()
                str_vullen = 24 - len(nieuwe_maand)
                str_maand = "{} {} {}\n".format('----', nieuwe_maand,
                                                str_vullen*'-')
                kalender.SetDefaultStyle(wx.TextAttr(KLEUR_MAAND, wx.NullColour,
                                                     font_maand))
                kalender.AppendText(str_maand)

            if prev_date == 0 or prev_date != edatum:
                # Weergave dag. Speciale weergave indien 'vandaag' of 'morgen'
                if vandaag.date() == edatum:
                    edag = "vandaag"
                elif morgen.date() == edatum:
                    edag = "morgen"
                else:
                    edag = str(agenda_data[event][0].strftime("%A %d %B"))
                event_dag = "{}\n".format(edag)
                # Toevoegen aan kalender
                kalender.SetDefaultStyle(wx.TextAttr(KLEUR_DAG, wx.NullColour,
                                                     font_dag))
                kalender.AppendText(event_dag)

            kalender.SetDefaultStyle(wx.TextAttr(KLEUR_TIJD, wx.NullColour,
                                                 font_tijd))
            kalender.AppendText(event_tijd)
            kalender.SetDefaultStyle(wx.TextAttr(wx.WHITE, wx.NullColour,
                                                 font_descr))
            kalender.AppendText(event_descr)
            if agenda_data[event][4] != "":
                event_locatie = "\t{}\n".format(agenda_data[event][4])
                kalender.SetDefaultStyle(wx.TextAttr(KLEUR_MAAND, wx.NullColour,
                                                     font_tijd))
                kalender.AppendText(event_locatie)
                #kalender.AppendText("\n")
                # Variabele om te onthouden of er een eerdere dag is behandeld
            prev_date = edatum

        kalgraph = wx.adv.CalendarCtrl(self, -1, date=vandaag, size=(200, 200))

        str_zodiac = "graphics/zodiac/{}.png".format(getZodiacSign())
        zodiac_png = (wx.Image(str_zodiac,
                               wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        zodiac_icon = (wx.StaticBitmap(self, -1, zodiac_png, (140, 140),
                                       (zodiac_png.GetWidth(),
                                        zodiac_png.GetHeight())))

        # Sizers toevoegen
        contentSizer.Add(kalender, 1, wx.EXPAND | wx.ALL, 5)
        rechtsSizer.Add(kalgraph, 0, wx.ALL, 5)
        rechtsSizer.Add(zodiac_icon, 0, wx.ALIGN_CENTER | wx.ALL, 0)
        contentSizer.Add(rechtsSizer, 0, wx.ALL, 5)
        mainSizer.Add(contentSizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        self.Layout()


#
# Synchroniseren van kalenderdata
#
def syncCalendar():
    # Vandaag datetime
    vandaag = datetime.today()
    # Tot aan welke datum synchroniseren datetime
    tot_datum = vandaag + relativedelta(years=1)
    # Try voor geval ophalen data mislukt
    try:
        client = caldav.DAVClient(url=caldav_url, username=username,
                                  password=password)
        my_principal = client.principal()

        # Gevraagde kalender ophalen
        my_calendar = my_principal.calendar(name="DineshJonathan")

        # Opgehaalde events verzamelen
        events_fetched = my_calendar.date_search(start=vandaag, end=tot_datum,
                                                 expand=True)
        temp_data = {}

        # Alle data van events in tijdelijke dictionary
        # Als dit mislukt is oorspronkelijke data behouden
        for event in events_fetched:
            heledag = False
            # starttijd
            ev_dtstart = event.vobject_instance.vevent.dtstart.value
            if len(str(ev_dtstart)) < 11:
                ev_dtstart = datetime.strptime(str(ev_dtstart), '%Y-%m-%d')
                heledag = True
                # starttijd corrigeren tijdzone
            ev_dtstart = ev_dtstart.astimezone(pytz.timezone('Europe/Amsterdam'))
            # eindtijd
            ev_dtend = event.vobject_instance.vevent.dtend.value
            if len(str(ev_dtend)) < 11:
                ev_dtend = datetime.strptime(str(ev_dtend), '%Y-%m-%d')
                ev_dtend = ev_dtend - relativedelta(days=1)
                # eindtijd corrigeren tijdzone
            ev_dtend = ev_dtend.astimezone(pytz.timezone('Europe/Amsterdam'))
            # omschrijving
            ev_summary = event.vobject_instance.vevent.summary.value
            try:
                ev_location = event.vobject_instance.vevent.location.value
            except:
                ev_location = ""
                # inhoud aan item in dictionary toevoegen
            temp_data[ev_dtstart] = (ev_dtstart, ev_dtend, ev_summary, heledag,
                                     ev_location)
            if(heledag):
                while ev_dtstart < ev_dtend:
                    ev_dtstart = ev_dtstart + relativedelta(days=1)
                    temp_data[ev_dtstart] = (ev_dtstart, ev_dtend, ev_summary,
                                             heledag, ev_location)

        agenda_data.clear()
        # Data tijdelijke dictionary kopieren naar dictionary van module
        for i in sorted(temp_data):
            agenda_data[i] = temp_data[i]
    except:
        print("Kan kalender niet updaten.")


#
# Krijg huidige dierenriemteken
#
def getZodiacSign():
    result = ""
    today = datetime.today().date()
    month = today.month
    day = today.day

    if month == 1:
        if day <= 20:
            result = "capricorn"
        else:
            result = "aquarius"
    elif month == 2:
        if day <= 18:
            result = "aquarius"
        else:
            result = "pisces"
    elif month == 3:
        if day <= 20:
            result = "pisces"
        else:
            result = "aries"
    elif month == 4:
        if day <= 19:
            result = "aries"
        else:
            result = "taurus"
    elif month == 5:
        if day <= 20:
            result = "taurus"
        else:
            result = "gemini"
    elif month == 6:
        if day <= 21:
            result = "gemini"
        else:
            result = "cancer"
    elif month == 7:
        if day <= 22:
            result = "cancer"
        else:
            result = "leo"
    elif month == 8:
        if day <= 22:
            result = "leo"
        else:
            result = "virgo"
    elif month == 9:
        if day <= 22:
            result = "virgo"
        else:
            result = "libra"
    elif month == 10:
        if day <= 22:
            result = "libra"
        else:
            result = "scorpio"
    elif month == 11:
        if day <= 21:
            result = "scorpio"
        else:
            result = "sagittarius"
    elif month == 12:
        if day <= 21:
            result = "sagittarius"
        else:
            result = "capricorn"

    return result

