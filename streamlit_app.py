import streamlit as st

st.subheader("🎈 Create my app with python, streamlit")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.subheader('Process')
st.text('과정1. 깃허브(github.com) 계정 생성')
st.text('과정2. 스트림릿(steamlit.io) 계정 생성 - 이 때 반드시 깃허브 계정과 연동')
st.text('과정3. 깃허브에서 앱 코드(main.py) 작성')
st.text('과정4. 스트림릿에서 앱 코드 배포')


st.subheader('제곱 계산기')
st.write('숫자를 입력하면 제곱값을 계산해드려요') 
number=st.number_input('숫자를 입력하세요.', min_value=0, value=0) 
squared_number=number**2 
st.write(f'{number]의 제곱은 {squared_number]입니다.')
