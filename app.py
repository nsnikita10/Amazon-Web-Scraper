# -*- coding: utf-8 -*-
"""
Created on May 24 17:39:36 2021

@author: niksingh
"""
#importing libraries 
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

#importing csv file 
data = pd.read_csv('C:\\Users\\niksingh\\Desktop\\Personal data\\Masters\\Projects\\python\\amazon-web-scrapping\\output.csv')

#Data Cleaning - Extracting numeric info
data['Rating'] = data['Overall_Rating'].str.extract(r'(\d+.\d+)').astype('float')
data['Number_of_reviews'] = data['Total_Reviews'].str.extract(r'(\d+.\d+)').astype('float')

#Creating dashboard
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Book Analytics",),
        html.P(
            children="Analyze the best selling books"
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Product_Title"],
                        "y": data["Rating"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Rating of Books"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Product_Title"],
                        "y": data["Number_of_reviews"],
                        "type": "bar",
                    },
                ],
                "layout": {"title": "Average Reviews of Books"},
            },
        ),
    ]

)
    
#Running server
if __name__ == "__main__":
    app.run_server(port=8050,host='0.0.0.0')



