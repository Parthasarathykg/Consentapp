# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 00:30:36 2020

@author: kmjb086
"""


import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Img(src='/assets/doc.png')),
                dbc.Col(html.Img(src='/assets/hca.png')),
                dbc.Col(html.Img(src='/assets/aff.png')),
                dbc.Col(html.Img(src='/assets/location.png')),
                dbc.Col(html.Img(src='/assets/consent.png'))
            ]
        ),
    ]
)

layout = html.Div([ row ])





#if __name__ == "__main__":
 #   app.run_server()