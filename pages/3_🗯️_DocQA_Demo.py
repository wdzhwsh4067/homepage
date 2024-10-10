import streamlit as st
# import streamlit.components.v1 as components
# components.iframe("https://cherokee.nicedata.eu.org/", height=500)
import streamlit.components.v1 as components
import base64
from faker import Faker
import random
from datetime import datetime
import pandas as pd
import requests

st.set_page_config(layout="wide")

# LOGO_URL_LARGE="./static/lora.png"
st.logo(
    "./static/logo1.png",
    link="https://nicedata.eu.org/"
)




st.title("🔥 DocQA")
st.markdown(
    """
    Currently, enhancing the instructional compliance of Large Language Models (LLMs) largely relies on high-quality instruction-response pairs. However, existing methods for constructing Supervised Fine-Tuning (SFT) data have several shortcomings: 1) reliance on a single sample source, which typically involves unstructured and unsupervised texts, neglecting the more prevalent semi-structured data, leading to excessively high training costs; 2) issues with data quality, such as QA questions lacking focus, short and vague responses, and severe hallucinations in the answers.
    To tackle these challenges, this paper proposes a scalable solution.It involves training LLMs
    To overcome these limitations, we introduce the Doc2QA framework for QA data construction, aimed at efficiently leveraging the diverse and widely available semi-structured data (including Html, Doc, PDFs, etc.) to generate QA pairs. This approach reduces the high preparation costs and inaccuracies caused by data hallucinations, such as short, unfocused, and hallucinatory QA pairs.
    Experiments demonstrate that our method surpasses classical QA construction techniques in multiple test datasets and benchmarks, especially on AlpacaEval, where the Doc2QA model, using only xx\% of the training data, achieved an xx\% performance improvement. Additionally, manual review confirmed the exceptional quality of the generated dataset, significantly enhancing the practical value of SFT data and setting a new benchmark for the precision of LLM's instructional compliance. This represents a significant step towards more efficient and accurate LLM training.
        """
)
st.info("Click on the left sidebar menu to navigate to the different apps.")

# Border Demo
st.markdown('<a name="customizable-border"></a>', unsafe_allow_html=True)
st.header("🔲 Detail", divider="rainbow")
st.markdown("You can now customize `st.container` and `st.form` by adding or removing the border")

# Initialize Faker to generate fake data
fake = Faker()

def random_date(start, end):
    return start + (end - start) * random.random()

def create_sample_data(num_rows=10):
    data = {
        "Customer Name": [fake.name() for _ in range(num_rows)],
        "Product": [random.choice(["Laptop", "Smartphone", "Tablet", "Headphones", "Charger"]) for _ in range(num_rows)],
        "Quantity": [random.randint(1, 5) for _ in range(num_rows)],
        "Order Date": [random_date(datetime(2021, 1, 1), datetime(2023, 1, 1)).strftime("%Y-%m-%d") for _ in range(num_rows)]
    }
    return pd.DataFrame(data)
df = create_sample_data(10)

after, before = st.columns(2)

with after:
    st.subheader("New customizable borders")
    st.info("⬇️ :red[st.container] can now be configured to have a border")
   
    with st.container(border=True):
        # st.info("This text and table are inside a container with a border")
        st.dataframe(data=df, use_container_width=True)

    st.code(
        """
        with st.container(border=True):
            st.dataframe(data=df, use_container_width=True)
        """
    )

    st.info("⬇️ :red[st.form] can now be configured to appear without a border")

    with st.form(key="my_form_2", border=False):
        st.dataframe(data=df, use_container_width=True)
        st.form_submit_button(label="Submit")
    
    st.code(
        """
        with st.form(key="my_form_2", border=False):
            st.dataframe(data=df, use_container_width=True)
            st.form_submit_button(label="Submit")
        """
    )

with before:
    st.subheader("Old non-customizable borders")
    st.info("⬇️ :red[st.container] does not have a border")
    with st.container():
        st.dataframe(data=df, use_container_width=True)
        
    # Instead of st.empty(), use a markdown with empty space
    st.markdown('<div style="height: 31px;"></div>', unsafe_allow_html=True)
    
    st.code(
        """
        with st.container():
            st.dataframe(data=df, use_container_width=True)
        """
    )

    st.info("⬇️ :red[st.form] always has a border")
    with st.form(key="my_form_1"):
        st.dataframe(data=df, use_container_width=True)
        st.form_submit_button(label="Submit")
        
    st.code(
        """
        with st.form(key="my_form"):
            st.info("This text and table are inside a form with a border")
            st.dataframe(data=df, use_container_width=True)
            st.form_submit_button(label="Submit")
        """
    )

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
    
tab1, tab2 = st.tabs(
    [
        "Multi-Dimensional Scatter Analysis",
        "Scatter Basics"
    ]
)

with tab1:
    st.subheader("Dynamic Scatter Chart", anchor=False)
    st.caption("Choose the dimension for the x-axis, y-axis, color, and size to explore average house price, average rent, geographic region, and median income in the United States.")

    st.divider()
    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_data
        def load_data():
            df = pd.read_csv('1.27/pages/data_simplified.csv')
            df['Average House Price'] = df['Average House Price'].str.replace('$', '').str.replace(',', '').astype(int)
            df['Median Income'] = df['Median Income'].str.replace('$', '').str.replace(',', '').astype(int) 
            
            sorted_regions = df.groupby('Region in the US')['Average House Price'].mean().sort_values().index.tolist()
            df['Region in the US'] = pd.Categorical(df['Region in the US'], categories=sorted_regions, ordered=True)
            df = df.sort_values('Region in the US')
        
            # Create income buckets
            income_bins = [0, 50000, 100000, 150000, 200000, float('inf')]
            income_labels = ['<50k', '50k-100k', '100k-150k', '150k-200k', '200k+']
            df['Income Bucket'] = pd.cut(df['Median Income'], bins=income_bins, labels=income_labels, right=False)
        
            df['Income Bucket'] = pd.Categorical(df['Income Bucket'], categories=income_labels, ordered=True)
            df = df.sort_values('Income Bucket')
        
            return df

        df = load_data()

        col1, col2, col3, col4 = st.columns(4)

        x_axis = col1.selectbox('X-axis:', df.columns, index=1, disabled=True)
        y_axis = col2.selectbox('Y-axis:', df.columns, index=0)
        color_dim = col3.selectbox('Color:', df.columns, index=3)
        size_dim = col4.selectbox('Size:', df.columns, index=2)
        
        st.scatter_chart(
            df,
            x=x_axis,
            y=y_axis,
            color=color_dim,
            size=size_dim,
            height=600,
            use_container_width=True
        )
        """
    )

with tab2:
    st.subheader("Simple Scatter Chart", anchor=False)
    st.caption("The chart shows some positive correlation between Average Rent and Average House Price")

    st.divider()
    st.code(
        """
        import streamlit as st
        import pandas as pd

        @st.cache_data
        def load_data():
            df = pd.read_csv('1.27/pages/data_simplified.csv')
            df['Average House Price'] = df['Average House Price'].str.replace('$', '').str.replace(',', '').astype(int)
            df['Median Income'] = df['Median Income'].str.replace('$', '').str.replace(',', '').astype(int) 
            
            sorted_regions = df.groupby('Region in the US')['Average House Price'].mean().sort_values().index.tolist()
            df['Region in the US'] = pd.Categorical(df['Region in the US'], categories=sorted_regions, ordered=True)
            df = df.sort_values('Region in the US')
        
            # Create income buckets
            income_bins = [0, 50000, 100000, 150000, 200000, float('inf')]
            income_labels = ['<50k', '50k-100k', '100k-150k', '150k-200k', '200k+']
            df['Income Bucket'] = pd.cut(df['Median Income'], bins=income_bins, labels=income_labels, right=False)
        
            df['Income Bucket'] = pd.Categorical(df['Income Bucket'], categories=income_labels, ordered=True)
            df = df.sort_values('Income Bucket')
        
            return df

        df = load_data()

        st.scatter_chart(
            df,
            x='Average Rent',
            y='Average House Price',
            height=600,
            use_container_width=True
        )
        """
    )
    
    
# ============================================

# ============================================s