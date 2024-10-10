import streamlit as st
import leafmap.foliumap as leafmap
import base64
# from faker import Faker
import random
st.set_page_config(layout="wide")

# LOGO_URL_LARGE="./static/lora.png"
st.logo(
    "./static/logo1.png",
    link="https://nicedata.eu.org/"
)


st.sidebar.title("Contact")
with st.sidebar:
  st.info(
    """
  - Email: [sh.wang4067@gmail.com](mailto:sh.wang4067@gmail.com)
  - Tel: +86 181-1615-2720
  - Homepage: [nicedata.eu.org](https://nicedata.eu.org)
  - Github: [wdzhwsh4076](https://github.com/wdzhwsh4076)
  - Address: Boda Campus, Xinjiang University, Urumqi City, China
    """
)
p1, p2 = st.columns(2)
with p2:
  
  st.subheader("")
  st.image("./static/self.jpeg",width=200)
with p1:
  
  st.title("Shaohuang Wang")

  st.markdown(
      """
I'm Shaohuang Wang, a Computer Science Master's student at Xinjiang University, focusing on Machine Learning and Data Structures. 

My research interests include Large Language Models and Recommender Systems.  I'm also a developer at NLPIR Lab, working on NLP and data processing technologies. 

[Email](mailto:sh.wang4067@gmail.com) / [CV](https://nicedata.eu.org) / [Bio](https://nicedata.eu.org) / [Google Scholar](https://scholar.google.com) / [Twitter](https://twitter.com) / [Github](https://github.com/wdzhwsh4076)

      """
  )

# st.info("Click on the left sidebar menu to navigate to the different apps.")

# =========================================================================
st.markdown('<a name="customizable-border"></a>', unsafe_allow_html=True)
st.header("👨🏻‍🎓 Education", divider="rainbow")
st.markdown("""
### Xinjiang University, China
- **M.Eng. in Computer Science** (2022.09 - Present)
  - GPA: 3.5/4.0
  - Core Course: Machine Learning, Computer Networks, Data Structures
  - Thesis: Research on scientific and technological information recommendation via LLM
  - Research Interest: LLM, RAG, SFT, Fine-tuning, Recommend System

### Shanghai University of Engineering Science, China
- **B.Eng. in Vehicle Engineering** (2016.09 - 2020.06)
  - GPA: 3.1/4.0
  - Awards: National Scholarship (Top 1%), First-Class Scholarship (Top 3%)
      """
    )

# =========================================================================
st.markdown('<a name="customizable-border"></a>', unsafe_allow_html=True)
st.header("🧑🏻‍💻 Publication", divider="rainbow")
def get_file_url(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url
p1, p2 = st.columns(2)
old_skeleton_url = get_file_url("./static/lora.png")
new_skeleton_url = get_file_url("./static/rag.png")
with p1:
    st.subheader("Bypassing LLM Safeguards: The In-Context Tense Attack Approach.")
    st.info("Wang, S et al. International Conference on Computer Engineering and Networks, 2406.12243 (2024). (Accepted)")
    st.markdown("""
    We explore the power of combining tense attacks with in-context examples in manipulating the security of LLMs and propose In-Context Tense Attack (ITA) for jailbreaking purposes.
      """
    )
    f1, f2, f3 = st.columns(3)
    with f1:
      with open("./static/lora.png", "rb") as file1:
        btn1 = st.download_button(
            key='4',
            label="Arxiv",
            data=file1,
            file_name="flower.png",
            mime="image/png",
            type="primary",
                        use_container_width=True,
        )
    with f2:
      with open("./static/lora.png", "rb") as file2:
        btn = st.download_button(
            key='1',
            label="PDF",
            data=file2,
            file_name="flower.png",
            mime="image/png",
          type="secondary",
                      use_container_width=True,
        )
    with f3:
      st.link_button("Cite", "https://streamlit.io/gallery",            use_container_width=True,)

with p2:
  #   st.markdown(
  #       f'<img src="data:image/gif;base64,{new_skeleton_url}" width=450 alt="demo gif">',
  #       unsafe_allow_html=True,
  # )
    st.image("./static/paper1.png",width=450)
    st.caption("""
Tense Attack is a technique targeting Large Language Models (LLMs) that
exploits the models’ potential vulnerability when processing requests phrased in
the past tense,
               """)

st.divider()
p1, p2 = st.columns(2)
old_skeleton_url = get_file_url("./static/lora.png")
new_skeleton_url = get_file_url("./static/rag.png")
with p2:
    st.subheader("CherryRec: Enhancing News Recommendation Quality via LLM driven Framework.")
    st.info("Wang, S et al. CherryRec: Enhancing News Recommendation Quality via LLM driven Framework. ICASSP (2025). (Under Review)")
    st.markdown("""
    Introduced CherryRec, a news recommendation framework using LLMs to filter low-value news and recommend high-quality news by understanding user preferences and integrating multi-dimensional scores.
      """
    )
    f1, f2, f3 = st.columns(3)
    with f1:
      with open("./static/lora.png", "rb") as file1:
        btn = st.download_button(
            key='2',
            label="Arxiv",
            data=file1,
            file_name="flower.png",
            mime="image/png",
            type="primary",
            use_container_width=True,
        )
    with f2:
      with open("./static/lora.png", "rb") as file2:
        btn = st.download_button(
            key='3',
            label="PDF",
            data=file2,
            file_name="flower.png",
            mime="image/png",
            type="secondary",
            use_container_width=True,
        )
    with f3:
      st.link_button("Cite", "https://streamlit.io/gallery",use_container_width=True,)

with p1:
    st.image("./static/paper2-1.png",width=450)
    st.caption("""
Knowledge-aware News Rapid Selector (KnRS) quickly identifies relevant
news candidates by assessing user interaction history and content attributes.
Content-aware News LLM Evaluator (CnLE) refines selections using a fine-tuned
LLM, deeply understanding user preferences to enhance personalized news rec-
ommendations.
               """)
with st.expander("A list of other publications "):
  st.markdown(
    """
1. **Wang, S** et al. "Bypassing LLM Safeguards: The In-Context Tense Attack Approach." International Conference on Computer Engineering and Networks, 2406.12243 (2024). (Accepted)
2. **Wang, S** et al. "CherryRec: Enhancing News Recommendation Quality via LLM driven Framework." ICASSP (2025). (Under Review)
3. Liang, Y & **Wang, S** et al. "LLaMA-MoT: A Cost-Effective Framework for Visual-Linguistic Instruction Tuning Based on Multi-Head Adapters and Chain-of-Thought." ESWA (2024). (Under Review)
4. **Wang, S** et al. "An agile construction method of instruction fine-tuning dataset based on semi-structured data." Patent (2024). (Submitted)
5. **Wang, S** et al. "Finite element analysis of modular automotive body based on Ansys." Guangxi Journal of Light Industry (2020). (Accepted)
6. **Wang, S** et al. "Buffer connecting device for vehicle." Patent (2020). (Accepted)

*Still in possession of 8 patents, along with various other publications.*
"""
)
# =========================================================================

# =========================================================================
st.markdown('<a name="customizable-border"></a>', unsafe_allow_html=True)
st.header("🧑🏻‍🏫 Research Experience", divider="rainbow")
st.markdown("""
### Domain Information Tracking and Processing Project
- **Developer@NLPIR Lab** (2022.09 - Present)
  - Responsible for the development of the algorithm tool layer, including data collection, review and correction, dynamic selection, keyword extraction, and briefing generation algorithms.
  - Utilized Elasticsearch and MySQL databases for data storage and processing, optimizing data query and analysis processes.
  - Achieved rapid system deployment and front-end and back-end separation design through Docker, simplifying operations and maintenance and enhancing system maintainability.
  - **Technology Stack**: Python, Elasticsearch, MySQL, Docker, Vue.JS, FastAPI

### Doc2QA Framework for Large Language Model SFT Datasets
- **Developer@NLPIR Lab** (2023.04 - Present)
  - Designed and released a comprehensive dataset for QA instruction fine-tuning using semi-structured data, providing a valuable resource for future research.
  - Developed a novel framework, "Doc2QA" based on Large Language Models (LLMs) to generate question-answer pairs from semi-structured data such as HTML, DOC, and PDF.
  - **Technology Stack**: Python, Llama-factory, Vllm, FastAPI, Docker, JavaScript
      """
    )
st.markdown('<a name="customizable-border"></a>', unsafe_allow_html=True)
st.header("🚵🏻‍♂️ Skills", divider="rainbow")
st.markdown(
    """
- **Proficient in Coding**: Python, FastAPI, Elasticsearch, Docker, Vue.Js, Nginx
- **Model Training in AI/ML**: PyTorch, TensorFlow, Llama-index, Vllm, Llama-factory
- **Simulation and Design**: AutoCAD, CATIA, SolidWorks, ANSYS, 3DMax, Adobe Photoshop/Illustrator
- **Languages**: Chinese (native), English (IELTS: 6.5, L: 6.5 R: 7.5 W: 6.0 S: 6.0), Japanese (JLPT-N2)    
"""
)
st.image(
    "./static/stack.png",
)
# row1_col1, row1_col2 = st.columns(2)
# with row1_col1:
#     st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
#     st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

# with row1_col2:
#     st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
#     st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
