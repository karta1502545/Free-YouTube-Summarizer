import os
from pydub import AudioSegment
from groq import Groq
from tqdm import tqdm

def split_audio(file_path, chunk_length_ms=300000):
    audio = AudioSegment.from_file(file_path)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks

def transcribe_audio_chunk(client, chunk, chunk_num, language="zh"):
    chunk_filename = f"audio_chunk_{chunk_num}.mp3"
    chunk.export(chunk_filename, format="mp3")
    with open(chunk_filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(chunk_filename, file.read()),
            model="whisper-large-v3",
            prompt="以下是繁體中文的句子：",
            response_format="json",
            language=language,
            temperature=0.0
        )
        os.remove(chunk_filename)
        return transcription.text

def transcribe_audio(file_path, api_key, chunk_length_ms=300000):
    client = Groq(api_key=api_key)
    chunks = split_audio(file_path, chunk_length_ms)
    all_transcriptions = []

    total_chunks = len(chunks)
    print(f"Total number of chunks: {total_chunks}")

    for i, chunk in enumerate(tqdm(chunks, desc="Transcribing", unit="chunk")):
        transcription_text = transcribe_audio_chunk(client, chunk, i)
        all_transcriptions.append(transcription_text)

    with open("subtitle.txt", 'w', encoding='utf-8') as f:
        f.write("\n".join(all_transcriptions))

    print("All transcription results have been written to subtitle.txt")

# Use the function
api_key = "your_groq_api_key"
filename = "audio.mp3"
transcribe_audio(filename, api_key)
