##################### Hard Starting Project ######################
import pandas
from datetime import datetime
import smtplib
import random

email = "test@gmail.com"
password = "123"
PLACE_HOLDER = "[NAME]"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        replaced_text = content.replace(PLACE_HOLDER, birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="test@yahoo.com",
                            msg=f"Subject:Happy Birthday!!\n\n{replaced_text}")


