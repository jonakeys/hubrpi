# hubrpi
Information hub for use on small (touch)screen (example 7' touchscreen for Raspberry PI).


// INTRO
Information hub I made for the touchscreen of a Raspberry Pi 2B to display information like weather, calendar, energy usage, a fortune cookie (as known in Unix-land ;-) and play music. Feel free to try it and improve it. As it's my first Python project I wrote, I'm sure there are different ways to make it more efficient. You can use it as a base and work from there. Take a look at the screenshots to see what it looks like on my screen.
To make it work, you have to enter your details for the OpenWeather api and the caldav calendar ofcourse. The images and data created for the energy-tools are generated with another script on my github, 'energieverbruik' https://github.com/jonakeys/energieverbruik.

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
