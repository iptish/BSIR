import datetime
# it's intentional to _not_ take the absolute value
# if we use a positive limit, bad things will happen!

with open("bsir.py") as f:
  exec(f.read())
 
    
from tkinter import *
import tkinter as tk
import  tkcalendar as tkc



def update_interest():
  delta = end.get_date() - start.get_date()
  fees = float(entry_fees.get()) + float(exit_fees.get())
  interest_rate = interest_from_limit(delta.days,fees,int(multiplier.get()),int(spread.get()),float(entry_limit.get()))
  mystr = "{:.3f}".format(interest_rate)
  #interest.config(state= "normal")
  interest.delete(0, 'end')
  interest.insert(0,mystr)
  #interest.config(state= "readonly")
  
def update_limit():
  delta = end.get_date() - start.get_date()
  fees = float(entry_fees.get()) + float(exit_fees.get())
  interest_rate = interest_from_limit(delta.days,fees,int(multiplier.get()),int(spread.get()),float(entry_limit.get()))
  limit = limit_from_interest(delta.days,fees,int(multiplier.get()),int(spread.get()),float(interest.get()))
  mystr = "{:.2f}".format(limit)
  #entry_limit.config(state= "normal")
  entry_limit.delete(0, 'end')
  entry_limit.insert(0,mystr)
  #entry_limit.config(state= "readonly")
  
def onButton_lim():
  #entry_limit.config(state= "readonly")
  #interest.config(state= "normal")
  update_limit()
def onButton_int():
  #entry_limit.config(state= "normal")
  #interest.config(state= "readonly")
  update_interest()
  
  
master = tk.Tk()
tk.Label(master, text="spread").grid(row=0)
tk.Label(master, text="multiplier").grid(row=1)
tk.Label(master, text="entry fees").grid(row=2)
tk.Label(master, text="exit fees").grid( row=3)
tk.Label(master, text="starting date").grid(row=4)
tk.Label(master, text="ending date").grid( row=5)
tk.Label(master, text="entry limit").grid(row=6)
tk.Label(master, text="interest rate (%)").grid(row=7)

  

button_int = tk.Button(master, text="Calculate",command=onButton_int)
button_lim = tk.Button(master, text="Calculate",command=onButton_lim)

spread = tk.Entry(master)
spread.insert(0,"5000")
multiplier = tk.Entry(master)
multiplier.insert(0,"10")
entry_fees = tk.Entry(master)
entry_fees.insert(0,"5.08")
exit_fees = tk.Entry(master)
exit_fees.insert(0,"5.08")
start = tkc.DateEntry(master) # defaults to today
end = tkc.DateEntry(master)
end.set_date(datetime.date(2024, 1, 19))
entry_limit = tk.Entry(master)
entry_limit.insert(0,"-4900.0")
interest = tk.Entry(master)

spread.grid(row=0, column=1)
multiplier.grid(row=1, column=1)
entry_fees.grid(column=1, row=2)
exit_fees.grid(column=1, row=3)
start.grid(column=1, row=4)
end.grid(column=1, row=5)
entry_limit.grid(column=1, row=6)
interest.grid(column=1, row=7)

button_lim.grid(column=2, row = 6)
button_int.grid(column=2, row = 7)

    

update_interest()
#interest.config(state= "readonly")
   

master.mainloop()