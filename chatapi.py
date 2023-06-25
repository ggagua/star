import openai
import sqlite3
import json
import os
from dotenv import load_dotenv

api_key = os.getenv('API_KEY')
openai.api_key = api_key



conn = sqlite3.connect('swseries.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM swlist")

rows = cursor.fetchall()
def get_sw_series(year):
    namelist = []  # Clear the namelist for each call

    for row in rows:
        if year == row[2]:
            namelist.append(row[1])

    series_dict = {
        'year': year,
        'name': namelist
    }

    return json.dumps(series_dict)





def chat_with_gpt(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        functions=[
            {
                "name": 'get_sw_series',
                "description": "Gets information about which star wars was released on which year",
                "parameters": {
                    "type": "object",
                    "properties": {
                    "year": {
                        "type" : "string",
                        "description" : "Date of year, e.g 2021, 2022, it could also be TBC. TBC indicates the movies that are planned in future but are not given exact date yet."

                    },
                },
                    "required": ["year"]
                }
            }
        ],
        function_call="auto",
    )
    message =  response.choices[0]['message']
    if message.get("function_call"):
        function_name = message["function_call"]["name"]
        function_args = json.loads(message['function_call']['arguments'])
        function_year = function_args['year']
        function_response = get_sw_series(year=function_year)
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
                message,
                {"role": "function",
                 "name": function_name,
                 "content": function_response}
            ],

        )
        return second_response.choices[0].message.content.strip()
    return response.choices[0].message.content.strip()










