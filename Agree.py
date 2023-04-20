import streamlit as st
import pandas as pd
from PIL import Image
from random import randint, sample
from time import sleep

favicon = Image.open("uwindsor_favicon.ico")
facialimage = Image.open("image4.jpg")
participant_data = {}
question_dict = {}

st.set_page_config(page_title="SYMPA Lab",
                       page_icon=favicon,
                       layout="wide",
                       initial_sidebar_state="collapsed",
                       menu_items=None)

if 'page' not in st.session_state:
    st.session_state['page'] = 0

if 'df' not in st.session_state:
    st.session_state.df = []

def nextpage():
    st.session_state.page += 1

def update_dataframe(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    question_dict = {}
    for i in range(1, 11):
        key = 'pQ{}'.format(i)
        val = eval('q{}'.format(i))
        question_dict[key] = val

    if not st.session_state.df:
        st.session_state.df.append(question_dict)

def master():
    update_dataframe(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    nextpage()

with st.empty():
    if st.session_state.page == 0:
        with st.container():
            st.title("Interpersonal Perception Task")
            st.subheader("Overview")

            st.write("Researchers have long tried to identify the predictors of success. Especially in a highly diverse society such as Canada, interpersonal skills are critical. Perceiving others accurately is important. We have found that people whose perceptions are accurate regardless of another’s race, ethnicity, or gender, are particularly likely to succeed.")
            st.write("Based on foundational research conducted at the University of Windsor, our research group has developed a measure of interpersonal perception, which allows us to predict career success. Research shows that some people are surprisingly good at reading personality information from a person’s face. Moreover, our research shows that people who are good at interpersonal perception succeed regardless of their academic success. That is, regardless of the degrees they hold, people who are good at perceiving others tend to live longer, have higher incomes, have more rewarding relationships, and report higher life satisfaction.")
            st.write("We are now at the end of a process in which we develop a shorter version of our test of interpersonal perception. In our short test, we want you to look at just 6 faces and make predictions about them. We believe that our test of only 6 faces will perform about as good as our other much longer test battery.")
            st.write("At the end of the study, you will receive your accuracy based on the match between your answer and answers we collected from a panel of personality experts who have conducted extensive personality assessments on these individuals, as well as your performance relative to other participants who have previously completed the study.")

            st.subheader("Value Prediction Task")
            st.write("People’s values are an important aspect of their personality, and personality is reflected in the way they look.")
            st.write("In the next screen, a series of 3 facial photos will be presented. A panel of personality experts has provided validated ratings based on assessments of personality and values for each individual presented in the image.")
            st.write("For each photo, please guess to what extent personality psychologists may have or may not have endorsed each value statement for the individual depicted in the photo. The personality psychologists used the same scale as you with 1 = *Not at all important to me*, to 10 = *Very important to me*. Please guess how personality psychologists rated the values of the individual in the picture.")
            
            buff1, col1, buff2 = st.columns([0.5,1,0.5])

            col1.image(facialimage, width = 250)

            q1 = col1.radio("Control over others",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)

            q2 = col1.radio("Achieving goals",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)

            q3 = col1.radio("Gratification of desires",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)

            q4 = col1.radio("Seeking adventure and risk",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)

            q5 = col1.radio("Interested in everything, exploring",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)

            q6 = col1.radio("Preserving nature",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)

            q7 = col1.radio("Working for the welfare of others",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)

            q8 = col1.radio("Submitting to life's circumstances",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)

            q9 = col1.radio("Dutiful, meeting obligations",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)

            q10 = col1.radio("Neat, tidy",
                              ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], 0, horizontal=True)
            
            st.subheader("This message will be shown on the next page")
            st.write("Now, you will be shown the other participant you met with at the beginning of the study’s responses (participant 2) on the same task. You can view their responses and then you will be given the opportunity to change your answers, if you wish to do so.")

            if st.button("Continue", on_click=master, disabled=(st.session_state.page > 3)):
                pass

    if st.session_state.page == 1:
        with st.empty():
            with st.spinner(text="Gathering responses from participant 2..."):
                sleep(4)
                nextpage()

    if st.session_state.page == 2:
        confederate_values = []
        participant_df = pd.DataFrame(st.session_state.df, index=[0])
        confederate_df = participant_df.copy()  # initialize to be the same
        to_change = sample(range(0, 10), k=3)
        for idx in to_change:
            new_val = confederate_df.iloc[0, idx]
            while new_val == confederate_df.iloc[0, idx]:
                new_val = sample(range(1, 11), k=1)[0]
            confederate_df.iloc[0, idx] = new_val
        with st.container():
            st.subheader("Value Prediction Task")
            st.write("For each photo, please guess to what extent personality psychologists may have or may not have endorsed each value statement for the individual depicted in the photo. The personality psychologists used the same scale as you with 1 = *Not at all important to me*, to 10 = *Very important to me*. Please guess how personality psychologists rated the values of the individual in the picture.")

            ptcp, buff, conf = st.columns([1, 0.25, 1])

            ptcp.image(facialimage, width=250)
            conf.image(facialimage, width = 250)

        #q1
            ptcp.radio("Control over others",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                       int(participant_df.at[0,"pQ1"])-1, horizontal=True, key="q1-ptcp")
            conf.radio("Control over others",
                            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                             ], int(confederate_df.at[0, "pQ1"])-1, horizontal=True, key="q1-conf", disabled=True)
        #q2
            ptcp.radio("Achieving goals",
                            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                             ], int(participant_df.at[0,"pQ2"])-1, horizontal=True, key="q2-ptcp")
            conf.radio("Achieving goals",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                        ], int(confederate_df.at[0, "pQ2"])-1, horizontal=True, key="q2-conf", disabled=True)
        #q3
            ptcp.radio("Gratification of desires",
                            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                             ], int(participant_df.at[0,"pQ3"])-1, horizontal=True, key="q3-ptcp")
            conf.radio("Gratification of desires",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                       int(confederate_df.at[0, "pQ3"])-1, horizontal = True, key="q3-conf", disabled=True)
        #q4
            ptcp.radio("Seeking adventure and risk",
                            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                             ], int(participant_df.at[0,"pQ4"])-1, horizontal=True, key="q4-ptcp")
            conf.radio("Seeking adventure and risk",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                        ], int(confederate_df.at[0, "pQ4"])-1, horizontal=True, key="q4-conf", disabled=True)
        #q5
            ptcp.radio("Interested in everything, exploring",
                            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                             ], int(participant_df.at[0,"pQ5"])-1, horizontal=True, key="q5-ptcp")
            conf.radio("Interested in everything, exploring",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                        ], int(confederate_df.at[0, "pQ5"])-1, horizontal=True, key="q5-conf", disabled=True)
        #q6
            ptcp.radio("Preserving nature",
                            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                             ], int(participant_df.at[0,"pQ6"])-1, horizontal=True, key="q6-ptcp")
            conf.radio("Preserving nature",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                        ], int(confederate_df.at[0, "pQ6"])-1, horizontal=True, key="q6-conf", disabled=True)
        #q7
            ptcp.radio("Working for the welfare of others",
                            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                             ], int(participant_df.at[0,"pQ7"])-1, horizontal=True, key="q7-ptcp")
            conf.radio("Working for the welfare of others",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                        ], int(confederate_df.at[0, "pQ7"]) - 1, horizontal=True, key="q7-conf", disabled=True)
        #q8
            ptcp.radio("Submitting to life's circumstances",
                            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                             ], int(participant_df.at[0,"pQ8"])-1, horizontal=True, key="q8-ptcp")
            conf.radio("Submitting to life's circumstances",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                        ], int(confederate_df.at[0, "pQ8"]) - 1, horizontal=True, key="q8-conf", disabled=True)
        #q9
            ptcp.radio("Dutiful, meeting obligations",
                            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                             ], int(participant_df.at[0,"pQ9"])-1, horizontal=True, key="q9-ptcp")
            conf.radio("Dutiful, meeting obligations",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                        ], int(confederate_df.at[0, "pQ9"]) - 1, horizontal=True, key="q9-conf", disabled=True)
        #q10
            ptcp.radio("Neat, tidy",
                             ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                              ], int(participant_df.at[0,"pQ10"])-1, horizontal=True, key="q10-ptcp")
            conf.radio("Neat, tidy",
                       ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                        ], int(confederate_df.at[0, "pQ10"]) - 1, horizontal=True, key="q10-conf", disabled=True)

    else:
        st.session_state.page = 0
        




