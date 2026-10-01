import streamlit as st

st.title("🧮 간단한 웹 계산기")
st.write("두 개의 정수와 연산자를 선택하여 계산 결과를 확인해보세요!")

# 1. 입력 필드 (정수 입력 및 연산자 선택)
num1 = st.number_input("첫 번째 정수 입력", value=0, step=1, format="%d")
operator = st.selectbox("연산자 선택", ["+", "-", "*", "/"])
num2 = st.number_input("두 번째 정수 입력", value=0, step=1, format="%d")


# 2. 계산 버튼 및 로직
if st.button("계산하기"):
    # 정수형으로 변환하여 계산
    n1, n2 = int(num1), int(num2)

    if operator == "+":
        result = n1 + n2
        st.success(f"결과: {n1} + {n2} = {result}")
    elif operator == "-":
        result = n1 - n2
        st.success(f"결과: {n1} - {n2} = {result}")
    elif operator == "*":
        result = n1 * n2
        st.success(f"결과: {n1} * {n2} = {result}")
    elif operator == "/":
        if n2 == 0:
            st.error("오류: 0으로 나눌 수 없습니다!")
        else:
            result = n1 / n2
            st.success(f"결과: {n1} / {n2} = {result}")
