import pandas as pd
import math

BANA_DB = "assets/db/Bahnar_DB.xlsx"

bahnar_df = pd.read_excel(BANA_DB, sheet_name="Sheet 1")

WORD_PER_PAGE = 20
PAGE_NUMBER = 1
MAX_PAGES = math.ceil(bahnar_df.shape[0] / WORD_PER_PAGE)

# bahnar_df_by_page = paginate_dataframe(bahnar_df, WORD_PER_PAGE, PAGE_NUMBER)

bana_bd = "./Bana-BinhDinh/audio_by_word"
bana_kt = "./Bana-KonTum/audio_by_word"
bana_gl = "./Bana-GiaLai/audio_by_word"
bana_speech_data_url = "https://bana-speech-data.herokuapp.com"

def calculate_max_pages():
    global MAX_PAGES
    global WORD_PER_PAGE
    global bahnar_df

    MAX_PAGES = math.ceil(bahnar_df.shape[0] / WORD_PER_PAGE)

def update_df():
    global PAGE_NUMBER
    global WORD_PER_PAGE
    global bahnar_df
    global bahnar_df_by_page

    bahnar_df_by_page = paginate_dataframe(bahnar_df, WORD_PER_PAGE, PAGE_NUMBER)

def paginate_dataframe(dataframe, page_size, page_num):
    page_size = page_size

    if page_size is None:
        return None

    offset = page_size*(page_num-1)
    return dataframe[int(offset):int(offset + page_size)]