import streamlit as st
import os
import pandas as pd
from beat_the_bookies.ranking import ranking_per_year

list_league = ['BundesLiga','LIGA','Ligue1','PL','SerieA']

dic_season ={'09-10':9,'10-11':8,'11-12':7,'12-13':6,'13-14':5,'14-15':4,'15-16':3,'16-17':2,'17-18':1,'18-19':0}


@st.cache
def get_select_box(league):
    return ranking_per_year(league)


option1 = st.selectbox('Select a league : ',list_league)
option2 = st.selectbox('Select a season : ',list(dic_season.keys()))
list_df = get_select_box(option1)

#st.write(list_df[dic_season[option2]])

## just to try to put two stuff side by side
a1,a2 = st.columns(2)
a1.write(list_df[dic_season[option2]])
a2.write(list_df[dic_season[option2]])
