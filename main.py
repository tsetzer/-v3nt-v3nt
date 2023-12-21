import streamlit as st
import datetime
from datetime import datetime, timedelta


# Dictionary to store YouTube links
youtube_links = {
    1: "https://youtu.be/uMMscUKV70M",           # Karin
    2: "https://youtu.be/APLExYnJsNw",           # Guenters
    3: "https://youtu.be/PP7fQf0NTfo",           # Kreta
    4: "https://youtu.be/MTwjOV1JrLM",           # Sascha
    5: "https://youtu.be/G_8m29ZTfYo",           # Eleonora & Jonas
    6: "https://youtu.be/q9BMYjceeMQ",           # Setzers
    7: "https://youtube.com/shorts/he1RYZT_m1E?feature=share",      # Julia & Lukas
    8: "https://youtu.be/DC1w7Rv_lIc",           # Oma Guenter
    9: "https://youtu.be/aBTnvXFkxRY",           # Oma Dell
    10: "https://youtu.be/tyUe_7oQKDE",          # Segeln
    11: "https://youtube.com/shorts/nbwpvfsMsAc?feature=share",     # Nga & Marchy
    12: "https://youtube.com/shorts/DoICWB4ZgQU?feature=share",     # Regina & Sven (s. unten)
    13: "https://youtu.be/dmrDpjsm67g",          # West Coast
    14: "https://youtube.com/shorts/zpJobnbUGqI?feature=share",     # Maxi & Marius
    15: "https://youtu.be/X8QK55z2S8Y",          # Max & Franzi
    16: "https://youtube.com/shorts/Wdx6iojoOZE?feature=share",     # Sonia
    17: "https://youtu.be/zL_CbIS-i1I",          # Boston,
    18: "https://youtu.be/GtKEV6CyPoo",          # Claudia
    19: "https://youtu.be/WlNeWszFnIE",          # Elena Alex
    20: "https://youtu.be/tR882g-lCTs",          # Gardasee
    21: "https://youtube.com/shorts/LE3YHn2Vt48?feature=share",     # Alex und Anna
    22: "https://youtu.be/wZUFZvcbt9M",          # Bella // Kim
    23: "https://youtu.be/CY_c6rUTzPI",          # Marcel & Nadine
    24: "https://youtu.be/CgcBhleSUNk",          # Malaysia"
}

"

def main():

    st.markdown("<h1 style='text-align: center'>🎄️❤️ Annas ❤️🎄</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center'>🌨️❤️ Adventskalender ❤️🌨</h1>", unsafe_allow_html=True)
    st.write("\n --- \n")

    ### DEBUG manual server_time for testing
    server_time = datetime(2023, 12, 28, 23, 55, 59, 342380)
    st.write(server_time)
    ### DEBUG END

    # Get current server time and shift by X hours
    # server_time = datetime.now()
    shifted_time = server_time + timedelta(hours=7)

    # Use only the date part
    today = shifted_time.date()

    for i in range(1, 25):
        if i == 6 and today >= datetime(today.year, 12, i).date():
            st.link_button(f"Türchen {i}a", youtube_links[i])
            st.link_button(f"Türchen {i}b", "https://maps.app.goo.gl/QNHRA1ENLAf2cjNn7")

        elif i == 12 and today >= datetime(today.year, 12, i).date():
            st.link_button(f"Türchen {i}a", youtube_links[i])
            st.link_button(f"Türchen {i}b", "https://youtube.com/shorts/pRSlqy5rqY4?feature=share")      # Sven

        elif i == 23 and today >= datetime(today.year, 12, i).date():
            st.link_button(f"Türchen {i}a", youtube_links[i])
            st.link_button(f"Türchen {i}b", "https://youtube.com/shorts/u6RS_6yiIS0?feature=share")      # Kim

        elif i == 24 and today >= datetime(today.year, 12, i).date():
            st.link_button(f"Türchen {i}a", youtube_links[i])
            st.link_button(f"Türchen {i}b", "https://youtu.be/m7N-XmOwrmg")         # Java
            st.link_button(f"Türchen {i}c", "https://youtu.be/wE9YZ4HH_70")         # Lombok
            st.link_button(f"Türchen {i}d", "https://youtu.be/Fg2jtjZTj70")         # Singapur

        elif today >= datetime(today.year, 12, i).date():
            st.link_button(f"Türchen {i}", youtube_links[i])

        else:
            st.link_button(f" Geheimes Türchen {i}", youtube_links[i], disabled=True)


if __name__ == "__main__":
    main()