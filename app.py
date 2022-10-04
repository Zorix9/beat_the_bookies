import streamlit as st
import os
import pandas as pd
from beat_the_bookies.ranking import ranking_per_year,ranking_over_year
from beat_the_bookies.pie_fault import get_card
from beat_the_bookies.pie_shots import get_shot


list_league = ['BundesLiga','LIGA','Ligue1','PL','SerieA']

dic_season ={'09-10':9,'10-11':8,'11-12':7,'12-13':6,'13-14':5,'14-15':4,'15-16':3,'16-17':2,'17-18':1,'18-19':0}


@st.cache
def get_select_box(league,season):
    return ranking_per_year(league,season)

@st.cache
def get_pie_fault(league,season):
    return get_card(league,season)


option1 = st.selectbox('Select a league : ',list_league)
option2 = st.selectbox('Select a season : ',list(dic_season.keys()))

df_classement = get_select_box(option1,option2)
fig = get_card(option1,option2)
fig_shot = get_shot(option1,option2)
df_best_team = ranking_over_year(option1,option2)



## just to try to put two stuff side by side
a1,a2 = st.columns(2)
a1.write(df_classement)
direction = a2.radio('Select a direction', ('Shots stats', 'Cards stats'))
if direction == 'Cards stats':
    a2.plotly_chart(fig)
else:
    a2.plotly_chart(fig_shot)

st.line_chart(df_best_team)
