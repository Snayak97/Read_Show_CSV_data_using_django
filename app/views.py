from django.shortcuts import render
import csv
import requests
from io import StringIO
import json

# Create your views here.

def Show_data(request):
    

  
    url = "https://raw.githubusercontent.com/shaktids/stock_app_test/refs/heads/main/dump.csv"
    
   
    response = requests.get(url)
    csv_data = StringIO(response.text)  

 
    reader = csv.DictReader(csv_data)
    
    companies = []
    data = {}


    for row in reader:
        company_name = row["index_name"]  
        if company_name not in companies:
            companies.append(company_name)

        if company_name not in data:
            data[company_name] = []

        # Append the relevant data
        data[company_name].append({
            "Date": row["index_date"],
            "Open": row["open_index_value"],
            "High": row["high_index_value"],
            "Low": row["low_index_value"],
            "Close": row["closing_index_value"],
        })
    d = {
        'companies': companies,
        'data': json.dumps(data),
    }

    return render(request,"show.html",d)
