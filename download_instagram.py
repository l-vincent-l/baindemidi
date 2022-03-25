from instagrapi import Client
import os, time, random, sys

ACCOUNT_USERNAME = os.getenv('INSTAGRAM_USERNAME')
ACCOUNT_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

if not ACCOUNT_USERNAME:
    print("No username provided")
    sys.exit(2)
elif not ACCOUNT_PASSWORD:
    print("No password provided")
    sys.exit(2)
else:
    print("Username and password provided")

verification_code = sys.argv[1] if len(sys.argv) >= 2 else ""
if verification_code:
    print(f"Got verification code")

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, verification_code=verification_code)
user_id = cl.user_id_from_username("bain.de.midi")
time.sleep(random.randrange(890, 2500)/1000)
medias = cl.user_medias(user_id)
photos = [media for media in medias if media.media_type == 1]

time.sleep(random.randrange(890, 2500)/1000)
path = "downloads/photos/instagram"
os.makedirs(path, exist_ok=True)
for photo in photos:
	cl.photo_download(photo.pk, path)