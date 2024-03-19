from flask import Flask, request, render_template, session,send_file
import pandas as pd
import io
import warnings
warnings.filterwarnings("ignore")
from flask_pymongo import PyMongo
import bcrypt
import os
import numpy as np
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import plotly
import plotly.graph_objects as px
import plotly.graph_objects as go
import json
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
application= Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
global dfw


@application.route('/')
def home():
    return render_template('home.html')

@application.route('/chart2', methods=['GET', 'POST'])
def upload():
        if request.method == 'POST':
            global dfw
            df = pd.read_csv(request.files.get('file'), skiprows=13, sep=";", header=None)
            df.fillna(0, inplace=True)
            df.replace(['0x', ''], ['', ''], regex=True, inplace=True)
            df.columns = ["Time", "Type", "ID", "DL", "D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]
            df.drop(columns="D8", inplace=True)
            df1 = df[df['ID'].str.contains('101')]
            df2 = df[df['ID'].str.contains('102')]
            df3 = df[df['ID'].str.contains('103')]
            df4 = df[df['ID'].str.contains('104')]
            df5 = df[df['ID'].str.contains('105')]
            df6 = df[df['ID'].str.contains('106')]
            df1['Voltage'] = df1['D0'] + df1['D1']
            df1["Voltage"] = df1["Voltage"].apply(lambda x: str(int(str(x), 16)))
            df1['Voltage'] = df1['Voltage'].astype(float) * 0.001
            df2['102'] = df2['D0'] + df2['D1']
            df2["102"] = df2["102"].apply(lambda x: str(int(str(x), 16)))
            df2['102'] = df2['102'].astype(float) * 0.00
            df3['103'] = df3['D0'] + df3['D1']
            df3["103"] = df3["103"].apply(lambda x: str(int(str(x), 16)))
            df3['103'] = df3['103'].astype(float) * 0.001
            df5['105'] = df5['D1'] + df5['D0']
            df5["105"] = df5["105"].apply(lambda x: str(int(str(x), 16)))
            df5['105'] = df5['105'].astype(float) * 0.001
            df5.rename(columns={'105': 'Voltage'}, inplace=True)
            df6['106'] = df6['D1'] + df6["D0"]
            df6["106"] = df6["106"].apply(lambda x: str(int(str(x), 16)))
            df6['106'] = df6['106'].astype(float) * 0.001
            df6.rename(columns={'106': 'Current'}, inplace=True)
            df7 = df[df['ID'].str.contains('107')]
            df8 = df[df['ID'].str.contains('108')]
            df9 = df[df['ID'].str.contains('109')]
            df10 = df[df['ID'].str.contains('10A')]
            df11 = df[df['ID'].str.contains('10B')]
            df12 = df[df['ID'].str.contains('10C')]
            df13 = df[df['ID'].str.contains('10C')]
            df14 = df[df['ID'].str.contains('115')]
            df15 = df[df['ID'].str.contains('116')]
            df8['108'] = df8['D1'] + df8["D0"]
            df8["108"] = df8["108"].apply(lambda x: str(int(str(x), 16)))
            df8.rename(columns={'108': 'Battery Capacity'}, inplace=True)
            df8['Battery Capacity'] = df8['Battery Capacity'].astype(float) * 0.001
            df8["Battery Health"] = df8["D2"]
            df8["Battery Health"] = df8["Battery Health"].apply(lambda x: str(int(str(x), 16)))
            df8["SOC"] = df8["D3"]
            df8["SOC"] = df8["SOC"].apply(lambda x: str(int(str(x), 16)))
            df5.reset_index(drop=True, inplace=True)
            df6.reset_index(drop=True, inplace=True)
            df8.reset_index(drop=True, inplace=True)
            d1 = df6["Current"]
            data1 = pd.concat([df5, d1], axis=1)
            d2 = df8[["Battery Capacity", "Battery Health", "SOC"]]
            d2.reset_index(drop=True, inplace=True)
            data2 = pd.concat([data1, d2], axis=1)
            df9['V1'] = df9['D1'] + df9['D0']
            df9['V2'] = df9['D3'] + df9['D2']
            df9['V3'] = df9['D5'] + df9['D4']
            df9['V4'] = df9['D7'] + df9['D6']
            df9["V1"] = df9["V1"].apply(lambda x: str(int(str(x), 16)))
            df9["V2"] = df9["V2"].apply(lambda x: str(int(str(x), 16)))
            df9["V3"] = df9["V3"].apply(lambda x: str(int(str(x), 16)))
            df9["V4"] = df9["V4"].apply(lambda x: str(int(str(x), 16)))
            df9['V1'] = df9['V1'].astype(float) * 0.001
            df9['V2'] = df9['V2'].astype(float) * 0.001
            df9['V3'] = df9['V3'].astype(float) * 0.001
            df9['V4'] = df9['V4'].astype(float) * 0.001
            d3 = df9[["V1", "V2", "V3", "V4"]]
            d3.reset_index(drop=True, inplace=True)
            data3 = pd.concat([data2, d3], axis=1)
            df10["V5"] = df10["D1"] + df10["D0"]
            df10["V6"] = df10["D3"] + df10["D2"]
            df10["V7"] = df10["D5"] + df10["D4"]
            df10["V8"] = df10["D7"] + df10["D6"]
            df10["V5"] = df10["V5"].apply(lambda x: str(int(str(x), 16)))
            df10["V6"] = df10["V6"].apply(lambda x: str(int(str(x), 16)))
            df10["V7"] = df10["V7"].apply(lambda x: str(int(str(x), 16)))
            df10["V8"] = df10["V8"].apply(lambda x: str(int(str(x), 16)))
            df10['V5'] = df10['V5'].astype(float) * 0.001
            df10['V6'] = df10['V6'].astype(float) * 0.001
            df10['V7'] = df10['V7'].astype(float) * 0.001
            df10['V8'] = df10['V8'].astype(float) * 0.001
            d4 = df10[["V5", "V6", "V7", "V8"]]
            d4.reset_index(drop=True, inplace=True)
            data4 = pd.concat([data3, d4], axis=1)
            df11["V9"] = df11["D1"] + df11["D0"]
            df11["V10"] = df11["D3"] + df11["D2"]
            df11["V11"] = df11["D5"] + df11["D4"]
            df11["V12"] = df11["D7"] + df11["D6"]
            df11["V9"] = df11["V9"].apply(lambda x: str(int(str(x), 16)))
            df11["V10"] = df11["V10"].apply(lambda x: str(int(str(x), 16)))
            df11["V11"] = df11["V11"].apply(lambda x: str(int(str(x), 16)))
            df11["V12"] = df11["V12"].apply(lambda x: str(int(str(x), 16)))
            df11['V9'] = df11['V9'].astype(float) * 0.001
            df11['V10'] = df11['V10'].astype(float) * 0.001
            df11['V11'] = df11['V11'].astype(float) * 0.001
            df11['V12'] = df11['V12'].astype(float) * 0.001
            d5 = df11[["V9", "V10", "V11", "V12"]]
            d5.reset_index(drop=True, inplace=True)
            data5 = pd.concat([data4, d5], axis=1)
            df12['V13'] = df12['D1'] + df12['D0']
            df12["V13"] = df12["V13"].apply(lambda x: str(int(str(x), 16)))
            df12['V13'] = df12['V13'].astype(float) * 0.001
            d6 = df12["V13"]
            d6.reset_index(drop=True, inplace=True)
            data6 = pd.concat([data5, d6], axis=1)
            data6["Time_stamp"] = data6["Time"] - data6["Time"].shift(1)
            dfw = data6.drop(data6.index[data6['Time_stamp'] < 0])
            dfw["Time_stamp"] = dfw["Time_stamp"].cumsum()
            dfw.drop(columns="Time", inplace=True)
            first_column = dfw.pop('Time_stamp')
            dfw.insert(0, 'Time_stamp', first_column)
            dfw["Time_stamp"]=dfw["Time_stamp"]/60
            plot = px.Figure(data=[go.Scatter(
                name='Voltage',
                x=dfw["Time_stamp"],
                y=dfw["Voltage"], line_color='brown'
            ),
            go.Scatter(
                    name='Current',
                    x=dfw["Time_stamp"],
                    y=dfw["Current"], visible=False, line_color='mediumpurple'),
                go.Scatter(name="Battery Capacity",
                           x=dfw["Time_stamp"],
                           y=dfw["Battery Capacity"], visible=False, line_color='seagreen'),
                go.Scatter(
                    name="Battery Health",
                    x=dfw["Time_stamp"],
                    y=dfw["Battery Health"], visible=False, line_color='red'),
                go.Scatter(
                    name="SOC",
                    x=dfw["Time_stamp"],
                    y=dfw["SOC"], visible=False, line_color='darkred'),
                go.Scatter(
                    x=dfw["Time_stamp"],
                    y=dfw["V1"], visible=False, line_color='darkblue'),
                go.Scatter(
                    x=dfw["Time_stamp"],
                    y=dfw["V2"], visible=False, line_color='orange'),
                go.Scatter(
                    x=dfw["Time_stamp"],

                    y=dfw["V3"], visible=False, line_color='red'),
                go.Scatter(
                    x=dfw["Time_stamp"],

                    y=dfw["V4"], visible=False, line_color='gold'),
                go.Scatter(
                    x=dfw["Time_stamp"],

                    y=dfw["V5"], visible=False, line_color='red'),
                go.Scatter(
                    x=dfw["Time_stamp"],
                    y=dfw["V6"], visible=False, line_color='green'),
                go.Scatter(
                    x=dfw["Time_stamp"],

                    y=dfw["V7"], visible=False, line_color='blue'),
                go.Scatter(
                    x=dfw["Time_stamp"],

                    y=dfw["V8"], visible=False, line_color='gray'),
                go.Scatter(
                    x=dfw["Time_stamp"],

                    y=dfw["V9"], visible=False, line_color='red'),
                go.Scatter(
                    x=dfw["Time_stamp"],
                    y=dfw["V10"], visible=False, line_color='green'),
                go.Scatter(
                    x=dfw["Time_stamp"],

                    y=dfw["V11"], visible=False, line_color='blue'),
                go.Scatter(
                    x=dfw["Time_stamp"],
                    y=dfw["V12"], visible=False, line_color='gray')

            ])

            plot.update_layout(

                updatemenus=[

                    dict(
                        buttons=list([

                            dict(label="Voltage",

                                 method="update",

                                 args=[{"visible": [True, False, False, False, False,False, False, False,False,False, False, False, False, False, False, False, False, False]},

                                       {"title": "Voltage with Respect to Time",
                                        'xaxis': {'title': 'Time(Sec)'},
                                        'yaxis': {'title': 'Voltage(volts)'}

                                        }]),

                            dict(label="Current",

                                 method="update",

                                 args=[{"visible": [False, True, False, False, False,False, False, False,False,False, False, False, False, False, False, False, False, False]},

                                       {"title": "Current with Respect to Time",
                                        'xaxis': {'title': 'Time(Sec)'},
                                        'yaxis': {'title': 'Current(Amps)'}
                                        }]),
                            dict(label="CC-CV charactoristics",

                                 method="update",

                                 args=[{"visible": [True, True, False, False, False, False, False, False, False, False,
                                                    False, False, False, False, False, False, False, False]},

                                       {"title": "Current with Respect to Time",
                                        'xaxis': {'title': 'Time(Sec)'},
                                        'yaxis': {'title': ' Voltage(V) Vs Current(Amps)'},

                                        }]),
                            dict(label="Battery Capacity",

                                 method="update",

                                 args=[{"visible": [False, False, True, False, False,False, False, False,False,False, False, False, False, False, False, False, False, False]},

                                       {"title": "Battery Capacity with Respect to Time",
                                        'xaxis': {'title': 'Time(Sec)'},
                                        'yaxis': {'title': 'Batter Capacity(Ah)'}

                                        }]),
                            dict(label="Battery Health",

                                 method="update",

                                 args=[{"visible": [False, False, False, True, False,False, False, False,False,False, False, False, False, False, False, False, False, False]},

                                       {"title": "Battery Health with Respect to Time",
                                        'xaxis': {'title': 'Time(Sec)'},
                                        'yaxis': {'title': 'Batter Health'}

                                        }]),
                            dict(label="SOC",
                                 method="update",

                                 args=[{"visible": [False, False, False, False, True,False, False, False,False,False, False, False, False, False, False, False, False, False]},

                                       {"title": "SOC with Respect to Time",
                                        'xaxis': {'title': 'Time(Sec)'},
                                        'yaxis': {'title': 'SOC'}

                                        }]),
                            dict(label="individual voltages(V1-V4)",
                                 method="update",

                                 args=[{"visible": [False, False, False, False, False,True,True,True,True,False, False, False, False, False, False, False, False, False]},

                                       {"title": "individual voltages (V1-V4) with Respect to Time",
                                        'xaxis': {'title': 'Time(Sec)'},
                                        'yaxis': {'title': 'individual voltages(v1-v4'}

                                        }]),
                            dict(label="individual voltages(V5-V8)",
                                 method="update",

                                 args=[{"visible": [False, False, False, False, False, False, False, False, False, True,
                                                    True, True, True,False, False, False, False]},

                                       {"title": "individual voltages (V5-V8) with Respect to Time",
                                        'xaxis': {'title': 'Time(Sec)'},
                                        'yaxis': {'title': 'individual voltages(V5-V8'}

                                        }]),
                            dict(label="individual voltages(V9-V12)",
                                 method="update",

                                 args=[{"visible": [False, False, False, False, False, False, False, False, False,
                                                    False, False, False, False, True, True, True, True]},

                                       {"title": "individual voltages (V9-V12) with Respect to Time",
                                        'xaxis': {'title': 'Time(Sec)'},
                                        'yaxis': {'title': 'individual voltages(V9-V12'}

                                        }])


                        ]),

                    )

                ])
            plot.update_layout(
                autosize=False,
                width=1400,
                height=700,plot_bgcolor='rgb(205, 201, 201)')


            graphJSON1 = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)

            return render_template('upload1.html', graphJSON1=graphJSON1,dfw=dfw)
        return render_template('upload1.html')
if __name__ == '__main__':
    application.secret_key = 'mysecret'
    application.run(host='0.0.0.0',port=8080)
