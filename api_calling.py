from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import os
import io

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

def Note_generate(img):

    prompt = """summarize the picture in note format at mx 100 word, 
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[img,prompt],
    )

    return response.text

def audio_transcript(text):
    speech = gTTS(text,lang='en',slow=False)

    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    
    return audio_buffer

def quiz_generator(img,difficulty):
    
    prompt = f"""generate 5 quiz question based on the image with {difficulty} make sure to add necessary markdown to differentiate the options"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[img,prompt],
    )

    return response.text