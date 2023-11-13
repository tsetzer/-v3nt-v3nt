import streamlit as st
import datetime

# st.set_page_config(layout="wide")

# Dictionary to store YouTube links
youtube_links = {
    1: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    2: "https://www.youtube.com/watch?v=l7OEFc8hcvQ",
    3: "https://www.youtube.com/shorts/0Y10H_hkoKI",
    4: "https://youtube.com/shorts/0Y10H_hkoKI",
    5: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    6: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    7: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    8: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    9: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    10: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    11: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    12: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    13: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    14: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    15: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    16: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    17: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    18: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    19: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    20: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    21: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    22: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    23: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    24: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
}

def main():
    st.title("🎄️:heart: Annas Adventskalender :heart: 🌨")
    st.write("\n --- \n\n\n")

    today = datetime.date.today()
    # today = datetime.date(2023,12,12)
    # st.write(today)
    # cols = st.columns(4)  # 4 columns for a grid-like layout

    st.write('''<style>

    [data-testid="cols"] {
        width: calc(33.3333% - 1rem) !important;
        flex: 1 1 calc(33.3333% - 1rem) !important;
        min-width: calc(33% - 1rem) !important;
    }
    </style>''', unsafe_allow_html=True)

    for i in range(1, 25):
    # with cols[(i-1) % 4]:
        if today >= datetime.date(today.year, 12, i):
            # st.write(f"Türchen {i}")
            st.link_button(f"Türchen {i}", youtube_links[i])

        else:
            # st.link_button(f"Türchen {i}: Noch geheim... 🤐🤶", youtube_links[i], disabled=True)
            st.link_button(f"Türchen {i}", youtube_links[i], disabled=True)

if __name__ == "__main__":
    main()
