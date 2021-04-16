import streamlit as st
import pandas as pd
import plotly.express as px

st.beta_set_page_config(layout="wide")


@st.cache
def loaddata():
    df = pd.read_csv("data\salaries-by-region.csv")

    df['Starting Median Salary'] = df['Starting Median Salary'].apply(lambda x: x.replace('$','')).apply(lambda x: x.replace(',','')).astype(float)
    df['Mid-Career 75th Percentile Salary'] = df['Mid-Career 75th Percentile Salary'].apply(lambda x: x.replace('$','')).apply(lambda x: x.replace(',','')).astype(float)
    return df[['Region','School Name','Starting Median Salary', 'Mid-Career 75th Percentile Salary']]

df = loaddata()

st.header("College Salary Exploration")
#schoolname = st.sidebar.text_input("Enter partial school name to see highlight", "")
schools = st.sidebar.multiselect('Highlight', df['School Name'].values.tolist(),
default=['Yale University','Cornell University','New York University (NYU)'])

df2 = pd.DataFrame(index=df.index)
df2['Region'] = df['Region']
df2['Size'] = 2
if schools:
    df2[df['School Name'].isin(schools)] =  ['Highlight',6]
outdf = pd.concat([df[['School Name','Starting Median Salary', 'Mid-Career 75th Percentile Salary']],df2], axis=1)

fig = px.scatter(outdf, x="Starting Median Salary", y="Mid-Career 75th Percentile Salary", 
    size='Size',color='Region', text="School Name",height=800,
    color_discrete_map={"Highlight": "yellow"})
fig.update_traces(textposition='top center')
fig.update_layout(title_text='School Salary', title_x=0.5)

st.plotly_chart(fig, use_container_width=True)