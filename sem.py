import pandas as pd
import plotly.graph_objects as go

from collections import defaultdict
dp = pd.read_excel(r"C:\Users\hp\Documents\ProgressTracker\ProgressTrackerData.xlsx",'Sheet2',header=[0,1])
df = pd.read_excel(r"C:\Users\hp\Documents\ProgressTracker\ProgressTrackerData.xlsx",'Sheet2',header=[0,1])
dh = pd.read_excel(r"C:\Users\hp\Documents\ProgressTracker\ProgressTrackerData.xlsx",'Sheet2',skiprows=1)
fig = go.Figure()
category = defaultdict(list) #list of dictionary
for i in (df.columns):
    category[i[0]].append(i[1])# appends first row i.e semesters and subjects
print(category)
del category['Names']
del category['Rollno']

field_values = [i for i, j in category.items()]  # contains semester1...

btn_dropdown = []
student_list = []

for i in range(len(df['Names']['Unnamed: 1_level_1'])):
    student_list.append(df['Names']['Unnamed: 1_level_1'][i])

subjects=[]
for i,j in category.items():
    for k in j:
        if(k=='SGPA'):
            continue
        subjects.append(k)

def set_color(b):#SGPA
    a=int(b)
    if(a>=75):
        return "rgb(50,205,50)"
    elif(a>=50 and a<75):
        return "rgb(255,120,80)"
    elif(a>=30 and a<50):
        return "rgb(65,105,225)"
    elif(a<30):
        return 'red'
    return 'black'

def setcolor(b):#MARKS
    if(b=="RE"):
        a=0
    else:
        a=float(b)
    if(a>=8.5):
        return "rgb(50,205,50)"
    elif(a>=7.5 and a<8.5):
        return "rgb(255,120,80)"
    elif(a<7.5):
        return "rgb(65,105,225)"
    
    return "black"

fig.add_trace(go.Bar(

    orientation='h',
    y=student_list,x=df['Semester1']['SGPA'],
    text=df['Semester1']['SGPA'],
    textposition='outside',
    marker=dict(color=list(map(setcolor,df['Semester1']['SGPA'].values))),
    visible=True,
   
))

# Semester wise result
for jio in field_values:
    res_x=[]
    for i in df[jio]['SGPA']:
        if not pd.isna(i) and i!='RE':
            res_x.append(i)
        else:
            res_x.append(0)
    
    btn_dropdown.append(dict(method='update',
                             label=jio,
                             visible=True,
                             args=[{
                                 'y': [student_list],
                                 'x': [res_x],
                                 'visible': [True],
                                 'text':[res_x],
                                 'marker':dict(color=list(map(setcolor,res_x))),
                                 'textposition':'outside',
                             }, {'title': 'B.Tech IT Result Analysis- ' + jio, 'yaxis': {'title': 'Students Name'},
                                 'xaxis': {'title': 'SGPA'}
                                 }]
                             )
                        )



new =defaultdict()
for i in range(len(student_list)):
    category2 = defaultdict()
    for j in subjects:
        category2[j]=dh[j][i] if (dh[j][i]!='AB') and (dh[j][i]!='RE') else 0
    new[student_list[i]]=category2

new2 = defaultdict()
for j in subjects:
    category2 = defaultdict()
    for i in range(len(student_list)):
        category2[student_list[i]]=dh[j][i] if (dh[j][i]!='AB') and (dh[j][i]!='RE') else 0
    new2[j] = category2


field_values2 = [i for i, j in new.items()]
btn_dropdown2 =[]

for jio in field_values2:
    res_x=[]
    for i,j in new[jio].items():
        res_x.append(j)
    
    btn_dropdown2.append(dict(method='update',
                             label=jio,
                             visible=True,
                             args=[{
                                 'y': [subjects],
                                 'x': [res_x],
                                 'visible': [True],
                                 'text':[res_x],
                                 'textposition':'outside',
                                 'marker':dict(color=list(map(set_color,res_x))),
                             }, {'title': 'Marks of ' + jio +' in various Subjects', 'yaxis': {'title': 'Subjects Name'},
                                 'xaxis': {'title': 'Student Report Sheet'}
                                 }]
                             )
                        )


field_values3 = [i for i, j in new2.items()]
btn_dropdown3 =[]

for jio in field_values3:
    res_x=[]
    for i,j in new2[jio].items():
        res_x.append(j)
    btn_dropdown3.append(dict(method='update',
                             label=jio,
                             visible=True,
                             args=[{
                                 'y': [student_list],
                                 'x': [res_x],
                                 'visible': [True],
                                 'text':[res_x],
                                 'textposition':'outside',
                                 'marker':dict(color=list(map(set_color,res_x))),
                             }, {'title': 'Marks List of ' + jio , 'yaxis': {'title': 'Students Name'},
                                 'xaxis': {'title': 'Student Report Sheet'}
                                 }]
                             )
                        )


updatemenus = []
updatemenus.append(dict())
updatemenus[0]['buttons'] = btn_dropdown
updatemenus[0]['type'] = 'dropdown'
updatemenus[0]['direction'] = 'down'
updatemenus[0]['x'] = -0.25
updatemenus[0]['y'] = 1.4



updatemenus.append(dict())
updatemenus[1]['buttons'] = btn_dropdown2
updatemenus[1]['type'] = 'dropdown'
updatemenus[1]['direction'] = 'down'
updatemenus[1]['x'] = -0.25
updatemenus[1]['y'] = 1.5


updatemenus.append(dict())
updatemenus[2]['buttons'] = btn_dropdown3
updatemenus[2]['type'] = 'dropdown'
updatemenus[2]['direction'] = 'down'
updatemenus[2]['x'] = -0.25
updatemenus[2]['y'] = 1.6


fig.layout.update(updatemenus=updatemenus)
fig.update_layout(barmode="relative",height=1000,title_text='B.Tech IT Result Analysis- Semester1',title_y=0.9,title_x=0.5,annotations=[
        dict( text='<b>Good Performance</b>', bgcolor='lightgreen',align='left',
              xref='paper',
              yref='paper',
              showarrow=False,
              x=1.0,
              y=1.5,
              bordercolor='black', borderwidth=1
            ),
        dict( text='<b>Can Do better</b>', bgcolor='rgb(255,120,80)',align='left',
              xref='paper',
              yref='paper',
              showarrow=False,
              x=1.0,
              y=1.4,
              bordercolor='black', borderwidth=1
            ),
        dict( text='<b>Needs Improvement</b>', bgcolor='rgb(65,105,225)',align='left',
              xref='paper',
              yref='paper',
              showarrow=False,
              x=1.0,
              y=1.3,
              bordercolor='black', borderwidth=1
            ),
        dict( text='<b>Fail</b>', bgcolor='red',align='left',
              xref='paper',
              yref='paper',
              showarrow=False,
              x=1.0,
              y=1.2,
              bordercolor='black', borderwidth=1
            )
    ])

fig.show()
