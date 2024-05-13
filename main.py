import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()  # This reads the .env file
expenses_key = os.environ.get('EXPENSES_KEY')
database_id = os.environ.get('DATABASE_ID')

headers = {
    "Authorization": "Bearer " + expenses_key,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

cycles: dict = {
    "id1": "",
    "name1": "1st Cycle",
    "id2": "",
    "name2": "2nd Cycle",
    "id3": "",
    "name3": "3rd Cycle",
    "id4": "",
    "name4": "4th Cycle"
}

variablesPreDefined: dict = {
    "yearID": "",
    "yearPropName": "2024",
    "situationID": "",
    "situationPropName": "Quitado"
}

def createDataParameter(yearID, yearPropName, cycleID, cyclePropName, month, 
                        description, total, expanseType, typeFixedOrVariable, 
                        targetValue, associationID, associationPropName, 
                        situationID, situationPropName):
    return
    

def create_page(dataParameter: dict):
    create_url = "https://api.notion.com/v1/pages"
    
    payload = {
        "parent": {"database_id": database_id},
        "properties": dataParameter
    }
    
    result = requests.post(create_url, headers=headers, json=payload)
    print(result.status_code)
    return result

dataParameters: dict = {
    'year': '2024',
    'cycle': '3rd Cycle',
    'month': 'May',
    'description': 'Teste'
}

dataFormated = {}

# create_page(dataFormated);

#==========================================================================
# Retrieve the database schema:

def get_pages():
    import json
    
    url = "https://api.notion.com/v1/databases/" + database_id + "/query";
    
    payload = {"page_size": 10};
    response = requests.post(url, headers=headers, json=payload);
    
    data = response.json();
    with open( 'db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    return data['results']

get_pages();
    