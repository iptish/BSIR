import datetime

# it's intentional to _not_ take the absolute value
# if we use a positive limit, bad things will happen!


def interest_from_limit(delta_days,fees,multiplier,spread,limit):
  factor = (-limit - fees/multiplier) / spread
  interest =  (1 - factor**(365/delta_days))*100
  return interest
  
  
def limit_from_interest(delta_days,fees,multiplier,spread,interest):
  print("Interest rate: {}%".format(str(round(interest, 2))))
  print("deltadays: {}%".format(str(delta_days)))
  print("multiplier: {}%".format(str(multiplier)))
  print("spread: {}%".format(str(spread)))
  print("fees: {}%".format(str(round(fees, 2))))
  factor = (1-interest/100)**(delta_days/365)
  print("factor: {}".format(str(round(factor, 5))))
  limit = - spread*factor - fees / multiplier
  print("limit: {}".format(str(round(limit, 2))))
  return limit
  
# time span in days
today = datetime.date.today() 
#today = datetime.date(2023, 10, 23)
expiry_date = datetime.date(2024, 1, 19)
delta = expiry_date - today

# trading fees
fees_entry = 5.08
fees_exit = 5.08
fees = fees_entry + fees_exit

# contract details
spread = 2000
multiplier = 10

entry_limit = -1979.9

interest = interest_from_limit(delta.days,fees,multiplier,spread,entry_limit)
print("Interest rate: {}%".format(str(round(interest, 2))))

# do it the other way round, calculate the limit for a given interest rate

interest_goal = 4.0

entry_limit = limit_from_interest(delta.days,fees,multiplier,spread,interest_goal)

print("Limit for a {}% rate: {}".format(str(round(interest_goal, 2)),str(round(entry_limit,3))))

