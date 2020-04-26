import json
import datetime
with open('timeseries.json') as f:
      corona_data = json.load(f)

def general_info():
    country_name= input('Please enter the country you want to research') #ask for country information
    date= input('Please enter the date you want to look at')
    for i in corona_data:
        if i == country_name:
            for x in corona_data[i]:
                if x['date']==date:
                    return x

if __name__ == "__main__":
    print(general_info())
