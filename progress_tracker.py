import pandas as pd
import plotly.graph_objects as go
from collections import defaultdict

dp = pd.read_excel(r"C:\Users\hp\Downloads\ProgressTrackerData.xlsx")
df = pd.read_excel(r"C:\Users\hp\Downloads\ProgressTrackerData.xlsx")
fig=go.Figure()
df=df.sort_values('Target Date')
fig.add_trace(go.Bar(
   
    orientation='h',
    visible=False,
    marker_color= 'rgb(50,205,50)',
  
     
))
fig.add_trace(go.Bar(
   
    orientation='h',
    visible=False,
    marker_color= 'rgb(255,0,0)',
  
     
))



category=defaultdict(list)
for i in range(len(dp['Fields'])):
    a=dp['Fields'][i].split(',')
    a=[i.replace(' ','') for i in a]
    for j in a:
        category[j].append((dp['Tracks'][i],dp['Percentage Completion'][i]))

print(category)

field_values=[ i for i,j  in category.items()]

btn_dropdown=[]
for jio in field_values:
    res=[ v[0] for v in category.get(jio,[])]
    res_x=[ v[1] for v in category[jio] ]
    pending_x=[100-x for x in res_x]
    print(res_x)
    btn_dropdown.append( dict(method='update',
                              label= jio,
                              visible= True,
                              args=[{
                                  'y':[res],
                                  'x':[res_x,pending_x],
                                  'visible': [True,True],
                                  'type': 'bar',
                                  'text': [res_x,pending_x],
                                  'textposition': 'auto',
                                
                                  },{'title': 'Completion status of '+ jio,'yaxis':{'title': 'TASKS'}, 'xaxis':{'title': 'Percentage Completion'}
                                  }]
                              )
                         )

updatemenus=[]
updatemenus.append(dict())
updatemenus[0]['buttons']=btn_dropdown
updatemenus[0]['type']='dropdown'
updatemenus[0]['direction']='down'
updatemenus[0]['x']=-0.25
updatemenus[0]['y']=1.3
btn=[]
btn.append(dict(method='update',
                              label= 'Track Progress',
                              visible= True,
                              args=[{
                                  'y':[dp['Tracks']],
                                  'x':[dp['Percentage Completion'],100-dp['Percentage Completion']],
                                  'visible': [True,True],
                                  'type': 'bar',
                                  'name':['DONE','PENDING'],
                                  'text': [dp['Percentage Completion'],100-dp['Percentage Completion']],
                                  'textposition': 'auto',
                                  },{'title': 'YOUR COURSE TTRACK','yaxis':{'title': 'TASKS'}, 'xaxis':{'title': 'Percentage Completion'}
                                  }]))
btn.append(dict(method='update',
                              label= 'TARGET DATE',
                              visible= True,
                              args=[{
                                  'y':[df['Tracks']],
                                  'x':[df['Target Date']],
                                  'visible': [True,False],
                                  'type': 'marksers+lines+text',
                                  'text': [dp['Percentage Completion']],
                                  'textposition': 'auto',
                                  },{'title': 'YOUR COURSE TRACK','yaxis':{'title': 'TASKS'}, 'xaxis':{'title': 'Target Date'}
                                  }]))

updatemenus.append(dict())
updatemenus[1]['buttons']=btn
updatemenus[1]['type']='buttons'
updatemenus[1]['direction']='right'
updatemenus[1]['x']=-0.25

updatemenus[1]['y']=1.5

    
fig.layout.update(title='Course Track in Various Fields',title_x=0.5)
fig.update_layout(barmode="relative",updatemenus=updatemenus)

fig.show()
