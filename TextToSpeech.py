from gtts import gTTS

text = input("Enter the text you want to convert to speech: ")

language = 'en'

obj = gTTS(text=text, lang=language, slow=False)
file_name = input("Enter the file name to save (e.g., sample.mp3): ")
obj.save(file_name)

print(f"Speech saved as {file_name}")
