import streamlit as st
import pandas as pd
import numpy as np


st.title('JCarlo AI :blue[BETA] :snowflake:')


prompt = st.text_input("Prompt you want to search for:")
with st.container():
    st.header('Articles:', divider='blue')
    st.markdown("#### Sample Article 1")
    st.markdown("#### Sample Article 2")
    st.markdown("#### Sample Article 3")
    st.markdown("#### Sample Article 4")
    # Spacing
    st.text("")
    st.text("")
    st.text("")

st.subheader('Prompt Feedback', divider='blue')
prompt_1 = st.checkbox("Prompt 1")
prompt_2 = st.checkbox("Prompt 2")
prompt_3 = st.checkbox("Prompt 3")
is_feedback = st.button(":blue[Give Feedback]")
