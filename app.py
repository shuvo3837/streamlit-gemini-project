import streamlit as st
from api_calling import Note_generate, audio_transcript, quiz_generator
from PIL import Image
st.title("Note Summary and Quiz Generator")
st.markdown("upload upto 3 images to generate note summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    img = st.file_uploader(
        "upload the photos of your note",
        type = ['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    PIL_img = []

    for i in img:
        pil_image = Image.open(i)   # single image
        PIL_img.append(pil_image) 


    if img:
        if len(img)>3:
            st.error("upload at max 3 img")
        else:
            st.subheader("your uploaded image")
            col = st.columns(len(img))

            for i,img in enumerate(img):
                with col[i]:
                    st.image(img)


    selected_option = st.selectbox(
        "Enter the difficulty of your Quiz",
        ("easy","medium","hard"),
        index=0
    )

    pressed = st.button("Click the button to initiate AI",type="primary")

if pressed:
    if not img:
        st.error("you must upload 1 image")

    else:
        
        with st.container(border = True):
            st.subheader("your note")

            with st.spinner("generate note"):
                generate_notes = Note_generate(PIL_img)
                st.markdown(generate_notes)


        with st.container(border = True):
            st.subheader("audio transcription")
            with st.spinner("translating"):

                generate_notes = generate_notes.replace("#","") \
                    .replace("##","") \
                    .replace("###","") \
                    .replace("*","") \
                    .replace("_","") \
                    .replace("-"," ") \
                    .replace("(","") \
                    .replace(")","") \
                    .replace("[","") \
                    .replace("]","") \
                    .replace("{","") \
                    .replace("}","") \
                    .replace(":","") \
                    .replace(";","") \
                    .replace('"',"") \
                    .replace("'","") \
                    .replace("\n"," ") \
                    .replace("  "," ")

                audio_transcription = audio_transcript(generate_notes)
                st.audio(audio_transcription)

                
        with st.container(border = True):
            st.subheader(f"Quiz ({selected_option}) difficulty")

            with st.spinner("generating quiz"):
                quiz = quiz_generator(PIL_img,selected_option)
                st.markdown(quiz)