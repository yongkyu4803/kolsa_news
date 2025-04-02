import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # CSV 형식으로 다운로드할 수 있는 링크입니다.
    csv_url = "https://docs.google.com/spreadsheets/d/1e35rPkGkKBklFygjUAZX0Q0-CKca--ADT46gXRGYCUQ/export?format=csv&gid=0"
    data = pd.read_csv(csv_url)
    return data

def main():
    st.title("Kolsa News")
    
    data = load_data()
    
    # 카드 스타일 정의
    st.markdown("""
    <style>
    .card {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .card-title {
        font-size: 24px;  /* 제목 글자 크기 */
        font-weight: bold;
        margin: 0;
    }
    .card-subinfo {
        font-size: 12px;  /* 제목의 50% 정도 */
        color: #555;
        margin: 0;
    }
    .card-content {
        font-size: 16.8px;  /* 제목의 70% (24px * 0.7) */
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # 각 행을 카드 형태로 표시
    for index, row in data.iterrows():
        # 첫 번째 줄: 제목과 링크 (링크 클릭 시 새 창으로 열림)
        title_html = f'<p class="card-title"><a href="{row["link"]}" target="_blank" style="text-decoration: none; color: inherit;">{row["title"]}</a></p>'
        # 두 번째 줄: 키워드, 미디어, pubDate
        subinfo_html = f'<p class="card-subinfo">{row["keyword"]} | {row["media"]} | {row["pubDate"]}</p>'
        # 세번째~다섯번째 줄: 요약내용 (contenet1, contenet2, contenet3)
        content_html = ""
        for col in ["content1", "content2", "content3"]:
            if pd.notna(row[col]) and row[col].strip() != "":
                content_html += f'<p class="card-content">{row[col]}</p>'
        card_html = f'<div class="card">{title_html}{subinfo_html}{content_html}</div>'
        st.markdown(card_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
