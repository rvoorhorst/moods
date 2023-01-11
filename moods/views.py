import base64
import random

import requests
from django.urls import reverse
from django.views.generic import FormView, TemplateView

import moods.settings as settings
from moods.constants import spotify_api_params
from moods.forms import CityNameForm


class HomeFormView(FormView):
    form_class = CityNameForm
    template_name = "moods/home.html"

    def get_success_url(self):
        return reverse("playlist")

    def form_valid(self, form):
        self.request.session["user_location"] = form.cleaned_data["user_location"]
        self.request.session.save()
        return super().form_valid(form)


class PlaylistTemplateView(TemplateView):
    template_name = "moods/playlist.html"

    def get_weather_data(self):
        user_location = self.request.session["user_location"]
        r = requests.get(settings.OPENWEATHER_API_URL + user_location)
        data = r.json()
        return data

    def get_spotify_api_access_token(self):
        basic_auth_token = base64.b64encode(
            ("%s:%s" % (settings.CLIENT_ID, settings.CLIENT_SECRET)).encode("ascii")
        ).decode("ascii")
        body = {"grant_type": "client_credentials"}
        headers = {"Authorization": "Basic %s" % basic_auth_token}
        r = requests.post(settings.TOKEN_URL, data=body, headers=headers)

        if r.status_code == 200:
            data = r.json()
            access_token = data["access_token"]
            return access_token

    def get_spotify_uri(self):
        wdata = self.get_weather_data()
        weather_type = wdata["list"][0]["weather"][0]["main"]
        access_token = self.get_spotify_api_access_token()
        params = spotify_api_params[weather_type]
        headers = {"Authorization": "Bearer " + access_token}
        r = requests.get(settings.SPOTIFY_API_URL, params=params, headers=headers)
        data = r.json()
        print(data)
        uri = data["tracks"][0]["artists"][0]["uri"]
        return uri

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_weather_data()
        uri = self.get_spotify_uri()
        temperature = data["list"][0]["main"]["temp"]
        context["temperature"] = round(temperature)
        context["country"] = data["city"]["country"]
        context["city"] = data["city"]["name"]
        context["weather_description"] = data["list"][0]["weather"][0]["description"]
        context["weather_main"] = str(
            data["list"][0]["weather"][0]["main"] + ".jpg"
        ).lower()
        context["uri"] = uri

        return context
