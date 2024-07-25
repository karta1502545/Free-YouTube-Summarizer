# free-YouTube-summarizer

Summarize YouTube videos (or any audio files you have) using Python.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/karta1502545/free-YouTube-summarizer.git
    cd free-YouTube-summarizer
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Download Audio from YouTube

1. Specify the YouTube link in `mp3downloader.py`:

    ```python
    youtube_link = "https://www.youtube.com/watch?v=example"
    ```

2. Run `mp3downloader.py` to download the audio file:

    ```bash
    python mp3downloader.py
    ```

### 2. Transcribe Audio using Whisper

1. Go to [Groq Console](https://console.groq.com) to get your API key.

2. Specify your API key in `whisper_groq.py`:

    ```python
    api_key = "your_groq_api_key"
    ```

3. Run `whisper_groq.py` to transcribe the audio file into text:

    ```bash
    python whisper_groq.py
    ```

### 3. Create Prompt for Summarization

1. Customize the template in `create_prompt.py` if needed.

2. Run `create_prompt.py` to create the prompt for ChatGPT:

    ```bash
    python create_prompt.py
    ```

### 4. Get Summary from ChatGPT

1. Upload the `subtitle.txt` file to [ChatGPT](https://chatgpt.com/).

2. Use the generated prompt to get the summary.

## Contributing

If you would like to contribute, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
