from instabot import Bot
import userins
import time
med = Bot()
med.login(username = userins.username , password = userins.password)
medias = med.get_total_user_medias(med.user_id)

for media in medias:
    try:
        med.delete_media(media)
        time.sleep(5)
        print("Delete Succesful!")
    except:
        print("No such post exists")
        time.sleep(10)


