# Import required packages
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv("airline_data.csv", 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

app = dash.Dash(__name__)
app.layout = html.Div(children=[html.H1("Airline On-time Performance Dashboard", style = {"textAlign":"center", "color": "#0E0C15", "font-size": 50}), html.P("Proportion of distance group (250 mile distance interval group)  by flights. ", style = {"textAline":"center", "color": '#F57241'}) , dcc.Graph(figure=fig)])
if __name__ == "__main__":
    app.run()



