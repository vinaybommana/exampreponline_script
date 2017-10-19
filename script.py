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


# contains all the lines from the "Automatic email content store.csv"
lines = list()

with open("Automatic email content store.csv") as f:
    for line in f:
        lines.append(line)

# today = date.today()
# print(today)

# contains dates in the lines
dates = list()

# contains emails from the lines `list`
emails = list()

# contains messages from the lines `list`
# we didn't use the messages list anywhere
messages = list()

for line in lines:
    # the first date$to$email is removed
    # can use a simple list comprehension removal
    # this way may be effective
    if (lines.index(line) != 0) and (len(line.split("$")[0]) < 9):
        # len(line.split("$")[0]) < 9 is to omit the 1st oct 2017 date with weird functionality
        # recommended to omit
        # we can convert the 1st oct 2017 to number and can use it
        # for analysis
        dates.append(line.split("$")[0])
        emails.append(line.split("$")[1])
        messages.append(line.split("$")[2])


# removes the extra date line in the csv file
dates = [i for i in dates if len(i.split("/")) == 3]
unique_emails = list(set(emails))
# print(unique_emails)

dictionary_of_dates_emails = dict()
for i in range(len(emails)):
    dictionary_of_dates_emails[emails[i]] = dates[i]

# print(dictionary_of_dates_emails)
# can use zip but the functionality is not so good for this script
# zip function is highly recommended
# dictionary_of_dates_emails = dict(zip(emails, dates))

messages = [i.strip() for i in messages]
c = collections.Counter(emails)
# print(c[unique_emails[-4]])

for i in unique_emails:
    try:
        # print(str(i) + " " + str(no_of_days_elapsed(dictionary_of_dates_emails[i])) + " " + str(c[i]))
        csv_file.writerow([str(i), str(no_of_days_elapsed(dictionary_of_dates_emails[i])), str(c[i])])
        pass
    except KeyError:
        # just to make sure everything is fine
        # no key error is present until now
        print("key not found")
