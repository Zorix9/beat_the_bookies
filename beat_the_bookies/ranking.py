import pandas as pd
from beat_the_bookies.get_data import get_data
import numpy as np


dic_season ={'09-10':9,'10-11':8,'11-12':7,'12-13':6,'13-14':5,'14-15':4,'15-16':3,'16-17':2,'17-18':1,'18-19':0}

def ranking_per_year(league,season):
    '''
    Compute the classement of every season
    ATTENTION : fct prend rien en paarmètre mais utilise la variable list_df
    '''
    ## doit appeler la fonction get_data()
    list_df = get_data(league)
    df = list_df[dic_season[season]]
    df['Home_point'] = df['FTR'].apply(lambda x: 3 if str(x) == 'H' else (0 if str(x) =='A' else 1))
    df['Away_point'] = df['FTR'].apply(lambda x: 0 if str(x) == 'H' else (3 if str(x)=='A' else 1))

    lst_points = []
    ## loop over the teams
    for item in df['HomeTeam'].unique():
       lst_points.append(df[df['HomeTeam']==item]['Home_point'].sum() + df[df['AwayTeam']==item]['Away_point'].sum())
    # creation of the dataframe with the ranking of each years
    classement = pd.DataFrame(list(zip(df['HomeTeam'].unique(),lst_points)),columns=['team','points'])
    classement = classement.sort_values(by='points',ascending=False).reset_index(drop=True)
    return classement


def ranking_top_five(league,season):
    ## doit appeler la fonction get_data()
    list_df = get_data(league)

    df_classement = ranking_per_year(league,season)
    lst_best_teams = df_classement['team'][0:6]

    df = list_df[dic_season[season]]


def ranking_over_year(league,season):
    '''
    Takes in imput the league and the season
    '''
    list_df = get_data(league)

    df_classement = ranking_per_year(league,season)
    lst_best_teams = df_classement['team'][0:5]

    df2 = list_df[dic_season[season]]

    lst_point_best_teams = []
    for teams in lst_best_teams:
        filter_list = []
        point_list = []
        for index,item in enumerate(df2['HomeTeam']):
            if item == teams:
                filter_list.append(True)
                if df2['FTR'][index] == 'H':
                    point_list.append(3)
                elif df2['FTR'][index] == 'D':
                    point_list.append(1)
                else:
                    point_list.append(0)
            elif df2['AwayTeam'][index] == teams:
                filter_list.append(True)
                if df2['FTR'][index] == 'A':
                    point_list.append(3)
                elif df2['FTR'][index] == 'D':
                    point_list.append(1)
                else:
                    point_list.append(0)
            else:
                filter_list.append(False)
        temp_df = df2[filter_list]
        temp_df['points'] = point_list
        lst_point_best_teams.append(np.cumsum(point_list))
    return pd.DataFrame(dict(zip(lst_best_teams,lst_point_best_teams)))







    return True
