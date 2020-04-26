import json
from datetime import date 
with open('timeseries.json') as f:
      corona_data = json.load(f)


 
def numOfDays(date1, date2): 
    date_difference=(date2-date1).days 
    return date_difference

def increasing_rate():
    country_name= input('Please enter the country you want to see the rate')
    start_date=input('Please enter the start date')
    final_date=input('Please enter the final date')
    start_date_year=int(start_date.split('-')[0])
    start_date_month=int(start_date.split('-')[1])
    start_date_day=int(start_date.split('-')[2])
    final_date_year=int(final_date.split('-')[0])
    final_date_month=int(final_date.split('-')[1])
    final_date_day=int(final_date.split('-')[2])
    
    for i in corona_data:
        if i == country_name:
            for x in corona_data[i]:
                if x['date']==start_date:
                    a=int(x['confirmed'])
                elif x['date']==final_date:
                    b=int(x['confirmed'])
                    break
    confirmed_difference=b-a
    
    date1 = date(start_date_year, start_date_month, start_date_day) 
    date2 = date(final_date_year, final_date_month, final_date_day) 
    day_difference = numOfDays(date1, date2) 
    average_rate=confirmed_difference/day_difference
    
    return 'There is an average increasing rate of' + str(average_rate) + ' people per day in between this time slot you chose'

if __name__ == "__main__":
    print(increasing_rate())