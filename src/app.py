import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Paso 4: Inicializar la biblioteca de Spotipy
auth_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)

sp=spotipy.Spotify(auth_manager=auth_manager)

# Paso 5: Realizar solicitidus a la API
post_malone_uri="https://open.spotify.com/intl-es/artist/246dkjvS1zLTtiykXe5h60"

top10 = sp.artist_top_tracks(artist_id="246dkjvS1zLTtiykXe5h60")

tracks = [{"name":i["name"], "popularity": i["popularity"], "duration": i["duration_ms"]} for i in top10["tracks"]]

# Paso 6: Transformar a Pandas Dataframe y mostrar el top 3 resultante
df = pd.DataFrame(tracks)

df["duration"] = df["duration"] / 1000

df_sorted = df.sort_values(by="popularity", ascending=True)

print(df_sorted.head(3))

# Paso 7: Analizar relación estadística
plt.figure(figsize=(7, 5))
plt.scatter(df["duration"], df["popularity"], color="red")

plt.xlabel("Duración (s)")
plt.ylabel("Popularidad")
plt.title("Relación entre duración y popularidad de canciones")

plt.show()

print("No parece haber excesiva relación entre la duración y la popularidad, ya que, por ejemplo, las 3 más populares son dispares en su duración")
