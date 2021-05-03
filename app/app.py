import src.utils as my_utils

import streamlit as st

st.title('Hello World!')
st.write('Welcome to my app template')

current_time = my_utils.get_current_time()
datetime_message = "Current date and time: {} UTC".format(current_time)

st.write(datetime_message)
