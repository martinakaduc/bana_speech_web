import streamlit as st
import numpy as np
from utils import *

if 'search_phase' not in st.session_state:
    st.session_state.search_phase = ""

if __name__ == '__main__':
    st.set_page_config(page_title="Bahnar Speech by Word")
    local_bahnar_df = bahnar_df.copy()

    with st.container():
        # Header section
        st.image('assets/images/BK.png', width=250)
        st.title('Bahnar Speech by Word')
        st.write("This is the data website containining all processed bana speech by word")

    with st.container():

        st.session_state.search_phase = st.text_input("Find the word you want", value=st.session_state.search_phase)
        if st.button("Search") or st.session_state.search_phase != "":
            vietnamese_words = [st.session_state.search_phase in str(x) for x in local_bahnar_df["Vietnamese"]]
            bahnaric_words = [st.session_state.search_phase in str(x) for x in local_bahnar_df["Bahnaric"]]
            joint_words = [x or y for x, y in zip(vietnamese_words, bahnaric_words)]
            local_bahnar_df = local_bahnar_df[joint_words]

        page_numb, page_size = st.columns([9, 3])
        WORD_PER_PAGE = page_size.number_input("Words per page", min_value=10, max_value=100, value=WORD_PER_PAGE)
        MAX_PAGES = math.ceil(local_bahnar_df.shape[0] / WORD_PER_PAGE)
        PAGE_NUMBER = page_numb.number_input("Page number", min_value=1, max_value=MAX_PAGES, value=PAGE_NUMBER)

    table = st.container()
    sound = st.empty()

    with table:
        st.header('Table of data')

        bahnar_df_by_page = paginate_dataframe(local_bahnar_df, WORD_PER_PAGE, PAGE_NUMBER)
        # st.write(bahnar_df_by_page.to_html(index=False, na_rep="", justify="center", show_dimensions=True), unsafe_allow_html=True)
        
        header_cols = st.columns((1, 2, 2, 2, 1, 1, 1))
        for i, col_header in enumerate(bahnar_df_by_page.columns):
            header_cols[i].markdown("**" + col_header + "**")

        for _, row in bahnar_df_by_page.iterrows():
            cols = st.columns((1, 2, 2, 2, 1, 1, 1))
            cols[0].write(row["No."])
            cols[1].write(row["Vietnamese"])
            cols[2].write(row["Bahnaric"])
            if row["PoS"] is np.nan:
                cols[3].write("-")
            else:
                cols[3].write(row["PoS"])

            if row["BinhDinh"] != "-":
                if cols[4].button("Speak", key=str(row["No."])+"_BD"):
                    sound.write("<audio autoplay hidden> \
                                    <source src='%s/BD/%s' type='audio/mpeg'> \
                                 </audio>" % (bana_speech_data_url, row["Bahnaric"]), unsafe_allow_html=True)
            else:
                cols[4].write("-")

            if row["KonTum"] != "-":
                if cols[5].button("Speak", key=str(row["No."])+"_KT"):
                    sound.write("<audio autoplay hidden> \
                                    <source src='%s/KT/%s' type='audio/mpeg'> \
                                 </audio>" % (bana_speech_data_url, row["Bahnaric"]), unsafe_allow_html=True)
            else:
                cols[5].write("-")

            if row["GiaLai"] != "-":
                if cols[6].button("Speak", key=str(row["No."])+"_GL"):
                    sound.write("<audio autoplay hidden> \
                                    <source src='%s/GL/%s' type='audio/mpeg'> \
                                 </audio>" % (bana_speech_data_url, row["Bahnaric"]), unsafe_allow_html=True)
            else:
                cols[6].write("-")