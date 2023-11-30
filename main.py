import streamlit as st
import datetime

# st.set_page_config(layout="wide")

# Dictionary to store YouTube links
youtube_links = {
    1: "https://youtu.be/uMMscUKV70M",           # Karin
    2: "https://youtu.be/VAMRi9_qbCc",           # Guenters
    3: "https://youtu.be/PP7fQf0NTfo",           # Kreta
    4: "https://youtu.be/MTwjOV1JrLM",           # Sascha
    5: "https://youtu.be/tyUe_7oQKDE",           # Segeln
    6: "https://youtu.be/q9BMYjceeMQ",           # Setzers
    7: "https://youtube.com/shorts/he1RYZT_m1E?feature=share", # Julia & Lukas
    8: "https://youtu.be/DC1w7Rv_lIc",           # Oma Guenter
    9: "https://youtu.be/aBTnvXFkxRY",           # Oma Mama
    10: "https://youtu.be/dmrDpjsm67g",           # West Coast
    11: "https://youtu.be/zL_CbIS-i1I",           # Boston
    12: "https://youtube.com/shorts/DoICWB4ZgQU?feature=share", # Regina
    13: "https://youtu.be/tR882g-lCTs",           # Gardasee
    14: "https://youtube.com/shorts/pRSlqy5rqY4?feature=share", # Sven
    15: "https://youtu.be/CgcBhleSUNk",          # Malaysia
    16: "https://youtube.com/shorts/Wdx6iojoOZE?feature=share", # Sonia
    17: "https://youtu.be/m7N-XmOwrmg",          # Java
    18: "https://youtube.com/shorts/nbwpvfsMsAc?feature=share", # Nga & Marchy
    19: "https://youtu.be/WlNeWszFnIE",          # Elena Alex
    20: "https://youtu.be/wE9YZ4HH_70",          # Lombok
    21: "https://youtube.com/shorts/LE3YHn2Vt48?feature=share", # Alex und Anna
    22: "https://youtu.be/Fg2jtjZTj70",          # Singapur
    23: "",
    24: "",
}



def main():

    st.markdown("<h1 style='text-align: center'>🎄️❤️ Annas ❤️🎄</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center'>🌨️❤️ Adventskalender ❤️🌨</h1>", unsafe_allow_html=True)
    st.write("\n --- \n")

    # today = datetime.date.today()
    today = datetime.date(2023,12,21)

    for i in range(1, 25):

        if today >= datetime.date(today.year, 12, i):
            st.link_button(f"Türchen {i}", youtube_links[i])

        else:
            st.link_button(f" Geheimes Türchen {i}", youtube_links[i], disabled=True)


if __name__ == "__main__":
    main()
