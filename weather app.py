from tkinter import *
import requests
import json

root=Tk()
root.title('Weather Application')
root.geometry('150x100')

try:
    req_api=requests.get('https://api.weatherapi.com/v1/current.json?key=57362d6838ce4b248e171459201012&q=chennai')
    api=json.loads(req_api.content)
except Exception as e:
    api='ERROR'

#label
labelloc=Label(root,text="Location:")
labelloc.grid(row=0,column=0)

labeltemp=Label(root,text="Temperature:")
labeltemp.grid(row=1,column=0)

labelcloud=Label(root,text="Cloudy:")
labelcloud.grid(row=2,column=0)

labelhumid=Label(root,text="Humidity:")
labelhumid.grid(row=3,column=0)

#results
location=Label(root,text=api['location']['name'])
location.grid(row=0,column=1)

temperature=Label(root,text=api['current']['temp_c'])
temperature.grid(row=1,column=1)

cloudy=Label(root,text=api['current']['cloud'])
cloudy.grid(row=2,column=1)

cloudy=Label(root,text=api['current']['humidity'])
cloudy.grid(row=3,column=1)


root.mainloop()