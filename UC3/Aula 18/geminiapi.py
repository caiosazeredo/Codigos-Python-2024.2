import google.generativeai as genai

genai.configure(api_key="AIzaSyB2fUWrL8InlVd5547lUXUI2LWBgRUTHf0")
pergunta = input("Pergunta ai:")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(pergunta)
print(response.text)