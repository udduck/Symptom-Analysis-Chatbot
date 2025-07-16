import streamlit as st

st.title("🩺 증상 분석 챗봇")  # 웹페이지의 제목 설정
st.warning("⚠ 이 챗봇은 참고용일 뿐이며, 실제 증상이 있을 경우에 반드시 병원에 방문하세요.")
st.write("어디가 아프신가요? 증상을 입력해 주세요!") # 간단한 안내 문구 출력

symptom = st.text_input("증상 입력")    # 증상 입력


# 증상 키워드에 따라 결과를 판단해주는 함수 정의
def analyze(symptom):
    if "머리" in symptom or "두통" in symptom:
        return "💡 두통이 있으시군요. 수분 섭취하고 휴식을 취해보세요."
    elif "속" in symptom or "토할 것" in symptom or "메스껍" in symptom:
        return "💡 속이 안 좋으신가요? 가볍게 미음이나 죽을 드시고, 충분한 수분 섭취를 해주세요."
    elif "열" in symptom or "발열" in symptom:
        return "💡 열이 난다면 해열제를 복용하거나 찬 수건으로 열을 식히세요. 고열이 지속된다면 병원에 방문하세요."
    elif "기침" in symptom or "목" in symptom:
        return "💡 감기 증상이 의심됩니다. 따뜻한 물을 마시고 휴식을 취하세요."
    elif "배" in symptom or "복통" in symptom:
        return "💡 복통이 있으시면 기름지거나 자극적인 음식은 피하세요. 증상이 지속된다면 병원 방문을 추천드립니다."
    elif "생리통" in symptom or ("배" in symptom and "생리" in symptom):
        return "💡 생리통에는 따뜻한 온열팩을 배에 대거나 진통제를 복용하는 것이 도움이 됩니다."
    else:
        return "⚠ 정확한 증상 분석이 어렵습니다. 정확한 증상을 입력하거나 병원 방문을 권장합니다."

# 증상을 입력하면 결과 출력
if symptom:
    result = analyze(symptom)     # 증상 분석 결과 받기
    st.write(analyze(symptom))  # 웹화면에 출력

st.markdown("---")
st.markdown("🛑 **주의**: 이 챗봇은 간단한 조언만 제공하며, 전문적인 의학적 판단을 대신할 수 없습니다.")
st.markdown("🚑 **심각한 증상이 있다면 즉시 병원을 방문하세요!**")
