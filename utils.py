from deep_translator import GoogleTranslator
from typing import Optional
from gtts import gTTS
import os
import time
from functools import lru_cache

@lru_cache(maxsize=100)
def _cached_translate(source_lang: str, target_lang: str, text: str) -> str:
    """Cached translation function for better performance."""
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(text)

def translate_text(source_lang: str, target_lang: str, text: str) -> str:
    """
    Translate text from source language to target language using Google Translator.
    Optimized with caching for better performance.
    
    Args:
        source_lang (str): Source language code (e.g., 'en', 'es', 'fr')
        target_lang (str): Target language code (e.g., 'en', 'es', 'fr')
        text (str): Text to translate
    
    Returns:
        str: Translated text
    
    Raises:
        ValueError: If text is empty or None
        Exception: If translation fails
    """
    # Handle empty input gracefully
    if not text or text.strip() == "":
        raise ValueError("Text cannot be empty or None")
    
    # Clean and prepare text
    clean_text = text.strip()
    
    try:
        # Use cached translation for better performance
        translated_text = _cached_translate(source_lang, target_lang, clean_text)
        return translated_text
        
    except Exception as e:
        # Raise a clear error if translation fails
        error_msg = str(e)
        if "timeout" in error_msg.lower() or "timed out" in error_msg.lower():
            raise Exception("Translation request timed out. Please check your internet connection and try again.")
        elif "connection" in error_msg.lower() or "network" in error_msg.lower():
            raise Exception("Network connection error. Please check your internet connection and try again.")
        else:
            raise Exception(f"Translation failed: {error_msg}")

def text_to_speech(text: str, lang: str, output_file: str = "output.mp3") -> str:
    """
    Convert text to speech using Google Text-to-Speech (gTTS).
    
    Args:
        text (str): Text to convert to speech
        lang (str): Language code (e.g., 'en', 'es', 'fr')
        output_file (str): Output MP3 file path (default: "output.mp3")
    
    Returns:
        str: Path to the saved MP3 file
    
    Raises:
        ValueError: If text is empty or None
        Exception: If TTS conversion fails
    """
    # Handle empty input gracefully
    if not text or text.strip() == "":
        raise ValueError("Text cannot be empty or None")
    
    try:
        # Create gTTS object
        tts = gTTS(text=text.strip(), lang=lang, slow=False)
        
        # Save the audio file
        tts.save(output_file)
        
        # Verify the file was created and is not empty
        if not os.path.exists(output_file):
            raise Exception("Audio file was not created")
        
        file_size = os.path.getsize(output_file)
        if file_size == 0:
            raise Exception("Audio file is empty")
        
        return output_file
        
    except Exception as e:
        # Raise a clear error if TTS conversion fails
        raise Exception(f"Text-to-speech conversion failed: {str(e)}")

def placeholder_function():
    """
    Placeholder function - will be replaced with actual utility functions
    """
    pass
