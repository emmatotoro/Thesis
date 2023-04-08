import streamlit as st

responses = {}

st.title("Interpersonal Perception Task")
st.subheader("Instructions")

st.write("Researchers have long tried to identify the predictors of success. Especially in a highly diverse society such as Canada, interpersonal skills are critical. Perceiving others accurately is important. We have found that people whose perceptions are accurate regardless of another’s race, ethnicity, or gender, are particularly likely to succeed.")
st.write("Based on foundational research conducted at Harvard University and Stanford University, our research group has developed a measure of interpersonal perception, which allows us to predict career success. Research shows that some people are surprisingly good at reading personality information from a person’s face. Moreover, our research shows that people who are good at interpersonal perception succeed regardless of their academic success. That is, regardless of the degrees they hold, people who are good at perceiving others tend to live longer, have higher incomes, have more rewarding relationships, and report higher life satisfaction.")
st.write("We are now at the end of a process in which we develop a shorter version of our test of interpersonal perception. In our short test, we want you to look at just 40 faces and make predictions about them. We believe that our test of only 40 faces will perform about as good as our other much longer test battery. We would like for you to work on two versions of our interpersonal perception task:")
st.write("At the end of the study, you will receive your accuracy based on the match between your answer and actual answers we collected from individuals displayed in the photos.")


st.subheader("Person Perception Task")
st.write("People’s values are an important aspect of their personality, and personality is reflected in the way they look. In the next screen, a series of 8 facial photos will be presented. For each photo, please guess to what extent a person may have or may not have endorsed each value statement. The person used the same scale as you before with 1 = *Not at all important to me*, to 5 = *Very important to me*. Please guess how the person in the picture responded.")
st.write("**Question 1.** Please guess how the person responded to these value statements.")

from PIL import Image
image = Image.open("/Users/emmakehoe/Desktop/image1.jpg")
st.image(image, width = 200)

col1, col2 = st.columns(2)

question1 = st.radio("Control over others",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )

question2 = st.radio("Achieving goals",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )

question3 = st.radio("Gratification of desires",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )

question4 = st.radio("Seeking adventure and risk",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )

question5 = st.radio("Interested in everything, exploring",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )

question6 = st.radio("Preserving nature",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )

question7 = st.radio("Working for the welfare of others",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )


question8 = st.radio("Submitting to life's circumstances",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )

question9 = st.radio("Dutiful, meeting obligations",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )

question10 = st.radio("Neat, tidy",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
                  ], 1, horizontal=True,
                  )


#this is just me testing something out ignore this#
#col1, col2, col3 = st.columns([1,1,1])

#with col1:
  #  st.button('1')
#with col2:
  #  st.button('2')
#with col3:
   # st.button('3')

responses = 'question1'


import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/emmakehoe/Desktop/credentials.json', scope)

client = gspread.authorize(creds)

sheet = client.open('My Streamlit Responses').sheet1

response_data = [responses['question1']]
sheet.append_row(response_data)
