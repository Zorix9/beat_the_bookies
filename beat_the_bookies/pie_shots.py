import pandas as pd
from beat_the_bookies.get_data import get_data
import plotly.express as px


def get_shot(league,season):
    list_shot = ['Goals','Shots on target','Shots']
    dic_season ={'09-10':9,'10-11':8,'11-12':7,'12-13':6,'13-14':5,'14-15':4,'15-16':3,'16-17':2,'17-18':1,'18-19':0}
    list_df = get_data(league)
    df = list_df[dic_season[season]]
    match_num = len(df['HS'])

    lst = []
    lst.append((df['FTHG'].sum()+df['FTAG'].sum())/match_num)
    lst.append((df['HST'].sum()+df['AST'].sum() - lst[0])/match_num)
    lst.append((df['HS'].sum()+df['AS'].sum() - lst[0] - lst[1])/match_num)

    df_final = pd.DataFrame(columns=list_shot)
    df_final.loc[0] = lst

    fig = px.pie(df_final, values = df_final.loc[0], names=df_final.columns, title='Goals, shots on target and shots')
    return fig
