import wx
import requests

FONT_NAAM = "IBM Plex Sans"
KLEUR_DAG = '#1d99f3'
KLEUR_COND = '#1cdc9a'
KLEUR_TEMP = '#f67400'
KLEUR_TEMP_MM = '#f39c1f'

# Enter the api key of openweathermap here
api_key = "api_key"
# Base url for the open map api
root_url = "https://api.openweathermap.org/data/2.5/onecall?"
# Latitude and longitude of location
lat = 53.000000
lon = 6.000000
# Units
units = "metric"
# Language
language = "nl"

#
# Dictionary van weergegevens
#
weer_data = {"curr_dt": 0,
             "curr_icoon": "",
             "curr_conditie": "",
             "curr_temperatuur": 0,
             "curr_temp_min": 0,
             "curr_temp_max": 0,
             "curr_luchtdruk": 0,
             "curr_luchtvochtigheid": 0,
             "curr_windsnelheid": 0,
             "curr_kans_neerslag": 0,
             "curr_regen_mm": 0,
             "curr_sneeuw_mm": 0,
             "day1_dt": 0,
             "day1_icoon": "",
             "day1_conditie": "",
             "day1_temp_dag": 0,
             "day1_temp_min": 0,
             "day1_temp_max": 0,
             "day1_kans_neerslag": 0,
             "day1_regen_mm": 0,
             "day1_sneeuw_mm": 0,
             "day2_dt": 0,
             "day2_icoon": "",
             "day2_conditie": "",
             "day2_temp_dag": 0,
             "day2_temp_min": 0,
             "day2_temp_max": 0,
             "day2_kans_neerslag": 0,
             "day2_regen_mm": 0,
             "day2_sneeuw_mm": 0}


#
# Tabblad Weer
#
class TabWeer(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self._on_clock_timer(None)
        self.update_timer = wx.Timer(self, -1)
        self.update_timer.Start(3581000)  # 3581 (=prime) = 1 uur
        self.Bind(wx.EVT_TIMER, self._on_clock_timer, self.update_timer)

    def _on_clock_timer(self, event):
        requestWeather()
        self.updateAll()

    def updateAll(self):
        # Maak tab leeg
        self.DestroyChildren()

        # Letterstijlen opmaken
        font_head = wx.Font(24, wx.NORMAL, wx.NORMAL, wx.BOLD,
                            faceName=FONT_NAAM)
        font_curr = wx.Font(16, wx.NORMAL, wx.NORMAL, wx.BOLD,
                            faceName=FONT_NAAM)
        font_days_bold = wx.Font(14, wx.NORMAL, wx.NORMAL, wx.BOLD,
                                 faceName=FONT_NAAM)
        font_days_normal = wx.Font(14, wx.NORMAL, wx.NORMAL, wx.NORMAL,
                                   faceName=FONT_NAAM)

        # PNG's weericonen (huidige en komende twee dagen)
        str_curr_icon = "graphics/VClouds_weather_icons/current/{}.png"\
            .format(weer_data["curr_icoon"])
        curr_png = (wx.Image(str_curr_icon,
                             wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        str_day1_icon = "graphics/VClouds_weather_icons/days/{}.png"\
            .format(weer_data["day1_icoon"])
        day1_png = (wx.Image(str_day1_icon,
                             wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        str_day2_icon = "graphics/VClouds_weather_icons/days/{}.png"\
            .format(weer_data["day2_icoon"])
        day2_png = (wx.Image(str_day2_icon,
                             wx.BITMAP_TYPE_ANY).ConvertToBitmap())

        # Initialiseren sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        northSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer = wx.StaticBoxSizer(wx.VERTICAL, self, "Vandaag")
        zeroSizer = wx.BoxSizer(wx.HORIZONTAL)
        currLSizer = wx.BoxSizer(wx.VERTICAL)
        currMSizer = wx.BoxSizer(wx.VERTICAL)
        currRSizer = wx.BoxSizer(wx.VERTICAL)
        day1Sizer = wx.BoxSizer(wx.VERTICAL)
        day2Sizer = wx.BoxSizer(wx.VERTICAL)

        #
        # Iconen en data huidige en komende twee dagen
        #
        # Weericoon huidige dag
        curr_icoon = (wx.StaticBitmap(self, -1, curr_png, (10, 5),
                                      (curr_png.GetWidth(),
                                       curr_png.GetHeight())))
        # Huidige weekdag
        curr_weekdag = weer_data["curr_dt"].GetWeekDay()
        # Huidige maand
        curr_maand = weer_data["curr_dt"].GetMonth()
        # Samenvoegen datum, dag en maand
        curr_dt = wx.StaticText(self, -1,
            label="{weekdag} {dag} {maand} {jaar}".format(
            weekdag=str(wx.DateTime.GetWeekDayName(curr_weekdag)),
            dag=str(weer_data["curr_dt"].GetDay()),
            maand=str(wx.DateTime.GetMonthName(curr_maand)),
            jaar=str(weer_data["curr_dt"].GetYear())))
        curr_dt.SetForegroundColour(KLEUR_DAG)
        # Label huidige weerconditie
        curr_cond = wx.StaticText(self, -1, label="{}".format(
            weer_data["curr_conditie"]))
        curr_cond.SetForegroundColour(KLEUR_COND)
        # Label huidige temperatuur
        curr_temp = wx.StaticText(self, -1, label="{} \u00b0C".format(
            str(weer_data["curr_temperatuur"])))
        curr_temp.SetForegroundColour(KLEUR_TEMP)
        # Label huidige minimale en maximale temperatuur
        curr_min_max = wx.StaticText(self, -1,
            label="{} \u00b0 / {} \u00b0".format(
                str(weer_data["curr_temp_min"]),
                str(weer_data["curr_temp_max"])))
        curr_min_max.SetForegroundColour(KLEUR_TEMP_MM)
        # Label huidige luchtdruk
        curr_druk = wx.StaticText(self, -1, label="{} hPa".format(
            str(weer_data["curr_luchtdruk"])))
        # Label huidige luchtvochtigheid
        curr_voch = wx.StaticText(self, -1, label="{} %".format(
            str(weer_data["curr_luchtvochtigheid"])))
        # Label huidige windsnelheid
        curr_snel = wx.StaticText(self, -1, label="{} m/s".format(
            str(weer_data["curr_windsnelheid"])))
        # Label huidige kans op neerslag
        curr_kans_neerslag = wx.StaticText(self, -1, label="{} %".format(
            str(weer_data["curr_kans_neerslag"])))
        # Label huidige regen (neerslag)
        curr_regen_mm = wx.StaticText(self, -1, label="{} mm (r)".format(
            str(weer_data["curr_regen_mm"])))
        # Label huidige sneeuw (neerslag)
        curr_sneeuw_mm = wx.StaticText(self, -1, label="{} mm (s)".format(
            str(weer_data["curr_sneeuw_mm"])))

        # Weekdag dag 1
        day1_weekdag = weer_data["day1_dt"].GetWeekDay()
        # Label van weekdag 1
        day1_dt = wx.StaticText(self, -1, label="{}".format(
            str(wx.DateTime.GetWeekDayName(day1_weekdag))))
        day1_dt.SetForegroundColour(KLEUR_DAG)
        # Weericoon dag 1
        day1_icoon = (wx.StaticBitmap(self, -1, day1_png, (10, 5),
                                      (day1_png.GetWidth(),
                                       day1_png.GetHeight())))
        # Label weerconditie dag 1
        day1_cond = wx.StaticText(self, -1, label="{}".format(
            weer_data["day1_conditie"]))
        day1_cond.SetForegroundColour(KLEUR_COND)
        # Label dagtemperatuur dag 1
        day1_temp_dag = wx.StaticText(self, -1, label="{} \u00b0C".format(
            str(weer_data["day1_temp_dag"])))
        day1_temp_dag.SetForegroundColour(KLEUR_TEMP)
        # Label minmale en maximale temperatuur dag 1
        day1_min_max = wx.StaticText(self, -1,
            label="{}  \u00b0 / {} \u00b0".format(
            str(weer_data["day1_temp_min"]), str(weer_data["day1_temp_max"])))
        day1_min_max.SetForegroundColour(KLEUR_TEMP_MM)
        # Label kans op neerslag dag 1
        day1_kans_neerslag = wx.StaticText(self, -1, label="{} %".format(
            str(weer_data["day1_kans_neerslag"])))
        # Label regen (neerslag) dag 1
        day1_regen_mm = wx.StaticText(self, -1, label="{} mm (r)".format(
            str(weer_data["day1_regen_mm"])))
        # Label sneeuw (neerslag) dag 1
        day1_sneeuw_mm = wx.StaticText(self, -1, label="{} mm (s)".format(
            str(weer_data["day1_sneeuw_mm"])))

        # Weekdag dag 2
        day2_weekdag = weer_data["day2_dt"].GetWeekDay()
        day2_dt = wx.StaticText(self, -1, label="{}".format(
            str(wx.DateTime.GetWeekDayName(day2_weekdag))))
        day2_dt.SetForegroundColour(KLEUR_DAG)
        # Weericoon dag 2
        day2_icoon = (wx.StaticBitmap(self, -1, day2_png, (10, 5),
                                      (day2_png.GetWidth(),
                                       day2_png.GetHeight())))
        # Label weerconditie dag 2
        day2_cond = wx.StaticText(self, -1, label="{}".format(
            weer_data["day2_conditie"]))
        day2_cond.SetForegroundColour(KLEUR_COND)
        # Label dagtemperatuur dag 2
        day2_temp_dag = wx.StaticText(self, -1, label="{} \u00b0C".format(
            str(weer_data["day2_temp_dag"])))
        day2_temp_dag.SetForegroundColour(KLEUR_TEMP)
        # Label minimale en maximale temperatuur dag 2
        day2_min_max = wx.StaticText(self, -1,
            label="{} \u00b0 / {} \u00b0".format(
            str(weer_data["day2_temp_min"]), str(weer_data["day2_temp_max"])))
        day2_min_max.SetForegroundColour(KLEUR_TEMP_MM)
        # Label kans op neerslag dag 2
        day2_kans_neerslag = wx.StaticText(self, -1, label="{} %".format(
            str(weer_data["day2_kans_neerslag"])))
        # Label regen (neerslag) dag 2
        day2_regen_mm = wx.StaticText(self, -1, label="{} mm (r)".format(
            str(weer_data["day2_regen_mm"])))
        # Label sneeuw (neerslag) dag 2
        day2_sneeuw_mm = wx.StaticText(self, -1, label="{} mm (s)".format(
            str(weer_data["day2_sneeuw_mm"])))

        #
        # Instellen lettertypen van labels
        #
        curr_dt.SetFont(font_head)
        curr_cond.SetFont(font_curr)
        curr_temp.SetFont(font_curr)
        curr_min_max.SetFont(font_curr)
        curr_druk.SetFont(font_curr)
        curr_voch.SetFont(font_curr)
        curr_snel.SetFont(font_curr)
        curr_kans_neerslag.SetFont(font_curr)
        curr_regen_mm.SetFont(font_curr)
        curr_sneeuw_mm.SetFont(font_curr)
        day1_dt.SetFont(font_days_bold)
        day1_cond.SetFont(font_days_normal)
        day1_temp_dag.SetFont(font_days_normal)
        day1_min_max.SetFont(font_days_normal)
        day1_kans_neerslag.SetFont(font_days_normal)
        day1_regen_mm.SetFont(font_days_normal)
        day1_sneeuw_mm.SetFont(font_days_normal)
        day2_dt.SetFont(font_days_bold)
        day2_cond.SetFont(font_days_normal)
        day2_temp_dag.SetFont(font_days_normal)
        day2_min_max.SetFont(font_days_normal)
        day2_kans_neerslag.SetFont(font_days_normal)
        day2_regen_mm.SetFont(font_days_normal)
        day2_sneeuw_mm.SetFont(font_days_normal)

        #
        # Toevoegen labels aan sizers
        #
        mainSizer.Add(northSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        mainSizer.Add(sizer, 1, wx.EXPAND | wx.ALL, 2)
        northSizer.Add(curr_dt, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer.Add(boxSizer, 1, wx.ALL, 2)
        sizer.Add(day1Sizer, 1, wx.EXPAND | wx.ALL, 2)
        sizer.Add(day2Sizer, 1, wx.EXPAND | wx.ALL, 2)
        zeroSizer.Add(currLSizer, 0, wx.ALL, 3)
        zeroSizer.Add(currMSizer, 0, wx.ALL, 3)
        zeroSizer.Add(currRSizer, 0, wx.ALL, 3)
        boxSizer.Add(curr_icoon, 1, wx.ALIGN_CENTER | wx.ALL, 2)
        boxSizer.Add(curr_cond, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        boxSizer.Add(zeroSizer, 0, wx.ALIGN_CENTER | wx.ALL, 2)
        currLSizer.Add(curr_temp, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        currLSizer.Add(curr_min_max, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        currMSizer.Add(curr_druk, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        currMSizer.Add(curr_voch, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        currMSizer.Add(curr_snel, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        currRSizer.Add(curr_kans_neerslag, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        currRSizer.Add(curr_regen_mm, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        currRSizer.Add(curr_sneeuw_mm, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day1Sizer.Add(day1_icoon, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        day1Sizer.Add(day1_dt, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day1Sizer.Add(day1_cond, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day1Sizer.Add(day1_temp_dag, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day1Sizer.Add(day1_min_max, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day1Sizer.Add(day1_kans_neerslag, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day1Sizer.Add(day1_regen_mm, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day1Sizer.Add(day1_sneeuw_mm, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day2Sizer.Add(day2_icoon, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        day2Sizer.Add(day2_dt, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day2Sizer.Add(day2_cond, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day2Sizer.Add(day2_temp_dag, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day2Sizer.Add(day2_min_max, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day2Sizer.Add(day2_kans_neerslag, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day2Sizer.Add(day2_regen_mm, 1, wx.ALIGN_LEFT | wx.ALL, 2)
        day2Sizer.Add(day2_sneeuw_mm, 1, wx.ALIGN_LEFT | wx.ALL, 2)

        # Sizer aan panel toevoegen en op maat maken
        self.SetSizerAndFit(mainSizer)
        self.Layout()


#
# Opvragen weerdata
#
def requestWeather():
    # Building the final url for the API call
    url = (f"{root_url}appid={api_key}&lat={lat}&lon={lon}&units={units}&lang={language}&exclude=minutely,hourly")
    # sending a get request at the url
    r = requests.get(url)
    # storing the returned json data into a variable
    data = r.json()

    # getting the datetime from the json data
    timestamp = data['current']['dt']
    curr_dt = wx.DateTime.FromTimeT(timestamp)
    # getting the temperature from the json data
    curr_temp = data['current']['temp']
    curr_temp_min = data['daily'][0]['temp']['min']
    curr_temp_max = data['daily'][0]['temp']['max']
    # getting the pressure from the json data
    curr_pressure = data['current']['pressure']
    # getting the humidity from the json data
    curr_humidity = data['current']['humidity']
    # getting the description from the json data
    curr_descr = data['current']['weather'][0]['description']
    # getting the wind speed from the json data
    curr_wind = data['current']['wind_speed']
    # getting the weather icon from the json data
    curr_icon = data['current']['weather'][0]['icon']
    curr_pop = data['daily'][0]['pop']
    # try, omdat regen en sneeuw niet altijd in de data zit
    try:
        curr_rain = data['daily'][0]['rain']
    except:
        curr_rain = 0
    try:
        curr_snow = data['daily'][0]['snow']
    except:
        curr_snow = 0
    # Opgehaalde data huidige dag in dictionary zetten
    weer_data["curr_dt"] = curr_dt
    weer_data["curr_icoon"] = curr_icon
    weer_data["curr_conditie"] = curr_descr
    weer_data["curr_temperatuur"] = curr_temp
    weer_data["curr_temp_min"] = curr_temp_min
    weer_data["curr_temp_max"] = curr_temp_max
    weer_data["curr_luchtdruk"] = curr_pressure
    weer_data["curr_luchtvochtigheid"] = curr_humidity
    weer_data["curr_windsnelheid"] = curr_wind
    weer_data["curr_kans_neerslag"] = int(curr_pop * 100)
    weer_data["curr_regen_mm"] = curr_rain
    weer_data["curr_sneeuw_mm"] = curr_snow

    #
    # Ophalen gegevens dag 1
    #
    # datetime dag 1
    day1_dt = wx.DateTime.FromTimeT(data['daily'][1]['dt'])
    # weericoon
    day1_icon = data['daily'][1]['weather'][0]['icon']
    # weerconditie
    day1_cond = data['daily'][1]['weather'][0]['description']
    # dagtemperatuur
    day1_temp_day = data['daily'][1]['temp']['day']
    # minimale en maximale temperatuur
    day1_temp_min = data['daily'][1]['temp']['min']
    day1_temp_max = data['daily'][1]['temp']['max']
    # kans op neerslag
    day1_pop = data['daily'][1]['pop']
    # neerslag. try, omdat regen en sneeuw niet altijd in data zit
    try:
        day1_rain = data['daily'][1]['rain']
    except:
        day1_rain = 0
    try:
        day1_snow = data['daily'][1]['snow']
    except:
        day1_snow = 0
    # Opgehaalde data dag 1 in dictionary zetten
    weer_data["day1_dt"] = day1_dt
    weer_data["day1_icoon"] = day1_icon
    weer_data["day1_conditie"] = day1_cond
    weer_data["day1_temp_dag"] = day1_temp_day
    weer_data["day1_temp_min"] = day1_temp_min
    weer_data["day1_temp_max"] = day1_temp_max
    weer_data["day1_kans_neerslag"] = int(day1_pop * 100)
    weer_data["day1_regen_mm"] = day1_rain
    weer_data["day1_sneeuw_mm"] = day1_snow

    #
    # Ophalen gegevens dag 2
    #
    # datetime dag 2
    day2_dt = wx.DateTime.FromTimeT(data['daily'][2]['dt'])
    # weericoon
    day2_icon = data['daily'][2]['weather'][0]['icon']
    # weerconditie
    day2_cond = data['daily'][2]['weather'][0]['description']
    # dagtemperatuur dag 2
    day2_temp_day = data['daily'][2]['temp']['day']
    # minimale en maximale temperatuur
    day2_temp_min = data['daily'][2]['temp']['min']
    day2_temp_max = data['daily'][2]['temp']['max']
    # kans op neerslag
    day2_pop = data['daily'][2]['pop']
    # neerslag. try, omdat regen en sneeuw niet altijd in data zit
    try:
        day2_rain = data['daily'][2]['rain']
    except:
        day2_rain = 0
    try:
        day2_snow = data['daily'][2]['snow']
    except:
        day2_snow = 0
    # Ogehaalde data dag 2 in dictionary zetten
    weer_data["day2_dt"] = day2_dt
    weer_data["day2_icoon"] = day2_icon
    weer_data["day2_conditie"] = day2_cond
    weer_data["day2_temp_dag"] = day2_temp_day
    weer_data["day2_temp_min"] = day2_temp_min
    weer_data["day2_temp_max"] = day2_temp_max
    weer_data["day2_kans_neerslag"] = int(day2_pop * 100)
    weer_data["day2_regen_mm"] = day2_rain
    weer_data["day2_sneeuw_mm"] = day2_snow
