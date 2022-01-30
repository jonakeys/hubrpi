# hubrpi
Information hub for use on small (touch)screen (example 7' touchscreen for Raspberry PI).

// INTRO
Information hub I made for the touchscreen of a Raspberry Pi 2B to display information like weather, calendar, energy usage, a fortune cookie (as known in Unix-land ;-) and play music. Feel free to try it and improve it. As it's my first Python project I wrote, I'm sure there are different ways to make it more efficient. You can use it as a base and work from there. Take a look at the screenshots to see what it looks like on my screen.
To make it work, you have to enter your details for the OpenWeather api and the caldav calendar ofcourse. The images and data created for the energy-tools are generated with another script on my github, 'energieverbruik' https://github.com/jonakeys/energieverbruik. And also the scripts to music you have to change to your own stations and/or folders.

Feel free to contact me, I hope to hear from you!

// NEEDED LIBRARIES
Needed python libraries:
- wxPython
https://www.wxpython.org/

(Installable via pip:)
- caldav
https://github.com/python-caldav/caldav

- fortunate
https://github.com/Kronuz/fortunate

- pandas (Python dataframes)
https://pandas.pydata.org/

- requests
https://docs.python-requests.org/en/latest/

- urllib3
https://urllib3.readthedocs.io/en/stable/

// WEATHER
The icons in folder 'weather_icons': Openweathermap.org.
The icons in folder 'VClouds_weather_icons': VClouds Weather Icons© Created and copyrighted© by VClouds - http://vclouds.deviantart.com/

// FORTUNE
The cookies are contanized files of the excellent program from: https://www.shlomifish.org/open-source/projects/fortune-mod/

// SCREENSHOTS
![tabWeer](https://user-images.githubusercontent.com/4281902/151707159-c39aaefc-f3e2-4fd5-9979-ccdac8215994.png)
![tabAgenda](https://user-images.githubusercontent.com/4281902/151707203-607e69a7-7a0a-4191-b0f7-1819c8f1334b.png)
![tabFortune](https://user-images.githubusercontent.com/4281902/151707223-eca351e1-c98f-4d30-944b-ef4f1b0aa484.png)
![tabGas](https://user-images.githubusercontent.com/4281902/151707207-cd6c2323-d4ef-468a-b651-07ad207a010e.png)
![tabElektriciteit](https://user-images.githubusercontent.com/4281902/151707209-de99e2dc-b525-4cfd-a260-4e24c8e1764a.png)
![tabWater](https://user-images.githubusercontent.com/4281902/151707212-8a0592d7-a728-4093-9ebf-c1627a615b23.png)
![tabEnergie](https://user-images.githubusercontent.com/4281902/151707214-af28575e-be3f-4b37-ac92-19cb5141f9aa.png)
![tabMuziek](https://user-images.githubusercontent.com/4281902/151707218-680c6eb9-f614-4827-936f-9a06c7716e65.png)
![tabTools](https://user-images.githubusercontent.com/4281902/151707232-ec674438-3129-4624-8a8d-3650bdd4d291.png)
