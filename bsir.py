import datetime
today = datetime.date.today() 
#today = datetime.date(2023, 10, 23)
expiry_date = datetime.date(2024, 1, 19)
delta = expiry_date - today

fees_entry = 5.08
fees_exit = 5.08
fees = fees_entry + fees_exit

spread = 2000
multiplier = 10

entry_limit = -1979.9

print("Delta: {} days".format(delta.days))

# it's intentional to _not_ take the absolute vale
# if we use a positive limit, bad things will happen!
factor = (-entry_limit - fees/multiplier) / spread

interest = 1 - factor**(365/delta.days)

print("Interest rate: {}%".format(str(round(interest*100, 2))))

# do it the other way round, calculate the limit for a given interest rate

interest_goal = 4.0

factor = (1-interest_goal/100)**(delta.days/365)
entry_limit = - spread*factor + fees / multiplier


print("Limit for a {}% rate: {}".format(str(round(interest_goal, 2)),str(round(entry_limit,3))))

