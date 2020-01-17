import json
import sqlite3
from pathlib import Path


question1 = input("Would you like to sign in or sign up?").lower()
if question1 == "sign in":
    sign_name = input("Enter name: ")
    sign_pass = input("Enter password: ")
    sign_email = input("Enter email: ")

    with sqlite3.connect("ui_data.sqlite3") as conn:
        command = "Select * from Data"
        cursor = conn.execute(command)
        for row in cursor:
            if sign_name and sign_pass and sign_email in row:
                print("You have successfully signed in.")
                break
            pass
if question1 == "sign up":
    while True:
        name = input("Enter full name: ")
        password1 = input("Please create password: ")
        password2 = input("Please re-enter password: ")
        if password1 != password2:
            print("These passwords must match.")
            pass
        if password1 == password2:
            break

    while True:
        email1 = input("Please enter email adress:")
        email2 = input("Please re-enter email adress:")
        if email1 != email2:
            print("These email adresses must match.")
        if email1 == email2:
            break

    if password1 == password2 and email1 == email2:
        info = [
            {"password": password1, "email": email1, "name": name}
        ]
        data = json.dumps(info)
        Path("info.json").write_text(data)

        checks = json.loads(Path("info.json").read_text())

        with sqlite3.connect("ui_data.sqlite3") as conn:
            command = "INSERT INTO Data VALUES(?, ?, ?)"
            for check in checks:
                conn.execute(command, tuple(check.values()))
            conn.commit()

    sign_in = input("Would you like to sign in?").lower()
    if sign_in == "yes" or question1 == "signup":
        sign_pass = input("Enter password: ")
        sign_email = input("Enter email: ")

    with sqlite3.connect("ui_data.sqlite3") as conn:
        command = "Select * from Data"
        cursor = conn.execute(command)
        for row in cursor:
            if sign_pass and sign_email in row:
                print("You have successfully signed in.")
                break
