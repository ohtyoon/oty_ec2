import streamlit as st

# 페이지 설정
st.set_page_config(page_title="EC2 Deployment Test", layout="centered")

st.write("이 앱은 AWS Learner Lab EC2 인스턴스에서 실행 중입니다.")

user_input = st.text_input("터미널에 출력할 메시지를 입력하세요:", "Hello, EC2!")

if st.button("전송"):
    st.success(f"입력 확인: {user_input}")
    
    print(f"[LOG] 사용자 입력 발생: {user_input}")
