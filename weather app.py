from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root=Tk()
root.title('Weather Application')
root.geometry('230x170')

def locate():
    try:
        req_api=requests.get("https://api.weatherapi.com/v1/current.json?key=57362d6838ce4b248e171459201012&q="+locentry.get()+"")
        api=json.loads(req_api.content)
        loc=text=api['location']['name']
        tempe=text=api['current']['temp_c']
        cloud=text=api['current']['cloud']
        humid=api['current']['humidity']
    except Exception as e:
        api='ERROR'

    location=Label(root,text=loc)
    location.grid(row=0,column=1)

    temperature=Label(root,text=tempe)
    temperature.grid(row=1,column=1)

    cloudy=Label(root,text=cloud)
    cloudy.grid(row=2,column=1)

    hum=Label(root,text=humid)
    hum.grid(row=3,column=1)



try:
    req_api=requests.get('https://api.weatherapi.com/v1/current.json?key=57362d6838ce4b248e171459201012&q=chennai')
    api=json.loads(req_api.content)
    loc=text=api['location']['name']
    tempe=text=api['current']['temp_c']
    cloud=text=api['current']['cloud']
    humid=api['current']['humidity']


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

entlabel=Label(root,text="Enter location: ")
entlabel.grid(row=4,column=0)

#results
location=Label(root,text=loc)
location.grid(row=0,column=1)

temperature=Label(root,text=tempe)
temperature.grid(row=1,column=1)

cloudy=Label(root,text=cloud)
cloudy.grid(row=2,column=1)

hum=Label(root,text=humid)
hum.grid(row=3,column=1)

#location entry
locentry=Entry(root)
locentry.grid(row=4,column=1)

#submit location
locbut=Button(root,text="Submit location",command=locate)
locbut.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=50)


root.mainloop()
