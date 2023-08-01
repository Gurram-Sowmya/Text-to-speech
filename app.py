import streamlit as st
import pyttsx3
import base64

def text_to_speech(text, voice_id=0, speed=150):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    # Set voice and speed
    engine.setProperty('voice', voices[voice_id].id)
    engine.setProperty('rate', speed)
    
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()

def main():
    st.title('Text-to-Speech Application')
    
    # Input text from the user
    input_text = st.text_area('Enter your text here:')
    
    # Select voice (0 for male, 1 for female)
    voice_option = st.selectbox('Select voice:', ['Male', 'Female'])
    voice_id = 0 if voice_option == 'Male' else 1
    
    # Select speed of speech
    speed = st.slider('Select speech speed:', 50, 300, 150)
    
    # Convert text to speech and display audio player and download button
    if st.button('Convert'):
        if input_text.strip() != "":
            text_to_speech(input_text, voice_id, speed)
            audio_file = open('output.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            st.success('Conversion successful! You can listen and download the audio.')
            # Generate and display download button
            b64 = base64.b64encode(audio_bytes).decode()
            href = f'<a href="data:file/mp3;base64,{b64}" download="output.mp3"><button>Download Audio</button></a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning('Please enter some text before converting.')
    
    st.info('Developed by Sowmya')  # Replace [Your Name] with your name

if __name__ == '__main__':
    main()
