import whisper
import json
import os

model = whisper.load_model("large-v2") 
audios = os.listdir("audios")
print(audios)

for audio in audios:
    if ("-" in audio):
         number = audio.split("-")[0]
         title = audio.split("-")[1][:-4]
         print(number, title)
         result = model.transcribe(audio = f"audios/{audio}",
        #  result = model.transcribe(audio = "audios/sample1.mp3",
                          language = "hi", 
                          task = "translate",
                          word_timestamps=False)
         chunks = []
         for segment in result["segments"]:
             chunks.append({"number":number, "title":title, "start": segment["start"],"end": segment["end"],"text": segment["text"] })
             print(chunks)
             chunks_with_metadata = {"chunks":chunks, "text": result["text"]}
             with open (f"jsons/{audio}.json", "w") as f:
                 json.dump(chunks_with_metadata, f)


# If json file already exists 
# json_file = f"jsons/{audio}.json"

#     if os.path.exists(json_file):
#         print("Already done:", audio)
#         continue