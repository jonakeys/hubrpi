# hubrpi
Information hub for use on small (touch)screen (example 7' touchscreen for Raspberry PI).

## INTRO
Information hub I made for the touchscreen of a Raspberry Pi 2B to display information like weather, calendar, energy usage, a fortune cookie (as known in Unix-land ;-) and play music. Feel free to try it and improve it. As it's my first Python project I wrote, I'm sure there are different ways to make it more efficient. You can use it as a base and work from there. Take a look at the screenshots to see what it looks like on my screen.
To make it work, you have to enter your details for the OpenWeather api and the caldav calendar ofcourse. The images and data created for the energy-tools are generated with another script on my github, 'energieverbruik' https://github.com/jonakeys/energieverbruik. And also the scripts to music you have to change to your own stations and/or folders.

The program can be run by:
```
$ python hubrpi.py
```

Feel free to contact me, I like to hear from you!

## NEEDED LIBRARIES
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

## WEATHER
The icons in folder 'weather_icons': Openweathermap.org.
The icons in folder 'VClouds_weather_icons': VClouds Weather Icons© Created and copyrighted© by VClouds - http://vclouds.deviantart.com/

## FORTUNE
The cookies are concatanized files of the excellent program from: https://www.shlomifish.org/open-source/projects/fortune-mod/

## SCREENSHOTS
![tabWeer](https://user-images.githubusercontent.com/4281902/166310427-76b9e265-a0a3-4804-b8ff-bd4df72ea7e5.png)
![tabAgenda](https://user-images.githubusercontent.com/4281902/166310396-862619af-02c4-4576-8146-9a8f8e4eb6c8.png)
![tabFortune](https://user-images.githubusercontent.com/4281902/166310417-93c85f79-b270-4c38-b683-894eda8ad6e1.png)
![tabBitcoin](https://user-images.githubusercontent.com/4281902/166327601-596718e5-b564-439d-946c-15b336044256.png)
![tabGas](https://user-images.githubusercontent.com/4281902/166310419-fd7d4ef3-6642-4df8-92fd-58c767957dda.png)
![tabElektriciteit](https://user-images.githubusercontent.com/4281902/166310412-fe84c1f1-ce9b-4184-bb6e-1e2bbd48d90c.png)
![tabWater](https://user-images.githubusercontent.com/4281902/166310425-8cdfb94d-08f3-49f2-bc53-836cb7940ec0.png)
![tabEnergie](https://user-images.githubusercontent.com/4281902/166310416-edecfaba-f1f3-4751-bf2e-83db515ab0fa.png)
![tabMuziek](https://user-images.githubusercontent.com/4281902/166310422-f58eab24-b587-4171-94c1-bda10868df29.png)
![tabTools](https://user-images.githubusercontent.com/4281902/166310423-e6275658-c916-4aa0-bf21-7560120baf40.png)
