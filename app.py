import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # CSV 형식으로 다운로드할 수 있는 링크입니다.
    csv_url = "https://docs.google.com/spreadsheets/d/1e35rPkGkKBklFygjUAZX0Q0-CKca--ADT46gXRGYCUQ/export?format=csv&gid=0"
    data = pd.read_csv(csv_url)
    return data

def main():
    st.title("📰 Kolsa News")
    
    data = load_data()
    
    # 카드 스타일 및 복사 기능에 필요한 JavaScript 정의
    st.markdown("""
    <style>
    .card {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        background-color: #f9f9f9 !important;
    }
    .card-title {
        font-size: 24px !important;  /* 제목 글자 크기 */
        font-weight: bold;
        margin: 0;
    }
    .card-subinfo {
        font-size: 12px !important;  /* 제목의 50% 정도 */
        color: #555;
        margin: 0;
    }
    .card-content {
        font-size: 16.8px !important;  /* 제목의 70% (24px * 0.7) */
        margin: 5px 0;
    }
    .copy-button {
        margin-top: 10px;
        padding: 5px 10px;
        font-size: 12px;
        cursor: pointer;
    }
    </style>

    <script>
    function copyToClipboard(id) {
        var text = document.getElementById(id).value;
        navigator.clipboard.writeText(text).then(function() {
            alert("Copied to clipboard!");
        }, function(err) {
            alert("Failed to copy text: " + err);
        });
    }
    </script>
    """, unsafe_allow_html=True)
    
    # 각 행을 카드 형태로 표시
    for index, row in data.iterrows():
        # 첫 번째 줄: 제목과 링크 (링크 클릭 시 새 창으로 열림)
        title_html = f'<p class="card-title"><a href="{row["link"]}" target="_blank" style="text-decoration: none; color: inherit;">{row["title"]}</a></p>'
        # 두 번째 줄: 키워드, 미디어, pubDate
        subinfo_html = f'<p class="card-subinfo">{row["keyword"]} | {row["media"]} | {row["pubDate"]}</p>'
        # 세번째~다섯번째 줄: 요약내용(각 앞에 블렛포인트 추가)
        content_html = ""
        # 복사할 텍스트에 넣기 위한 문자열 (각 항목 사이에 줄바꿈 포함)
        card_text = f'{row["title"]}\n{row["keyword"]} | {row["media"]} | {row["pubDate"]}\n'
        for col in ["content1", "content2", "content3"]:
            if pd.notna(row[col]) and row[col].strip() != "":
                content_html += f'<p class="card-content">• {row[col]}</p>'
                card_text += f'• {row[col]}\n'
        # 숨겨진 textarea (카드 내용을 복사하기 위한 대상)
        clipboard_html = f'<textarea id="card_content_{index}" style="display:none;">{card_text}</textarea>'
        # 복사 버튼
        button_html = f'<button class="copy-button" onclick="copyToClipboard(\'card_content_{index}\')">Copy</button>'
        
        card_html = f'<div class="card">{title_html}{subinfo_html}{content_html}{clipboard_html}{button_html}</div>'
        st.markdown(card_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
