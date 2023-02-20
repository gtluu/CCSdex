import plotly.express as px
from dash import Dash, dcc, html, State, callback_context, dash_table
from dash_extensions.enrich import Input, Output, DashProxy, MultiplexerTransform
import dash_bootstrap_components as dbc
import dash_table
import os
import pandas as pd


def get_table(df, mz=None, mz_tol=None, ccs=None, ccs_tol=None):
    about1 = 'CCSdex is a simple, searchable database developed as a proof of concept using DeepCCS version 1.0 to ' \
             'predict CCS values from The Natural Products Atlas v2021_08. CCS values are predicted for the ' \
             'following adducts: [M+H], [M+Na], [M-H], [M-2H].'
    about2 = 'DISCLAIMER: CCSDEX IS AN UNOFFICIAL DATABASE AND IS IN NO WAY AFFILIATED WITH THE NATURAL PRODUCTS ' \
             'ATLAS OR LININGTON RESEARCH GROUP. FURTHERMORE, DEVELOPMENT HAS CEASED AND ONGOING SUPPORT WILL NOT BE ' \
             'PROVIDED FOR CCSDEX.'
    about3 = 'CCSdex is licensed under a Creative Commons Attribution 4.0 International License.'

    if mz is not None and mz_tol is not None and ccs is not None and ccs_tol is not None:
        df = df.loc[(df['m/z'] >= (float(mz) - float(mz_tol))) &
                    (df['m/z'] <= (float(mz) + float(mz_tol))) &
                    (df['CCS'] >= (float(ccs) - (float(ccs) * (float(ccs_tol) / 100)))) &
                    (DF['CCS'] <= (float(ccs) + (float(ccs) * (float(ccs_tol) / 100))))]
        children = [
            html.Div(
                children=[
                    html.H1('CCSdex')
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    html.P(about1),
                    html.P(about2),
                    html.P(about3)
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    html.H5('m/z'),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    dcc.Input(
                        id='mass',
                        value=mz,
                        type='text'
                    ),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center',
                    'border-color': '#0047AB'
                }
            ),
            html.Div(
                children=[
                    html.H5('m/z Tolerance (Da)'),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    dcc.Input(
                        id='mass_tol',
                        value=mz_tol,
                        type='text'
                    ),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center',
                    'border-color': '#0047AB'
                }
            ),
            html.Div(
                children=[
                    html.H5('CCS'),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    dcc.Input(
                        id='ccs',
                        value=ccs,
                        type='text'
                    ),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center',
                    'border-color': '#0047AB'
                }
            ),
            html.Div(
                children=[
                    html.H5('CCS Tolerance (%)'),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    dcc.Input(
                        id='ccs_tol',
                        value=ccs_tol,
                        type='text'
                    ),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center',
                    'border-color': '#0047AB'
                }
            ),
            html.Div(
                children=[
                    html.Div(
                        html.Button(
                            'Search',
                            id='search'
                        )
                    ),
                ],
                style={
                    'border-radius': '20px',
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '25px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                dash_table.DataTable(data=df.to_dict('records'),
                                     columns=[{'name': i, 'id': i, 'presentation': 'markdown'}
                                              if i == 'NPAID' else {'name': i, 'id': i} for i in df.columns],
                                     id='data',
                                     page_size=50,
                                     style_cell={'textAlign': 'left'},
                                     style_data={'whiteSpace': 'normal',
                                                 'height': 'auto'}),
                style={
                    'position': 'relative',
                    'top': '100px',
                    'font-family': 'Arial'
                }
            )
        ]
    else:
        children = [
            html.Div(
                children=[
                    html.H1('CCSdex')
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    html.P(about1),
                    html.P(about2),
                    html.P(about3)
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    html.H5('m/z'),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    dcc.Input(
                        id='mass',
                        value=mz,
                        type='text'
                    ),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center',
                    'border-color': '#0047AB'
                }
            ),
            html.Div(
                children=[
                    html.H5('m/z Tolerance (Da)'),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    dcc.Input(
                        id='mass_tol',
                        value=mz_tol,
                        type='text'
                    ),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center',
                    'border-color': '#0047AB'
                }
            ),
            html.Div(
                children=[
                    html.H5('CCS'),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    dcc.Input(
                        id='ccs',
                        value=ccs,
                        type='text'
                    ),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center',
                    'border-color': '#0047AB'
                }
            ),
            html.Div(
                children=[
                    html.H5('CCS Tolerance (%)'),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                children=[
                    dcc.Input(
                        id='ccs_tol',
                        value=ccs_tol,
                        type='text'
                    ),
                ],
                style={
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '20px',
                    'width': '1250px',
                    'textAlign': 'center',
                    'border-color': '#0047AB'
                }
            ),
            html.Div(
                children=[
                    html.Div(
                        html.Button(
                            'Search',
                            id='search'
                        )
                    ),
                ],
                style={
                    'border-radius': '20px',
                    'position': 'relative',
                    'top': '50px',
                    'font-family': 'Arial',
                    'font-size': '25px',
                    'width': '1250px',
                    'textAlign': 'center'
                }
            ),
            html.Div(
                dash_table.DataTable(data=df.to_dict('records'),
                                     columns=[{'name': i, 'id': i, 'presentation': 'markdown'}
                                              if i == 'NPAID' else {'name': i, 'id': i} for i in df.columns],
                                     id='data',
                                     page_size=50,
                                     style_cell={'textAlign': 'left'},
                                     style_data={'whiteSpace': 'normal',
                                                 'height': 'auto'}),
                style={
                    'position': 'relative',
                    'top': '100px',
                    'font-family': 'Arial'
                }
            )
        ]
    return children


DF = pd.concat([pd.read_csv('db/npatlas_m_plus_h_predict.csv'),
                pd.read_csv('db/npatlas_m_plus_na_predict.csv'),
                pd.read_csv('db/npatlas_m_minus_h_predict.csv'),
                pd.read_csv('db/npatlas_m_minus_2h_predict.csv')])
DF['NPAID'] = ['[' + i + '](https://www.npatlas.org/explore/compounds/' + i + ')' for i in DF['NPAID'].values.tolist()]

app = DashProxy(prevent_initial_callbacks=True, transforms=[MultiplexerTransform()])

app.layout = html.Div(
    id='app',
    children=get_table(DF)
)


@app.callback(Output('app', 'children'),
              Input('search', 'n_clicks'),
              State('mass', 'value'),
              State('mass_tol', 'value'),
              State('ccs', 'value'),
              State('ccs_tol', 'value'))
def update_table(n_clicks, mass, mass_tol, ccs, ccs_tol):
    changed_id = [i['prop_id'] for i in callback_context.triggered][0]

    if 'search' in changed_id:
        if n_clicks is not None:
            global DF
            return get_table(DF,
                             mz=mass,
                             mz_tol=mass_tol,
                             ccs=ccs,
                             ccs_tol=ccs_tol)


if __name__ == '__main__':
    app.run_server(port=8050)
