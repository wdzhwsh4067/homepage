import streamlit as st
# import streamlit.components.v1 as components
# components.iframe("https://cherokee.nicedata.eu.org/", height=500)
import streamlit.components.v1 as components
import base64
# from faker import Faker
import random
from datetime import datetime
import pandas as pd
import requests
import time
st.set_page_config(layout="wide")

# LOGO_URL_LARGE="./static/lora.png"
st.logo(
    "./static/logo1.png",
    link="https://nicedata.eu.org/"
)

with st.sidebar:
    st.title('🌵 Cherokee Syllabary and Phonetic Converter')
    st.write('This chatbot is created using the open-source Llama 3 LLM model from Meta.')

    st.markdown('📖 Learn how to build this app in this [blog](https://nicedata.eu.org/Cherokee)!')

    st.info(
        """
    - Email: [sh.wang4067@gmail.com](mailto:sh.wang4067@gmail.com)
    - Tel: +86 181-1615-2720
    - Homepage: [nicedata.eu.org](https://nicedata.eu.org)
    - Github: [wdzhwsh4076](https://github.com/wdzhwsh4076)
    - Address: Boda Campus, Xinjiang University, Urumqi City, China
        """
    )
    st.markdown(
        """
    ### Link

    [1. cherokee dictionary](https://www.cherokeedictionary.net/)

    [2. cherokee 500 word](https://www.cherokeedictionary.net/first500)
            """
    )

st.title("🌵 Cherokee Converter")
# st.markdown(
#     """
#     I am excited to present the latest language model, which has been  fine-tuned using the state-of-the-art LoRA (Low-Rank Adaptation) technique on the robust foundation of the LLaMA3-8B model. 
#     This is an open-source project and you are very welcome to contribute your comments, questions, resources, and apps as [issues](https://github.com/giswqs/streamlit-geospatial/issues) or
#     [pull requests](https://github.com/giswqs/streamlit-geospatial/pulls) to the [GitHub repository](https://github.com/giswqs/streamlit-geospatial).

#     """
# )s
st.info("Click on the left sidebar menu to navigate to the different apps.")



def get_file_url(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url



## -------------------------------------------------------------------- ##
def syllabary_to_phonetic(syllabary_sentence: str) -> str:
    syllabary_to_phonetic_map = {
        'Ꭰ': 'a', 'Ꭱ': 'e', 'Ꭲ': 'i', 'Ꭳ': 'o', 'Ꭴ': 'u', 'Ꭵ': 'v',
        'Ꭶ': 'ga', 'Ꭷ': 'ka', 'Ꭸ': 'ge', 'Ꭹ': 'gi', 'Ꭺ': 'go', 'Ꭻ': 'gu', 'Ꭼ': 'gv',
        'Ꭽ': 'ha', 'Ꭾ': 'he', 'Ꭿ': 'hi', 'Ꮀ': 'ho', 'Ꮁ': 'hu', 'Ꮂ': 'hv',
        'Ꮃ': 'la', 'Ꮄ': 'le', 'Ꮅ': 'li', 'Ꮆ': 'lo', 'Ꮇ': 'lu', 'Ꮈ': 'lv',
        'Ꮉ': 'ma', 'Ꮊ': 'me', 'Ꮋ': 'mi', 'Ꮌ': 'mo', 'Ꮍ': 'mu', 'Ᏽ': 'mv',
        'Ꮎ': 'na', 'Ꮏ': 'hna', 'Ꮐ': 'nah', 'Ꮑ': 'ne', 'Ꮒ': 'ni', 'Ꮓ': 'no', 'Ꮔ': 'nu', 'Ꮕ': 'nv',
        'Ꮖ': 'qua', 'Ꮗ': 'que', 'Ꮘ': 'qui', 'Ꮙ': 'quo', 'Ꮚ': 'quu', 'Ꮛ': 'quv',
        'Ꮝ': 's', 'Ꮜ': 'sa', 'Ꮞ': 'se', 'Ꮟ': 'si', 'Ꮠ': 'so', 'Ꮡ': 'su', 'Ꮢ': 'sv',
        'Ꮣ': 'da', 'Ꮤ': 'ta', 'Ꮥ': 'de', 'Ꮦ': 'te', 'Ꮧ': 'di', 'Ꮨ': 'ti', 'Ꮩ': 'do', 'Ꮪ': 'du', 'Ꮫ': 'dv',
        'Ꮬ': 'dla', 'Ꮭ': 'tla', 'Ꮮ': 'tle', 'Ꮯ': 'tli', 'Ꮰ': 'tlo', 'Ꮱ': 'tlu', 'Ꮲ': 'tlv',
        'Ꮳ': 'tsa', 'Ꮴ': 'tse', 'Ꮵ': 'tsi', 'Ꮶ': 'tso', 'Ꮷ': 'tsu', 'Ꮸ': 'tsv',
        'Ꮹ': 'wa', 'Ꮺ': 'we', 'Ꮻ': 'wi', 'Ꮼ': 'wo', 'Ꮽ': 'wu', 'Ꮾ': 'wv',
        'Ꮿ': 'ya', 'Ᏸ': 'ye', 'Ᏹ': 'yi', 'Ᏺ': 'yo', 'Ᏻ': 'yu', 'Ᏼ': 'yv',
    }
    
    phonetic_sentence = ''
    for char in syllabary_sentence:
        if char in syllabary_to_phonetic_map:
            phonetic_sentence += syllabary_to_phonetic_map[char]
        else:
            phonetic_sentence += char
    
    return phonetic_sentence

def phonetic_to_syllabary(phonetic_sentence: str) -> str:
    phonetic_to_syllabary_map = {
        'a': 'Ꭰ', 'e': 'Ꭱ', 'i': 'Ꭲ', 'o': 'Ꭳ', 'u': 'Ꭴ', 'v': 'Ꭵ',
        'ga': 'Ꭶ', 'ka': 'Ꭷ', 'ge': 'Ꭸ', 'gi': 'Ꭹ', 'go': 'Ꭺ', 'gu': 'Ꭻ', 'gv': 'Ꭼ',
        'ha': 'Ꭽ', 'he': 'Ꭾ', 'hi': 'Ꭿ', 'ho': 'Ꮀ', 'hu': 'Ꮁ', 'hv': 'Ꮂ',
        'la': 'Ꮃ', 'le': 'Ꮄ', 'li': 'Ꮅ', 'lo': 'Ꮆ', 'lu': 'Ꮇ', 'lv': 'Ꮈ',
        'ma': 'Ꮉ', 'me': 'Ꮊ', 'mi': 'Ꮋ', 'mo': 'Ꮌ', 'mu': 'Ꮍ', 'mv': 'Ᏽ',
        'na': 'Ꮎ', 'hna': 'Ꮏ', 'nah': 'Ꮐ', 'ne': 'Ꮑ', 'ni': 'Ꮒ', 'no': 'Ꮓ', 'nu': 'Ꮔ', 'nv': 'Ꮕ',
        'qua': 'Ꮖ', 'que': 'Ꮗ', 'qui': 'Ꮘ', 'quo': 'Ꮙ', 'quu': 'Ꮚ', 'quv': 'Ꮛ',
        's': 'Ꮝ', 'sa': 'Ꮜ', 'se': 'Ꮞ', 'si': 'Ꮟ', 'so': 'Ꮠ', 'su': 'Ꮡ', 'sv': 'Ꮢ',
        'da': 'Ꮣ', 'ta': 'Ꮤ', 'de': 'Ꮥ', 'te': 'Ꮦ', 'di': 'Ꮧ', 'ti': 'Ꮨ', 'do': 'Ꮩ', 'du': 'Ꮪ', 'dv': 'Ꮫ',
        'dla': 'Ꮬ', 'tla': 'Ꮭ', 'tle': 'Ꮮ', 'tli': 'Ꮯ', 'tlo': 'Ꮰ', 'tlu': 'Ꮱ', 'tlv': 'Ꮲ',
        'tsa': 'Ꮳ', 'tse': 'Ꮴ', 'tsi': 'Ꮵ', 'tso': 'Ꮶ', 'tsu': 'Ꮷ', 'tsv': 'Ꮸ',
        'wa': 'Ꮹ', 'we': 'Ꮺ', 'wi': 'Ꮻ', 'wo': 'Ꮼ', 'wu': 'Ꮽ', 'wv': 'Ꮾ',
        'ya': 'Ꮿ', 'ye': 'Ᏸ', 'yi': 'Ᏹ', 'yo': 'Ᏺ', 'yu': 'Ᏻ', 'yv': 'Ᏼ',
    }
    
    syllabary_sentence = ''
    i = 0
    while i < len(phonetic_sentence):
        if i + 2 <= len(phonetic_sentence) and phonetic_sentence[i:i+2] in phonetic_to_syllabary_map:
            syllabary_sentence += phonetic_to_syllabary_map[phonetic_sentence[i:i+2]]
            i += 2
        elif i + 3 <= len(phonetic_sentence) and phonetic_sentence[i:i+3] in phonetic_to_syllabary_map:
            syllabary_sentence += phonetic_to_syllabary_map[phonetic_sentence[i:i+3]]
            i += 3
        elif phonetic_sentence[i] in phonetic_to_syllabary_map:
            syllabary_sentence += phonetic_to_syllabary_map[phonetic_sentence[i]]
            i += 1
        else:
            syllabary_sentence += phonetic_sentence[i]
            i += 1
    
    return syllabary_sentence

# Example usage
syllabary_sentence = "ᎨᏍᏗ ᏯᏍᎦᎢᎮ ᏥᏄᏍᏕ ᎠᎬᏱ ᏣᎴᏂᏍᎨ ᎠᏂᎩᏍᎬ, ᎾᎥᏂ ᏭᎷᏤᎢ, ᏏᏲ, ᎤᏍᏗ ᎠᏣᏗ ᎬᏉᏎᎰ ᏃᎴ ᎨᏍᏗ ᎯᎸᎯᏳ ᏥᎪᎥ ᏂᎯ ᎢᏳᏍᏗ ᎠᏣᏗ."
phonetic_sentence = syllabary_to_phonetic(syllabary_sentence)
print("Phonetic:", phonetic_sentence)

reconstructed_syllabary = phonetic_to_syllabary(phonetic_sentence)
print("Reconstructed Syllabary:", reconstructed_syllabary)
print("Original and reconstructed match:", syllabary_sentence == reconstructed_syllabary)

# dataset
st.markdown('<a name="customizable-border"></a>', unsafe_allow_html=True)
st.header("🔲 Demo", divider="rainbow")
# st.markdown("Enter Cherokee Syllabary Text:")

# st.markdown("""
# #### Cherokee-English Word Dataset (10.2k)

# This dataset focuses on vocabulary, ensuring that our model has a comprehensive grasp of Cherokee words and their English counterparts.
# """)
# Input text area for syllabary
    # Create two columns
# First row: syllabary to phonetic
st.subheader("Syllabary to Phonetic")
col1, col2 = st.columns(2)

with col1:
    syllabary_input = st.text_area("Enter Cherokee Syllabary Text:", 
                                    "ᎨᏍᏗ ᏯᏍᎦᎢᎮ ᏥᏄᏍᏕ ᎠᎬᏱ ᏣᎴᏂᏍᎨ ᎠᏂᎩᏍᎬ",
                                    height=100, key="syllabary_input")
    
    if st.button("Convert to Phonetic"):
        phonetic_output = syllabary_to_phonetic(syllabary_input)
        st.session_state.phonetic_output = phonetic_output

with col2:
    st.text_area("Phonetic Output:", 
                    value=st.session_state.get('phonetic_output', ''),
                    height=100, key="phonetic_output")

# Second row: phonetic to syllabary
st.subheader("Phonetic to Syllabary")
col3, col4 = st.columns(2)

with col3:
    phonetic_input = st.text_area("Enter Phonetic Text:", 
                                    "gesdi yasgaihe jinusde agvyi jalenisge anigigv",
                                    height=100, key="phonetic_input")
    
    if st.button("Convert to Syllabary"):
        syllabary_output = phonetic_to_syllabary(phonetic_input)
        st.session_state.syllabary_output = syllabary_output

with col4:
    st.text_area("Syllabary Output:", 
                    value=st.session_state.get('syllabary_output', ''),
                    height=100, key="syllabary_output")


# App skeleton Demo
st.markdown('<a name="new-app-loading-animation"></a>', unsafe_allow_html=True)
st.header("⏳ Method", divider="rainbow")
st.markdown("""
    #### Cherokee syllabary
    
    The Cherokee syllabary is a syllabary invented by Sequoyah in the late 1810s and early 1820s to write the Cherokee language. His creation of the syllabary is particularly noteworthy as he was illiterate until its creation.[3] He first experimented with logograms, but his system later developed into the syllabary. In his system, each symbol represents a syllable rather than a single phoneme; the 85 (originally 86)[1] characters provide a suitable method for writing Cherokee. The letters resemble characters from other scripts, such as Latin, Greek, Cyrillic, and Glagolitic, however, these are not used to represent the same sounds.
""")


def get_file_url(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

old_skeleton_url = get_file_url("./static/cherokee_tag.png")
new_skeleton_url = get_file_url("./static/cherokee_source.png")

gif1, gif2 = st.columns(2)
with gif1:
    # st.subheader("detail")

    st.markdown(
        f'<img src="data:image/gif;base64,{old_skeleton_url}" width=450 alt="demo gif">',
        unsafe_allow_html=True,
    )
    st.caption("Fig: https://en.wikipedia.org/wiki/Cherokee_syllabary ")

with gif2:
    # st.subheader("detail")

    st.markdown(    
        f'<img src="data:image/gif;base64,{new_skeleton_url}" width=450 alt="demo gif">',
        unsafe_allow_html=True,
    )
    st.caption("""Fig: https://en.wikipedia.org/wiki/Cherokee_syllabary """)

st.divider()

## -------------------------------------------------------------------- ##
