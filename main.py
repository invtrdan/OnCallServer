from flask import Flask, render_template, request
from datetime import datetime, date
from replit import db
import json

def schedule_data():
  db['01'] = ['','Oshione and J.R']
  db['02'] = ['','Oshione & Alex']
  db['03'] = ['','Farouk & J.R']
  db['04'] = ['','Oshione & J.R']
  db['05'] = ['','Spring Break']
  db['06'] = ['','Spring Break']
  db['07'] = ['','Spring Break']
  db['08'] = ['','Spring Break']
  db['09'] = ['','Spring Break']
  db['10'] = ['','Spring Break']
  db['11'] = ['','Spring Break']
  db['12'] = ['', 'Demetrius & Danielle']
  db['13'] = ['','Demetrius & Robert']
  db['14'] = ['','Mickey & Danielle']
  db['15'] = ['','Demetrius & Danielle']
  db['16'] = ['','Danielle & Robert']
  db['17'] = ['','Mickey & Robert']
  db['18'] = ['', 'Mickey & Robert']
  db['19'] = ['']
  db['20'] = ['']
  db['21'] = ['']
  db['22'] = 'Ari and Gabe','test'
  db['23'] = ['Ari and Ro']
  db['24'] = ['Azariah and Ari']
  db['25'] = ['Azariah and Ari']
  db['26'] = ['Farouk and Alex']
  db['27'] = ['Farouk and Alex']
  db['28'] = ['Oshione and J.R']
  db['29'] = ['n/a']
  db['30'] = ['n/a']
  db['31'] = ['n/a']

def get_month():
  today = str(date.today())
  month_int = int(today[5:7])
  if month_int == 2:
    month = 'February'
    index = 0
  elif month_int == 3:
    month = 'March'
    index = 1
  elif month_int == 4:
    month = 'April'
    index = 2
  elif month_int == 5:
    month = 'May'
    index = 2
  return month, index
  
app = Flask(__name__)
BASE_URL = "https://On-Call.invtrdan.repl.co"

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/oncall')
def get_oncall():
  schedule_data()
  today = str(date.today())
  today = today[8::]
  month, index = get_month()
  RA_list = db[today]
  RA = RA_list[index]
  return render_template('call.html', RA=RA)

@app.route('/schedule')
def view_schedule():
  schedule_data()
  today = str(date.today())
  month, index = get_month()
    
  d1 = "1: " + db['01'][index]
  d2 = "2: " + db['02'][index]
  d3 = "3: " + db['03'][index]
  d4 = "4: "+ db['04'][index] 
  d5 = "5: "+ db['05'][index] 
  d6 = "6: "+ db['06'][index]
  d7 = "7: "+ db['07'][index]
  d8 = "8: "+ db['08'][index]
  d9 = "9: "+ db['09'][index] 
  d10 = "10: "+ db['10'][index]
  d11 = "11: "+ db['11'][index]
  d12 = "12: "+ db['12'][index]
  d13 = "13: "+ db['13'][index]
  d14 = "14: "+ db['14'][index]
  d15 = "15: "+ db['15'][index]
  d16 = "16: "+ db['16'][index]
  d17 = "17: "+ db['17'][index]
  d18 = "18: "+ db['18'][index]
  d19 = "19: "+ db['19'][index]
  d20 = "20: "+ db['20'][index]
  d21 = "21: "+ db['21'][index]
  d22 = "22: "+ db['22'][index]
  d23 = "23: "+ db['23'][index]
  d24 = "24: "+ db['24'][index]
  d25 = "25: "+ db['25'][index]
  d26 = "26: "+ db['26'][index]
  d27 = "27: "+ db['27'][index]
  d28 = "28: "+ db['28'][index]
  d29 = "29: "+ db['29'][index]
  d30 = "30: "+ db['30'][index]
  d31 = "31: "+ db['31'][index]
  return render_template('schedule.html', month=month, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, d7=d7, d8=d8, d9=d9, d10=d10, d11=d11, d12=d12, d13=d13, d14=d14, d15=d15, d16=d16, d17=d17, d18=d18, d19=d19, d20=d20, d21=d21, d22=d22, d23=d23, d24=d24, d25=d25, d26=d26, d27=d27, d28=d28, d29=d29, d30=d30, d31=d31)
  
  
app.run(host='0.0.0.0', port=81)
