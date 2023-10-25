import datetime
# it's intentional to _not_ take the absolute value
# if we use a positive limit, bad things will happen!

with open("bsir.py") as f:
  exec(f.read())
 
    
from tkinter import *
import tkinter as tk
import  tkcalendar as tkc

master = tk.Tk()
var0 = tk.StringVar()
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()
var6 = tk.StringVar()
var7 = tk.StringVar()
tk.Label(master, text="spread").grid(row=0)
tk.Label(master, text="multiplier").grid(row=1)
tk.Label(master, text="entry fees").grid(row=2)
tk.Label(master, text="exit fees").grid( row=3)
tk.Label(master, text="starting date").grid(row=4)
tk.Label(master, text="ending date").grid( row=5)
tk.Label(master, text="entry limit").grid(row=6)
tk.Label(master, text="interest rate (%)").grid(row=7)

spread = tk.Entry(master, textvariable=var0)
spread.insert(0,"5000")
multiplier = tk.Entry(master, textvariable=var1)
multiplier.insert(0,"10")
entry_fees = tk.Entry(master, textvariable=var2)
entry_fees.insert(0,"5.08")
exit_fees = tk.Entry(master, textvariable=var3)
exit_fees.insert(0,"5.08")
start = tkc.DateEntry(master) # defaults to today
end = tkc.DateEntry(master)
end.set_date(datetime.date(2024, 1, 19))
entry_limit = tk.Entry(master, textvariable=var6)
entry_limit.insert(0,"-4900.0")
interest = tk.Entry(master, textvariable=var7)

spread.grid(row=0, column=1)
multiplier.grid(row=1, column=1)
entry_fees.grid(column=1, row=2)
exit_fees.grid(column=1, row=3)
start.grid(column=1, row=4)
end.grid(column=1, row=5)
entry_limit.grid(column=1, row=6)
interest.grid(column=1, row=7)


def update_interest():
  delta = end.get_date() - start.get_date()
  fees = float(entry_fees.get()) + float(exit_fees.get())
  interest_rate = interest_from_limit(delta.days,fees,int(multiplier.get()),int(spread.get()),float(entry_limit.get()))
  mystr = "{:.3f}".format(interest_rate)
  #interest.config(state= "normal")
  interest.delete(0, 'end')
  interest.insert(0,mystr)
  interest.config(state= "readonly")
  
def update_limit():
  delta = end.get_date() - start.get_date()
  fees = float(entry_fees.get()) + float(exit_fees.get())
  interest_rate = interest_from_limit(delta.days,fees,int(multiplier.get()),int(spread.get()),float(entry_limit.get()))
  limit = limit_from_interest(delta.days,fees,int(multiplier.get()),int(spread.get()),float(interest.get()))
  mystr = "{:.2f}".format(limit)
  #entry_limit.config(state= "normal")
  entry_limit.delete(0, 'end')
  entry_limit.insert(0,mystr)
  entry_limit.config(state= "readonly")
  

update_interest()
#interest.config(state= "readonly")


choice = tk.IntVar()

def onRadioButtonChange():
  if choice.get() != 0:
    #entry_limit.config(state= "readonly")
    interest.config(state= "normal")
    update_limit()
  else:
    entry_limit.config(state= "normal")
    #interest.config(state= "readonly")
    update_interest()
    
update_in_progress = False
   
def update(*args):
  global update_in_progress
  if update_in_progress: return
  try:
    if choice.get() != 0:
      #entry_limit.config(state= "readonly")
      interest.config(state= "normal")
      update_limit()
    else:
      entry_limit.config(state= "normal")
      #interest.config(state= "readonly")
      update_interest()
  except ValueError:
    return

var0.trace_add("write",update)
var1.trace_add("write",update)
var2.trace_add("write",update)
var3.trace_add("write",update)
var4.trace_add("write",update)
var5.trace_add("write",update)
var6.trace_add("write",update)
var7.trace_add("write",update)

limit_input = Radiobutton(text="",
                      variable=choice, value=0, highlightthickness=0,command=onRadioButtonChange)
limit_input.grid(column=2, row=6, sticky="w")
rate_input = Radiobutton(text="",
                      variable=choice, value=1, highlightthickness=0,command=onRadioButtonChange)
rate_input.grid(column=2, row=7, sticky="w")

master.mainloop()