import streamlit as st
import random
import numpy as np
from PIL import Image
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator

#########
# setting up the api key configuration
#########

api_key = "I6eCsG3fVH6k-L_4MYAbvgD_eoXk1U480UC8GezkUUcc"
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/209d939b-59cb-4001-a707-013244cee735"

authenticator = IAMAuthenticator(apikey=api_key)

langtranslator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)

langtranslator.set_service_url(url)

#########
# retrieving list of tips
#########

with open("list_of_tips.txt") as file:
     contents = file.readlines()

tips = [line.strip("\n") for line in contents]

random_tip = random.choice(tips)

#########
# sidebar
#########

languages_dictionary={"Arabic":"ar","Korean":"ko","Latvian":"lv","Bengali":"bn","Lithuanian":"lt",
"Bosnian":"bs","Malay":"ms","Bulgarian":"bg","Malayalam":"ml","Maltese":"mt","Chinese (Simplified)":"zh",
"Chinese (Traditional)":"zh-TW","Nepali":"ne","Croatian":"hr","Norwegian Bokmål":"nb","Czech":"cs","Polish":"pl",
"Danish":"da","Portuguese":"pt","Dutch":"nl","Romanian":"ro","English":"en","Russian":"ru","Estonian":"et",
"Finnish":"fi","Sinhala":"si","French":"fr","Slovak":"sk","French (Canadian)":"fr","Slovenian":"sl",
"German":"de","Spanish":"es","Greek":"el","Swedish":"sv","Gujarati":"gu","Tamil":"ta","Hebrew":"he","Telugu":"te",
"Hindi":"hi","Thai":"th","Hungarian":"hu","Turkish":"tr","Irish":"ga","Ukrainian":"uk","Indonesian":"id","Urdu":"ur",
"Italian":"it","Vietnamese":"vi","Japanese":"ja","Welsh":"cy"}

available_languages = list(languages_dictionary)

st.sidebar.title("Welcome!")
st.sidebar.markdown("This is a language translator application designed with :heart: specifically for polyglots.")
st.sidebar.text("            ")
st.sidebar.text("            ")
st.sidebar.markdown("**Choose languages that you speak:**")
languages = st.sidebar.multiselect("", available_languages, ['English'])
st.sidebar.text("            ")
st.sidebar.text("            ")

#########
# main
#########

image = Image.open("Polyglot translator.png")
st.image(image, use_column_width=True)

option = st.selectbox(
    'Which language would you choose to type',
    languages)

option1 = st.selectbox('Which language would you like to translate to',
                       languages)


sent = "Enter the text in "+option+" language in the text-area provided below"

sentence = st.text_area(sent, height=250)

if st.button("Translate"):

    try:

        if option == option1:
            st.write("Please Select different Language for Translation")

        else:

            translate_code = languages_dictionary[option]+'-'+languages_dictionary[option1]

            translation = langtranslator.translate(
                text=sentence, model_id=translate_code)

            ans = translation.get_result()['translations'][0]['translation']

            sent1 = 'Translated text in '+option1+' language is shown below'

            st.markdown(sent1)
            st.write(ans)

            st.sidebar.markdown(":bulb: **Language learning tip:**")
            st.sidebar.text("            ")
            st.sidebar.info(f"{random_tip}")

    except:
        st.write("Please do cross check if text-area is filled with sentences or not")
