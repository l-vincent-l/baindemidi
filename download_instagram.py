from instagrapi import Client
import os

ACCOUNT_USERNAME = os.getenv('INSTAGRAM_USERNAME')
ACCOUNT_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
user_id = cl.user_id_from_username("bain.de.midi")
medias = cl.user_medias(user_id)
photos = [media for media in medias if media.media_type == 1]

for photo in photos:
	cl.photo_download(photo.pk)