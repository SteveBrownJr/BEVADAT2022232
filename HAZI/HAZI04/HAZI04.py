import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def csv_to_df(path):
    df = pd.read_csv(path)
    return df

def capitalize_columns(df):
    new_df = df.copy()
    for column in new_df:
        if not ('e' in column):
           new_df = new_df.rename(columns={column : column.upper()})
    return new_df

def math_passed_count(df):
    new_df = df.copy()
    passedcount = 0
    for index,row in new_df.iterrows():
        if row['math score'] >= 50:
            passedcount = passedcount+1
    return passedcount

def did_pre_course(df):
    new_df = df.copy()
    subset = new_df[new_df['test preparation course'] == "completed"]
    return subset

def average_scores(df):
    new_df = df.copy()
    grouped = new_df.groupby(['parental level of education'])['math score','reading score','writing score'].mean()
    return grouped

def add_age(df):
    new_df = df.copy()  
    np.random.seed(42)  
    new_df['age'] = np.random.randint(18,67,new_df.shape[0])
    return new_df

def female_top_score(df):
    new_df = df.copy()
    best = 0
    for i in range(len(new_df)):
        if new_df['gender'][i] == 'female' and (new_df['math score'][best]+new_df['writing score'][best]+new_df['reading score'][best]) < (new_df['math score'][i] + new_df['writing score'][i] + new_df['reading score'][i]):
            best = i
    return (new_df['math score'][best],new_df["reading score"][best],new_df["writing score"][best])

def add_grade(df):
    new_df = df.copy()
    new_df['grade'] = ''
    for i in range(len(new_df)):
        perc = ((new_df['math score'][i] + new_df['reading score'][i] + new_df['writing score'][i]) / 300)
        if perc < 0.6:
            new_df['grade'][i] = 'F'
        elif perc >= 0.6 and perc < 0.7:
            new_df['grade'][i] = 'D'
        elif perc >= 0.7 and perc < 0.8:
            new_df['grade'][i] = 'C'
        elif perc >= 0.8 and perc < 0.9:
            new_df['grade'][i] = 'B'
        elif perc >= 0.9:
            new_df['grade'][i] = 'A'
    return new_df

def math_bar_plot(df):
    new_df = df.copy()
    fig,ax = plt.subplots()
    grouped = new_df.groupby('gender')['math score'].mean()
    ax.bar(grouped.index,grouped.values)
    ax.set_ylabel('Math Score')
    ax.set_xlabel('Gender')
    ax.set_title('Average Math Score by Gender')
    return fig

def writing_hist(df):
    new_df = df.copy()
    fig,ax = plt.subplots()
    ax.hist(new_df['writing score'])
    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Writing Score')
    ax.set_title('Distribution of Writing Scores')
    return fig

def ethnicity_pie_chart(df):
    new_df = df.copy()
    fig,ax = plt.subplots()
    grouped = new_df.groupby(['race/ethnicity'])['race/ethnicity'].count()
    ax.set_title('Proportion of Students by Race/Ethnicity')
    ax.pie(grouped,labels=grouped.index,autopct='%1.1f%%')
    return fig