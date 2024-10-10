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
    st.title('💬 Cherokee Model')
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

st.title("Cherokee Language Model with RAG")
# st.markdown(
#     """
#     I am excited to present the latest language model, which has been  fine-tuned using the state-of-the-art LoRA (Low-Rank Adaptation) technique on the robust foundation of the LLaMA3-8B model. 
#     This is an open-source project and you are very welcome to contribute your comments, questions, resources, and apps as [issues](https://github.com/giswqs/streamlit-geospatial/issues) or
#     [pull requests](https://github.com/giswqs/streamlit-geospatial/pulls) to the [GitHub repository](https://github.com/giswqs/streamlit-geospatial).

#     """
# )s
st.info("Click on the left sidebar menu to navigate to the different apps.")

components.iframe("https://211.nicedata.eu.org/chatbot/Su0heMXH9oIXOd5C", height=700)



def get_file_url(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url



## -------------------------------------------------------------------- ##

# dataset
st.markdown('<a name="customizable-border"></a>', unsafe_allow_html=True)
st.header("🔲 Datasets", divider="rainbow")
st.markdown("Trained on **two datasets** build by myself to ensure its proficiency in **Cherokee-Englishtranslation**.")

st.markdown("""
#### Cherokee-English Word Dataset (10.2k)

This dataset focuses on vocabulary, ensuring that our model has a comprehensive grasp of Cherokee words and their English counterparts.
""")
text="""
<iframe
  src="https://huggingface.co/datasets/wang4067/cherokee-english-word-10.2k/embed/viewer/default/train"
  frameborder="0"
  width="100%"
  height="560px"
></iframe>
"""
components.html(text,width=700, height=560, scrolling=False)

st.markdown("""
#### Cherokee-English Bible Sentence Dataset (7.96k)

This dataset provides a rich source of bilingual text, enabling our model to understand and reproduce the nuances of the Cherokee language within a religious context.
""")
text="""
<iframe
  src="https://huggingface.co/datasets/wang4067/cherokee-english-bible-7.96k/embed/viewer/default/train"
  frameborder="0"
  width="100%"
  height="560px"
></iframe>
"""
components.html(text,width=700, height=560, scrolling=False)









# App skeleton Demo
st.markdown('<a name="new-app-loading-animation"></a>', unsafe_allow_html=True)
st.header("⏳ Method", divider="rainbow")
st.markdown("""
            
    #### LoRa (Low-Rank Adaptation) 
    
    LoRA reduces the number of trainable parameters by learning pairs of rank-decompostion matrices while freezing the original weights. This vastly reduces the storage requirement for large language models adapted to specific tasks and enables efficient task-switching during deployment all without introducing inference latency. LoRA also outperforms several other adaptation methods including adapter, prefix-tuning, and fine-tuning.
    
  """)

st.markdown("""
    In this paper, adopt a more parameter-efficient approach, where the task-specific parameter increment $\Delta\Phi = \Delta\Phi(\Theta)$ is further encoded by a much smaller-sized set of parameters $\Theta$ with $|\Theta| \ll |\Phi_0|$.
    The task of finding $\Delta\Phi$ thus becomes optimizing over $\Theta$:
""")

st.latex(r'''
    \begin{align}
        \max_{\Theta} \sum_{(x,y)\in Z}  \sum_{t=1}^{|y|}  \log\left({p_{\Phi_0+\Delta\Phi(\Theta)}(y_{t} | x, y_{<t})}\right)
    \end{align}
    ''')

st.markdown("""
    #### RAG (Retrieval-Augmented Generation)
    
    Retrieval-Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response. Large Language Models (LLMs) are trained on vast volumes of data and use billions of parameters to generate original output for tasks like answering questions, translating languages, and completing sentences. RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts.
""")


def get_file_url(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

old_skeleton_url = get_file_url("./static/lora.png")
new_skeleton_url = get_file_url("./static/rag.png")

gif1, gif2 = st.columns(2)
with gif1:
    # st.subheader("detail")

    st.markdown(
        f'<img src="data:image/gif;base64,{old_skeleton_url}" width=450 alt="demo gif">',
        unsafe_allow_html=True,
    )
    st.caption("Fig 3: As illustrated above, the decomposition of ΔW means that we represent the large matrix ΔW with two smaller LoRA matrices, A and B. If A has the same number of rows as ΔW and B has the same number of columns as ΔW, we can write the decomposition as ΔW = AB. (AB is the matrix multiplication result between matrices A and B.) ")

with gif2:
    # st.subheader("detail")

    st.markdown(
        f'<img src="data:image/gif;base64,{new_skeleton_url}" width=450 alt="demo gif">',
        unsafe_allow_html=True,
    )
    st.caption("""
Fig 4: RAG extends the power of LLMs by accessing relevant proprietary data without retraining. When using RAG with Elastic, you benefit from:
Cutting-edge search techniques
Easy model selection and the ability to swap models effortlessly
Secure document and role-based access to ensure your data stays protected
               """)

st.divider()

## -------------------------------------------------------------------- ##

# Border Demo
st.markdown('<a name="customizable-border"></a>', unsafe_allow_html=True)
st.header("🔲 Future Work ", divider="rainbow")
st.markdown("""
### 1. Data Work

**✅ Approach 1:** Inherit training data from the lab or colleagues without verifying the data quality before training.

**✅ Approach 2:** Download open-source data to construct a "system + query + answer" dataset.

**✅ Approach 3:** Utilize GPT-4 to generate data, mastering the prompts that GPT-4 prefers. Recognize the importance of prompt diversity and explore various methods to expand the diversity of tasks and expressions in prompts. Deliberately include noisy prompts to enhance noise resistance. Be meticulous in checking data quality and align annotation standards with colleagues.

**❓ Approach 4:** Drive the data construction process with user interaction logs, collecting real user prompts, and using rules or GPT-4 to analyze user feedback to obtain high-quality answer data.

**❓ Approach 5:** Draw inspiration from concepts like chain-of-thought, retrieval-augmented generation, function call, and agent-based approaches to break down complex tasks at the data level. For example, if the model can't write a long novel, then "the model writes an outline for the novel, and then the model writes the long novel based on the outline."

### 2. Training Work

**✅ Approach 1:** Inherit training code from the lab or colleagues, modify the data path, and run the training script.

**❓ Approach 2:** Inherit or download training code, study every parameter of the launch code, and understand why offloading is enabled, what sequence parallelism means, etc. Then, examine how the dataloader handles data formats and whether the session data loss is calculated only in the last round or in every round. Investigate which special tokens are used in the code.

**❓ Approach 3:** Not only understand each parameter but also form your own insights: Is an epoch of 3 too many? Is 100,000 training data entries appropriate? Are there too many special tokens? Is the learning rate too high for a 7B model, and how many steps should be used for warm-up, or can warm-up be omitted? With these questions in mind, consult with ChatGPT or read articles from experts to gain further insights.
""")


## -------------------------------------------------------------------- ##
with st.expander("Here are some details about this training process."):
    st.markdown(
"""

```shell
bf16: true
cutoff_len: 1024
dataset: dict_word_v4,dict_sentence_v4
dataset_dir: data
ddp_timeout: 180000000
do_train: true
finetuning_type: lora
flash_attn: auto
gradient_accumulation_steps: 8
include_num_input_tokens_seen: true
learning_rate: 0.0001
logging_steps: 5
lora_alpha: 16
lora_dropout: 0.1
lora_rank: 8
lora_target: all
lr_scheduler_type: cosine
max_grad_norm: 1.0
max_samples: 100000
model_name_or_path: /wsh/models/Meta-Llama-3-8B-Instruct
num_train_epochs: 40.0
optim: adamw_torch
output_dir: saves/Custom/lora/train_2024-09-15-17-54-11-v4-learn_rate_0001
packing: false
per_device_train_batch_size: 2
plot_loss: true
preprocessing_num_workers: 16
report_to: none
save_steps: 100
stage: sft
warmup_steps: 0
```
"""
    )
    
    
# ============================================

# ============================================s