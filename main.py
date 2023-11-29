import streamlit as st
import datetime

# st.set_page_config(layout="wide")

# Dictionary to store YouTube links
youtube_links = {
    1: "https://youtu.be/uMMscUKV70M",           # Karin
    2: "https://youtu.be/PP7fQf0NTfo",           # Kreta
    3: "https://youtu.be/MTwjOV1JrLM",           # Sascha
    4: "https://youtu.be/tyUe_7oQKDE",           # Segeln
    5: "https://youtu.be/q9BMYjceeMQ",           # Setzers
    6: "https://youtube.com/shorts/he1RYZT_m1E?feature=share", # Julia & Lukas
    7: "https://youtu.be/dmrDpjsm67g",           # West Coast
    8: "https://youtu.be/zL_CbIS-i1I",           # Boston
    9: "https://youtube.com/shorts/DoICWB4ZgQU?feature=share", # Regina
    10: "https://youtu.be/tR882g-lCTs",           # Gardasee
    11: "https://youtube.com/shorts/pRSlqy5rqY4?feature=share", # Sven
    12: "https://youtu.be/CgcBhleSUNk",          # Malaysia
    13: "https://youtube.com/shorts/Wdx6iojoOZE?feature=share", # Sonia
    14: "https://youtu.be/m7N-XmOwrmg",          # Java
    15: "https://youtube.com/shorts/nbwpvfsMsAc?feature=share", # Nga & Marchy
    16: "https://youtu.be/wE9YZ4HH_70",          # Lombok
    17: "https://youtu.be/Fg2jtjZTj70",          # Singapur
    18: "",
    19: "",
    20: "",
    21: "",
    22: "",
    23: "",
    24: "",
}

def main():

    st.markdown("<h1 style='text-align: center'>🎄️❤️ Annas ❤️🎄</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center'>🌨️❤️ Adventskalender ❤️🌨</h1>", unsafe_allow_html=True)
    st.write("\n --- \n")

    today = datetime.date.today()
    # today = datetime.date(2023,12,17)

    for i in range(1, 25):

        if today >= datetime.date(today.year, 12, i):
            st.link_button(f"Türchen {i}", youtube_links[i])

        else:
            st.link_button(f" Geheimes Türchen {i}", youtube_links[i], disabled=True)


if __name__ == "__main__":
    main()
