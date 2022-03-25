from instagrapi import Client
import os, time, random

ACCOUNT_USERNAME = os.getenv('INSTAGRAM_USERNAME')
ACCOUNT_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
print(ACCOUNT_USERNAME)

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
user_id = cl.user_id_from_username("bain.de.midi")
time.sleep(random.randrange(890, 2500)/1000)
medias = cl.user_medias(user_id)
photos = [media for media in medias if media.media_type == 1]

time.sleep(random.randrange(890, 2500)/1000)
path = "downloads/photos/instagram"
os.makedirs(path, exist_ok=True)
for photo in photos:
	cl.photo_download(photo.pk, path)