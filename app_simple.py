import streamlit as st
import os
import pandas as pd

directory_in_str = 'raw_data/LIGA'
directory = os.fsencode(directory_in_str)

list_df = [ pd.read_csv(directory_in_str+'/'+os.fsdecode(file)) for file in os.listdir(directory) if os.fsdecode(file).endswith('.csv')]

for df in list_df:
    df['Home_point'] = df['FTR'].apply(lambda x: 3 if str(x) == 'H' else (0 if str(x) =='A' else 1))
    df['Away_point'] = df['FTR'].apply(lambda x: 0 if str(x) == 'H' else (3 if str(x)=='A' else 1))

def classment_per_year():
    '''
    Compute the classement of every season
    ATTENTION : fct prend rien en paarmètre mais utilise la variable list_df
    '''
    list_df_classement = []
    for df in list_df:
        lst_points = []

        for item in df['HomeTeam'].unique():
           lst_points.append(df[df['HomeTeam']==item]['Home_point'].sum() + df[df['AwayTeam']==item]['Away_point'].sum())

        classement = pd.DataFrame(list(zip(df['HomeTeam'].unique(),lst_points)),columns=['team','points'])
        classement = classement.sort_values(by='points',ascending=False).reset_index(drop=True)
        list_df_classement.append(classement)
    return list_df_classement

test_classement = classment_per_year()
list_season = [0,1,2,3,4]

option = st.selectbox('Select a season :', list_season)
filtered_df = test_classement[option]
st.write(filtered_df)
