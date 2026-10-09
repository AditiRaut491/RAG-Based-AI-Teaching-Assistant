import whisper
import json
model = whisper.load_model("large-v2") #translate non-english speech to english speech
result = model.transcribe(audio = "audios/sample1.mp3",
                          language = "hi", # hi means hindi language 
                          task = "translate",
                          word_timestamps=False)

print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"],"end": segment["end"],"text": segment["text"] })
print(chunks)

with open ("output.json", "w") as f:
    json.dump(chunks, f)