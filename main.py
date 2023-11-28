import streamlit as st
import datetime

# st.set_page_config(layout="wide")

# Dictionary to store YouTube links
youtube_links = {
    1: "https://youtu.be/uMMscUKV70M",          # Karin
    2: "https://youtu.be/CgcBhleSUNk",          # Malaysia
    3:
    4: "https://youtube.com/shorts/0Y10H_hkoKI",
    5: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    6:
    7: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    8: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    9:
    10: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    11: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    12: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    13: "https://youtube.com/shorts/0Y10H_hkoKI?feature=share",
    14:
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


# "https://youtu.be/uMMscUKV70M",          # Karin
#
# "https://youtu.be/CgcBhleSUNk",          # Malaysia
# "https://youtu.be/m7N-XmOwrmg",          # Java
# "https://youtu.be/wE9YZ4HH_70",          # Lombok
# "https://youtu.be/Fg2jtjZTj70",          # Singapur


def main():

    st.markdown("<h1 style='text-align: center'>🎄️❤️ Annas ❤️🎄</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center'>🌨️❤️ Adventskalender ❤️🌨</h1>", unsafe_allow_html=True)
    st.write("\n --- \n")

    # today = datetime.date.today()
    today = datetime.date(2023,12,15)
    # st.write(today)

    for i in range(1, 25):

        if today >= datetime.date(today.year, 12, i):
            # st.write(f"Türchen {i}")
            st.link_button(f"Türchen {i}", youtube_links[i])

        else:
            # st.link_button(f"Türchen {i}: Noch geheim... 🤐🤶", youtube_links[i], disabled=True)
            st.link_button(f"Türchen {i}", youtube_links[i], disabled=True)


if __name__ == "__main__":
    main()
