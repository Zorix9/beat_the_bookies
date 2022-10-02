import pandas as pd
from beat_the_bookies.get_data import get_data



def ranking_per_year(league):
    '''
    Compute the classement of every season
    ATTENTION : fct prend rien en paarmètre mais utilise la variable list_df
    '''
    ## doit appeler la fonction get_data()
    list_df = get_data(league)

    ## compute the points of every match for the away team and the home team
    # in new columns for each season
    for df in list_df:
        df['Home_point'] = df['FTR'].apply(lambda x: 3 if str(x) == 'H' else (0 if str(x) =='A' else 1))
        df['Away_point'] = df['FTR'].apply(lambda x: 0 if str(x) == 'H' else (3 if str(x)=='A' else 1))
    ## compute the ranking for each year
    list_df_classement = []
    for df in list_df:
        lst_points = []
        ## loop over the teams
        for item in df['HomeTeam'].unique():
           lst_points.append(df[df['HomeTeam']==item]['Home_point'].sum() + df[df['AwayTeam']==item]['Away_point'].sum())
        # creation of the dataframe with the ranking of each years
        classement = pd.DataFrame(list(zip(df['HomeTeam'].unique(),lst_points)),columns=['team','points'])
        classement = classement.sort_values(by='points',ascending=False).reset_index(drop=True)
        list_df_classement.append(classement)
    return list_df_classement
