# Moods

A simple Django application that finds suitable music for the local type of weather using the OpenWeather and Spotify Api.


## Requirements

* Python v3.9.x
* Django==4.1.4


## Install


```
$ pyenv virtualenv 3.9.10 moods
$ pyenv activate moods
$ make install
```

Add Spotify API keys etc. in settings.py 

* CLIENT_ID 
* CLIENT_SECRET 
* TOKEN_URL 
* SPOTIFY_API_URL

For a tutorial on setting up your Spotify Developer account and obtaining API keys, token etc see:

* https://developer.spotify.com/documentation/web-api/quick-start/


Add OpenWeather URL containing your API key to settings.py. For example: http://api.openweathermap.org/data/2.5/forecast/?id=_YOUR_ID_HERE_&units=metric&q=

Of course units can be changed to imperial, other OpenWeather API parameters can be added as well.

* OPENWEATHER_API_URL

OpenWeather API docs:

* https://openweathermap.org/current

```
$ python3 manage.py runserver
```


## Customize

Edit moods/constants/__init__.py to link weather types to music genres. A 
complete list of all available music genres for the Spotify API can be found 
here:

* https://spotify-top.com/genres

Replace the images in the /moods/static folder. Please note that the filenames have to match the original ones.
