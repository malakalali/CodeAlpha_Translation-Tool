# Language Translation Tool

A comprehensive language translation tool built with Python that supports text translation and text-to-speech functionality.

## Features ✅

- **Text Translation**: Translate text between 20+ languages using Google Translate
- **Text-to-Speech**: Convert translated text to speech and download as MP3 files
- **Multiple Interfaces**: Both command-line (CLI) and web-based (Streamlit) interfaces
- **Error Handling**: Robust error handling for empty inputs and unsupported languages
- **File Management**: Automatic temporary file cleanup and download functionality

## Supported Languages

The tool supports 20+ languages including:
- English, Spanish, French, German, Italian, Portuguese
- Russian, Japanese, Korean, Chinese (Simplified), Arabic
- Hindi, Dutch, Swedish, Norwegian, Danish, Finnish
- Polish, Turkish, Greek

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Virtual Environment Setup

1. **Navigate to the project directory:**
   ```bash
   cd language-translation-tool
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```
   
   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface (CLI) - Recommended

The CLI version is fully functional and doesn't require Streamlit:

```bash
python cli_app.py
```

**Features:**
- Interactive language selection
- Text translation with real-time feedback
- Optional audio file generation
- File management (keep or delete audio files)

### Web Interface (Streamlit) - Optional

**Note:** Streamlit installation may have dependency issues on some systems. The CLI version provides the same functionality.

To run the web interface (if Streamlit is available):

```bash
streamlit run app.py
```

**Features:**
- Modern web interface with dropdown menus
- Real-time translation display
- Audio file download functionality
- Responsive design with helpful tooltips

## Project Structure
```
language-translation-tool/
├── app.py              # Streamlit web application
├── cli_app.py          # Command-line interface
├── utils.py            # Core translation and TTS functions
├── test_translation.py # Translation function tests
├── test_tts.py         # Text-to-speech function tests
├── test_integration.py # Integration tests
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── venv/              # Virtual environment
```

## Core Functions

### Translation
```python
from utils import translate_text

# Translate text from English to Spanish
translated = translate_text("en", "es", "Hello")
print(translated)  # Output: "Hola"
```

### Text-to-Speech
```python
from utils import text_to_speech

# Convert text to speech and save as MP3
audio_file = text_to_speech("Hola", "es", "output.mp3")
print(f"Audio saved to: {audio_file}")
```

## Testing

Run the test suites to verify functionality:

```bash
# Test translation functionality
python test_translation.py

# Test text-to-speech functionality
python test_tts.py

# Test complete integration
python test_integration.py
```

## Dependencies
- **deep-translator**: Translation library (Google Translate)
- **gTTS**: Google Text-to-Speech
- **pyperclip**: Clipboard operations (for future features)
- **streamlit**: Web application framework (optional)

## Development Status
- [x] Project structure setup
- [x] Translation logic implementation
- [x] Text-to-speech integration
- [x] User interface development (CLI + Streamlit)
- [x] Testing and validation
- [ ] Clipboard functionality (next step)
- [ ] Auto-play audio (next step)

## Troubleshooting

### Streamlit Installation Issues
If you encounter issues installing Streamlit due to pyarrow compilation problems:
1. Use the CLI version instead: `python cli_app.py`
2. The CLI provides the same functionality as the web interface

### Audio File Issues
- Ensure you have write permissions in the current directory
- Audio files are automatically cleaned up unless you choose to keep them
- MP3 files are typically 1-10KB in size depending on text length

## Contributing

Feel free to contribute by:
- Adding new language support
- Improving error handling
- Enhancing the user interface
- Adding new features

## License

This project is open source and available under the MIT License.
