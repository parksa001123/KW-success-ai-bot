from openai import OpenAI
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="KW 학생성공 AI 챗봇",
    page_icon="🎓",
    layout="wide"
)

# 제목
st.title("🎓 KW 학생성공 AI 챗봇")
st.caption("비교과 추천 · 대학생활 상담 · 진로 및 학습 지원")

# API KEY 입력
api_key = st.text_input(
    "OpenAI API Key 입력",
    type="password"
)

# API 없을 때
if not api_key:
    st.info("🔑 OpenAI API Key를 입력해주세요.")
    st.stop()

# OpenAI 연결
client = OpenAI(api_key=api_key)

# 세션 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
prompt = st.chat_input("무엇이든 질문하세요!")

if prompt:

    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 응답
    with st.chat_message("assistant"):

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
                    당신은 경운대학교 학생성공 AI 챗봇입니다.

                    역할:
                    - 비교과 프로그램 추천
                    - 진로 및 취업 상담
                    - 학습지원
                    - 대학생활 상담
                    - 심리·정서 지원 안내
                    - 학생 맞춤 성장 추천

                    항상 친절하고 한국어로 답변하세요.
                    """
                },
                *st.session_state.messages
            ]
        )

        answer = response.choices[0].message.content

        st.markdown(answer)

    # 저장
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

           
