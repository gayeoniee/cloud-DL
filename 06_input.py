import streamlit as st

st.title('Title')
st.header('header')
st.subheader('subheader')

st.divider()

st.write('write 문장')  # 다양한 요소 포함 가능 p태그
st.text('text 문장')    # 텍스트만
st.markdown(
    '''
    여기는 메인 텍스트. \n
    :red[Red], :blue[Blue], :green[Green]
    **굵게**, *이탤릭체 도 가능
    '''
)
st.code(
    '''
    df_covid = pd.read_csv('data/Covid19-India.csv')
    df_covid.info()
    ''',
    language='python'
)

st.divider()

st.button('Hello', icon='🎲')  # secondary type : 기본
st.button('Hello', type='primary')
st.button('Hello', type='primary', disabled=True, key=10)  # type까지 똑같으면 Duplicate에러

st.divider()

################################# button click

def button_write():
    st.write('버튼 클릭!')
    
st.button('reset', type='primary')  # 페이지 갱신
st.button('activate', on_click=button_write)

clicked = st.button('activate2', type='primary')
if clicked:
    st.write('버튼2 클릭!')
    
#################################

st.header('같은 버튼 여러개 만들기')
# key=
# activate button 5개 primary
for i in range(5):
    st.button('activate', type='primary', key=f'act_btn_{i+1}')

#################################

st.divider()

