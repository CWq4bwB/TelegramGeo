from pyrogram import Client

api_id = 2040
api_hash = "b18441a1ff607e10a989891a5462e627"
app = Client("my_account", api_id, api_hash)
fixed_location = ""


async def main():
    global fixed_location
    async with app:
        for elem in await app.get_nearby_chats(float(fixed_location[0]), float(fixed_location[1])):
            print('\n')
            print(f"Название: {elem.title}")
            print(f"id: {elem.id}")
            print(f"Участников: {elem.members_count}")
            if elem.username:
                print(f"Ссылка: {elem.username}")
            photo = elem.photo
            if photo:
                await app.download_media(photo.big_file_id, file_name=f"{location}/{elem.title}.jpg")
                print("Фотография сохранена.")
            else:
                print("Фотографий нет.")


async def get_members(chat_id):
    async with app:
        async for member in app.get_chat_members(chat_id):
            if not (member.user.is_deleted or member.user.is_bot):
                photo = member.user.photo
                uid = member.user.id
                fio = member.user.first_name if not member.user.last_name else member.user.first_name + " " + \
                                                                               member.user.last_name
                username = member.user.username
                phone = member.user.phone_number
                print('\n')
                print(f"Имя: {fio}")
                print(f"id: {uid}")
                if username:
                    print(f"ник: {username}")
                if phone:
                    print(f"телефон: {phone}")
                if photo:
                    await app.download_media(photo.big_file_id, file_name=f"{location}/{fio}.jpg")
                    print("Фотография сохранена.")
                else:
                    print("Фотографий нет.")


while True:
    location = input("Введи локацию или chat_id: ")
    if not location:
        break
    elif location[0] == "-":
        app.run(get_members(location))
    else:
        fixed_location = location.split(", ")
        app.run(main())
