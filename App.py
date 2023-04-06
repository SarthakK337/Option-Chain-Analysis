import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash import Input, Output, dcc, html
from sklearn import datasets
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


from StrategyBuilder import Strategys , ShortIronCondor
from StratergyPlot1 import StrategyPloter

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
s = Strategys()
data = s.option_chain_data("NIFTY")
data['New_expiryDate']=pd.to_datetime(data['expiryDate'])
data=data.sort_values(by='New_expiryDate').reset_index().drop(columns="index")


main = dbc.Card([
            html.Div(
                dcc.Dropdown(
                    id='Nifty',
                    options=[
                        {
                            "label": html.Div(['Nifty 50'], style={'color': 'MediumTurqoise', 'font-size': 13}),
                            "value": "NIFTY",
                        },
                        {
                            "label": html.Div(['Bank Nifty'], style={'color': 'MediumTurqoise', 'font-size': 13}),
                            "value": "BANKNIFTY",
                        }

                    ], value='NIFTY'
                )
            )
        ])

BS1 = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("B/S"),
                dcc.Dropdown(["B","S"],  id='B/S1',value="B")
            ]

        )

    ],
    body=True,
)

BS2 = dbc.Card(
    [
        html.Div(
            [
                dcc.Dropdown(["B","S"],  id='B/S2',value="B")
            ]

        )

    ],
    body=True,
)

BS3 = dbc.Card(
    [
        html.Div(
            [
                dcc.Dropdown(["B","S"],  id='B/S3',value="B")
            ]

        )

    ],
    body=True,
)

BS4 = dbc.Card(
    [
        html.Div(
            [
                dcc.Dropdown(["B","S"],  id='B/S4',value="B")
            ]

        )

    ],
    body=True,
)


Strike1 = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Strike"),
                dcc.Input(
                    id="Strike1", type="number",
                    step=50
                )
            ]

        )

    ],
    body=True,
)

Strike2 = dbc.Card(
    [
        html.Div(
            [
                dcc.Input(
                    id="Strike2", type="number",
                    step=50
                )
            ]

        )

    ],
    body=True,
)

Strike3 = dbc.Card(
    [
        html.Div(
            [
                dcc.Input(
                    id="Strike3", type="number",
                    step=50
                )
            ]

        )

    ],
    body=True,
)

Strike4 = dbc.Card(
    [
        html.Div(
            [
                dcc.Input(
                    id="Strike4", type="number",
                    step=50
                )
            ]

        )

    ],
    body=True,
)

CP1 = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("CE/PE"),
                dcc.Dropdown(["C", "P"], id='CE/PE1', value='C')
            ]

        )

    ],
    body=True,
)

CP2 = dbc.Card(
    [
        html.Div(
            [
                dcc.Dropdown(["C", "P"], id='CE/PE2', value='C')
            ]

        )

    ],
    body=True,
)

CP3 = dbc.Card(
    [
        html.Div(
            [
                dcc.Dropdown(["C", "P"], id='CE/PE3', value='C')
            ]

        )

    ],
    body=True,
)

CP4 = dbc.Card(
    [
        html.Div(
            [
                dcc.Dropdown(["C", "P"], id='CE/PE4', value='C')
            ]

        )

    ],
    body=True,
)

Lots1 = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Lots"),
                dcc.Input(
                    id="Lots1", type="number",
                    min=1, step=1, value=1
                )
            ]

        )

    ],
    body=True,
)

Lots2 = dbc.Card(
    [
        html.Div(
            [
                dcc.Input(
                    id="Lots2", type="number",
                    min=1, step=1, value=1
                )
            ]

        )

    ],
    body=True,
)

Lots3 = dbc.Card(
    [
        html.Div(
            [
                dcc.Input(
                    id="Lots3", type="number",
                    min=1, step=1, value=1
                )
            ]

        )

    ],
    body=True,
)

Lots4 = dbc.Card(
    [
        html.Div(
            [
                dcc.Input(
                    id="Lots4", type="number",
                    min=1, step=1, value=1
                )
            ]

        )

    ],
    body=True,
)

Expiry1 = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Expiry"),
                dcc.Dropdown(
                    id="Expiry1",
                    options=[
                        {"label": i, "value": i} for i in data["expiryDate"].unique()
                    ],
                    value=data["expiryDate"].unique()[0],
                )
            ]

        )

    ],
    body=True,
)


Expiry2 = dbc.Card(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="Expiry2",
                    options=[
                        {"label": i, "value": i} for i in data["expiryDate"].unique()
                    ],
                    value=data["expiryDate"].unique()[0],
                )
            ]

        )

    ],
    body=True,
)

Expiry3 = dbc.Card(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="Expiry3",
                    options=[
                        {"label": i, "value": i} for i in data["expiryDate"].unique()
                    ],
                    value=data["expiryDate"].unique()[0],
                )
            ]

        )

    ],
    body=True,
)

Expiry4 = dbc.Card(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="Expiry4",
                    options=[
                        {"label": i, "value": i} for i in data["expiryDate"].unique()
                    ],
                    value=data["expiryDate"].unique()[0],
                )
            ]

        )

    ],
    body=True,
)




# app.layout = dbc.Container(
#     [
#         html.H1("Option Chain Analysis"),
#         html.Hr(),
#         dbc.Row(
#             [
#                 dbc.Row(main),
#                 html.Hr(),
#                 dbc.Row(
#                     [
#                         dbc.Col(BS,sm=2),
#                         dbc.Col(Strike, sm=2),
#                         dbc.Col(CP, sm=2),
#                         dbc.Col(Lots, sm=2),
#                         dbc.Col(Expiry, sm=2)
#                     ]
#                 ),
#                 # dbc.Col(controls1, md=1),
#                 dbc.Col(dcc.Graph(id = "cluster-graph")),
#                 # dbc.Col(dcc.Graph())
#             ],
#             align="center",
#         ),
#     ],
#     fluid=True,
# )

app.layout= html.Div([
    html.Div([
        html.H1("Option Chain Analysis"),
        html.Hr(),
        dbc.Row(main),
        dbc.Row([
            dbc.Col([
                dbc.Row([BS1]),
                dbc.Row([BS2]),
                dbc.Row([BS3]),
                dbc.Row([BS4])],sm=2),
            dbc.Col([
                dbc.Row([Strike1]),
                dbc.Row([Strike2]),
                dbc.Row([Strike3]),
                dbc.Row([Strike4])],sm=2),
            dbc.Col([
                dbc.Row([CP1]),
                dbc.Row([CP2]),
                dbc.Row([CP3]),
                dbc.Row([CP4])],sm=2),
            dbc.Col([
                dbc.Row([Lots1]),
                dbc.Row([Lots2]),
                dbc.Row([Lots3]),
                dbc.Row([Lots4])], sm=2),
            dbc.Col([
                dbc.Row([Expiry1])], sm=2)
        ])
    ],style={'background-color': '#92a8d1',
             'width': '40%',
             'float': 'left',
            'padding': '7px'
    }),
    html.Div([
        dcc.Graph(id = "cluster-graph")
    ],id='visualisation',
        style={'background-color': '#708090	',
               'width': '60%',
               'float': 'left',
               'padding': '7px'
               }
    )

])


@app.callback([
    Output("cluster-graph", "figure")
            ],[
                Input("Nifty", "value"),
                Input("Strike1", "value"),
                Input("Strike2", "value"),
                Input("Strike3", "value"),
                Input("Strike4", "value"),
                Input("Lots1", "value"),
                Input("Lots2", "value"),
                Input("Lots3", "value"),
                Input("Lots4", "value"),
                Input("B/S1", "value"),
                Input("B/S2", "value"),
                Input("B/S3", "value"),
                Input("B/S4", "value"),
                Input("CE/PE1", "value"),
                Input("CE/PE2", "value"),
                Input("CE/PE3", "value"),
                Input("CE/PE4", "value"),
                Input("Expiry1", "value")
              ],
    prevent_initial_call=True
)

def make_graph(Index, Strike1, Strike2, Strike3, Strike4, Lots1, Lots2, Lots3, Lots4, BS1, BS2, BS3, BS4, CE1, CE2, CE3, CE4, Expiry1):
    a = ShortIronCondor()
    s = StrategyPloter()
    if Index=="NIFTY":
        Lots1 = Lots1 * 50
        Lots2 = Lots2 * 50
        Lots3 = Lots3 * 50
        Lots4 = Lots4 * 50
    if Index=="BANKNIFTY":
        Lots1 = Lots1 * 25
        Lots2 = Lots2 * 25
        Lots3 = Lots3 * 25
        Lots4 = Lots4 * 25


    op_list=[
        {'op_type': CE1, 'strike': Strike1, 'tr_type': BS1, 'op_pr': a.CallPrice(Index,Expiry1,Strike1) if CE1=="C" else a.PutPrice(Index,Expiry1,Strike1),'contract': Lots1},
        {'op_type': CE2, 'strike': Strike2, 'tr_type': BS2, 'op_pr': a.CallPrice(Index,Expiry1,Strike2) if CE2=="C" else a.PutPrice(Index,Expiry1,Strike2),
         'contract': Lots2},
        {'op_type': CE3, 'strike': Strike3, 'tr_type': BS3, 'op_pr': a.CallPrice(Index,Expiry1,Strike3) if CE3=="C" else a.PutPrice(Index,Expiry1,Strike3),
         'contract': Lots3},
        {'op_type': CE4, 'strike': Strike4, 'tr_type': BS4, 'op_pr': a.CallPrice(Index,Expiry1,Strike4) if CE4=="C" else a.PutPrice(Index,Expiry1,Strike4),
         'contract': Lots4}
    ]
    x,y=s.multi_plotter(spot=a.StrikePrice(Index, Expiry1), op_list=op_list)
    df = pd.DataFrame({"x": x, "y": y})
    fig = px.line(df, x="x", y="y")
    fig.add_hline(y=0)
    fig.add_vline(x=a.StrikePrice(Index, Expiry1), line_dash="dash", line_color="red")
    fig.add_trace(go.Scatter(x=df["x"], y=[0]*len(df["x"]), fill='tozeroy'))  # fill down to xaxis
    fig.add_trace(go.Scatter(x=df["x"], y=df["y"], fill='tonexty'))  # fill to trace0 y

    # fig = [
    #     px.scatter(df, x="x", y="y", size_max=60)
    # ]
    # fig1=[
    #     sns.lineplot(x=x, y=y, label='combined', alpha=1, color='k')
    # ]
    fig.update_layout(showlegend=False)
    return [fig]

@app.callback([
    Output("Strike1", "value"),
    Output("Strike2", "value"),
    Output("Strike3", "value"),
    Output("Strike4", "value")
            ],[
    Input("Nifty", "value")
])

def update_strike(Index):
    s = Strategys()
    value=s.StrikePrice1(Index)
    value=round(value/100,0)*100
    return (int(value),int(value),int(value),int(value))

if __name__ == "__main__":
    app.run_server(debug=True, port=8008)