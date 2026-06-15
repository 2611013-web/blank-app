import streamlit as st
# 웹 페이지 제목 설정
st.title("🍜 배달 주문 가능 여부 확인기")
st.write("원하는 음식과 가격을 입력하여 주문이 가능한지 확인해보세요.")

st.markdown("---")

# 1. 음식 입력받기 (자주 시키는 메뉴 추천 및 직접 입력 기능)
food = st.selectbox(
    "원하는 음식을 선택하거나 입력하세요:",
    ["짜장면", "짬뽕", "탕수육", "직접 입력"]
)

if food == "직접 입력":
    food = st.text_input("음식 이름을 입력해주세요:", value="볶음밥")

# 2. 주문 금액 입력받기 (기본값 8,000원, 500원 단위로 조절 가능)
price = st.number_input(
    f"{food}의 가격을 입력하세요 (원):", 
    min_value=0, 
    value=8000, 
    step=500
)

# 최소 배달 주문 금액 설정
MIN_ORDER_AMOUNT = 10000

st.markdown("---")

# 3. 주문 확인 버튼 및 조건문 로직 실행
if st.button("주문하기"):
    if price >= MIN_ORDER_AMOUNT:
        # 조건 만족 시 초록색 성공 메시지 출력
        st.success(f"🎉 주문 완료! {food}({price:,}원) 주문이 정상 접수되었습니다.")
    else:
        # 조건 미달 시 빨간색 경고 메시지 출력
        st.error(f"❌ 주문 불가! 최소 배달 주문 금액은 {MIN_ORDER_AMOUNT:,}원입니다. 현재 {MIN_ORDER_AMOUNT - price:,}원이 부족합니다.")