import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''
#1
def csv_to_df(path : str = "StudentsPerformance.csv")->pd.DataFrame:
    df = pd.read_csv(path)
    return df
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''
#2
def capitalize_columns(df_data :pd.DataFrame = csv_to_df())->pd.DataFrame:
    df_data_capitalized = df_data.copy()
    df_data_capitalized.columns = [col if 'e' in col else col.upper() for col in df_data_capitalized.columns]
    return df_data_capitalized


'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

#3
def math_passed_count(df_data : pd.DataFrame = csv_to_df()) -> int:
    df = df_data.copy()
    return len(df[df['math score'] >= 50])

'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

#4
def did_pre_course(df_data : pd.DataFrame = csv_to_df()) -> pd.DataFrame:
    df=df_data.copy()
    return pd.DataFrame(df[df["test preparation course"]=="completed"])

'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''
#5!
def average_scores(df_data : pd.DataFrame = csv_to_df()) -> pd.DataFrame:
    dataframe = df_data.copy()
    dataframe = dataframe.groupby(['parental level of education'])['math score','reading score','writing score'].mean()
    return dataframe

'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''
#6
def add_age(df_data : pd.DataFrame = csv_to_df()) -> pd.DataFrame:
    df = df_data.copy()
    df['age'] = ''
    np.random.seed(42)
    for i in range(len(df)):
        df['age'][i] = np.random.randint(low=18,high=67)
    return df


'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''
#7
def female_top_score(df_data : pd.DataFrame = csv_to_df()) -> pd.DataFrame:
    new_df = df_data.copy()
    best = 0
    for i in range(len(new_df)):
        if new_df['gender'][i] == 'female' and new_df['math score'][best] < new_df['math score'][i] and new_df['reading score'][best] < new_df['reading score'][i] and new_df['writing score'][best] < new_df['writing score'][i]:
            best = i
    return (new_df['math score'][best],new_df["reading score"][best],new_df["writing score"][best])


'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''
#8
def add_grade(df : pd.DataFrame = csv_to_df()) -> pd.DataFrame:
    new_df = df.copy()
    new_df['grade'] = ''
    for i in range(len(new_df)):
        min = ((new_df['math score'][i] + new_df['reading score'][i] + new_df['writing score'][i]) / 300)
        if min < 0.6:
            new_df['grade'][i] = 'F'
        elif min >= 0.6 and min < 0.7:
            new_df['grade'][i] = 'D'
        elif min >= 0.7 and min < 0.8:
            new_df['grade'][i] = 'C'
        elif min >= 0.8 and min < 0.9:
            new_df['grade'][i] = 'B'
        elif min >= 0.9:
            new_df['grade'][i] = 'A'
    return new_df

'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''
#9
def math_bar_plot(df : pd.DataFrame = csv_to_df()):
    new_df = df.copy()
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    grouped = new_df.groupby('gender')['math score'].mean()
    ax.bar(grouped.index,grouped.values)
    ax.set_ylabel('Math Score')
    ax.set_xlabel('Gender')
    return fig

''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''
#10
def writing_hist(df:pd.DataFrame = csv_to_df()):
    new_df = df.copy()
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.hist(new_df['writing score'])
    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Writing Score')
    return fig
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''
#11
def ethnicity_pie_chart(df : pd.DataFrame = csv_to_df()):
    new_df = df.copy()
    fig,ax = plt.subplots()
    grouped = new_df.groupby(['race/ethnicity'])['race/ethnicity'].count()
    ax.pie(grouped,labels=grouped.index,autopct='%1.1f%%')
    return fig
