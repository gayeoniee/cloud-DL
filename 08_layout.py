import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

# layout 요소
# columns는 요소를 왼쪽에서 오른쪽으로 배치
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        '오늘의 날씨',
        value='35도',
        delta='+3'
    )

with col2:
    st.metric(
        '오늘의 미세먼지',
        value='보통',
    )
    
with col3:
    st.metric(
        '오늘의 습도',
        value='65%'
    )
    
##
st.markdown('---')

data = {
    '이름': ['홍길동', '김길동', '박길동'],
    '나이': [10, 20, 30]
}
df = pd.DataFrame(data)
st.dataframe(df)
st.divider()

st.table(df)
st.divider()

st.json(data)
st.divider()

# datafile.csv -> load -> table 출력 -> px.box() -> st.plotly_chart()
file = st.file_uploader('파일 업로드', type='csv')
if file is not None:
    df_file = pd.read_csv(file)
    st.table(df_file.head(10))
    
    col4, col5, col6 = st.columns(3)
    numeric_cols = df_file.select_dtypes(include=['number']).columns
    with col4:
        column = st.selectbox("y축 컬럼 선택", numeric_cols)
    
    category_cols = df_file.select_dtypes(exclude=['number']).columns
    with col5:
        category = st.selectbox("x축 컬럼 선택", [None] + list(category_cols))
    
    with col6:  
        color_col = st.selectbox("color", [None] + list(category_cols))
    
    if category:
        df_boxplot = px.box(data_frame=df_file, x=category, y=column, color=color_col)
    else:
        df_boxplot = px.box(data_frame=df_file, y=column)

    st.plotly_chart(df_boxplot)

st.divider()

df_tips = sns.load_dataset('tips')
x_options = ['day','size']
y_options = ['total_bill','tip']
hue_options = ['smoker','sex']

x_option = st.selectbox(
    'Select X-axis',
    index=None,
    options=x_options
)

y_option = st.selectbox(
    'Select Y-axis',
    index=None,
    options=y_options
)

hue_option = st.selectbox(
    'Select Hue',
    index=None,
    options=hue_options
)

chart_type = st.selectbox(
    'Select Chart Type',
    options=['box', 'violin', 'bar']
)

if (x_option != None) & (y_option != None):
    kwargs = dict(data_frame=df_tips, x=x_option, y=y_option)
    if hue_option != None:
        kwargs['color'] = hue_option
        
    if chart_type == 'box':
        fig = px.box(**kwargs)
    elif chart_type == 'violin':
        fig = px.violin(**kwargs, box=True, points='all')
    elif chart_type == 'bar':
        fig = px.bar(**kwargs)
        fig.update_layout(barmode='group')

    st.plotly_chart(fig)
    
    
st.divider()

