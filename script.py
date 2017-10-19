# automated script to give:
# 1. No of days elapsed from the last date of conversation
# 2. No of conversations for each email address

import csv
from datetime import date
import collections

csv_file = csv.writer(open("output.csv", "w"))
csv_file.writerow(["email", "No of days since last conversation", "No of conversations elapsed"])
# In order to find the no of days elapsed between two dates
# d0 = date(year, month, date)
# d1 = date(year, month, date)
# difference = d0 - d1
# print(difference.days)


def no_of_days_elapsed(conversation_date):
    """
    input: specified date
    returns no of days elapsed from the given date to the present day
    """
    day, month, year = conversation_date.split("/")
    today = date.today()
    year_of_now, month_of_now, day_of_now = str(today).split("-")
    if year == "17":
        year = str(2017)
    date_0 = date(int(year), int(month), int(day))
    date_1 = date(int(year_of_now), int(month_of_now), int(day_of_now))
    delta = date_1 - date_0
    return delta.days


lines = list()

with open("Automatic email content store.csv") as f:
    for line in f:
        lines.append(line)

# today = date.today()
# print(today)
dates = list()
emails = list()
messages = list()

for line in lines:
    if (lines.index(line) != 0) and (len(line.split("$")[0]) < 9):
        dates.append(line.split("$")[0])
        emails.append(line.split("$")[1])
        messages.append(line.split("$")[2])


# removes the extra date line in the csv file
dates = [i for i in dates if len(i.split("/")) == 3]
# print(dates)
# print(len(dates))
# print(emails)
unique_emails = list(set(emails))
# print(unique_emails)

dictionary_of_dates_emails = dict()
# i = 0
for i in range(len(emails)):
    dictionary_of_dates_emails[emails[i]] = dates[i]

# print(dictionary_of_dates_emails)

# dictionary_of_dates_emails = dict(zip(emails, dates))
# print(dictionary_of_dates_emails)

# for i in unique_emails:
#     print(i)

messages = [i.strip() for i in messages]
c = collections.Counter(emails)
# print(c[unique_emails[-4]])

for i in unique_emails:
    try:
        # print(str(i) + " " + str(no_of_days_elapsed(dictionary_of_dates_emails[i])) + " " + str(c[i]))
        csv_file.writerow([str(i), str(no_of_days_elapsed(dictionary_of_dates_emails[i])), str(c[i])])
        pass
    except KeyError:
        print("key not found")
