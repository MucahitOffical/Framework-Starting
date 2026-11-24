import requests


def user_gather(response):
    data = response.json()

    for user in data:
        print(user)


def register():

    while True:
        username = input("Kullanıcı adınızı giriniz: ")

        if len(username) > 12:
            print("Kullanıcı adı çok uzun!")
        else:
            break

    email = input("Emailinizi giriniz: ")
    password = input("Şifrenizi giriniz: ")

    response = requests.post(
        "http://127.0.0.1:8000/register",
        json={
            "username": username,
            "email": email,
            "password": password
        }
    )


def toplu_kayit(kisi):

    for i in range(kisi):
        register()


toplu_kayit(2)

response = requests.get("http://127.0.0.1:8000/users")

user_gather(response)