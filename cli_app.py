#!/usr/bin/env python3
"""
Command-line interface for the Language Translation Tool.
This is a simple CLI version to demonstrate functionality without Streamlit.
"""

import os
import tempfile
from utils import translate_text, text_to_speech

def main():
    print("🌍 Language Translation Tool - CLI Version")
    print("=" * 50)
    
    # Language options (ISO codes)
    languages = {
        "1": ("English", "en"),
        "2": ("Spanish", "es"), 
        "3": ("French", "fr"),
        "4": ("German", "de"),
        "5": ("Italian", "it"),
        "6": ("Portuguese", "pt"),
        "7": ("Russian", "ru"),
        "8": ("Japanese", "ja"),
        "9": ("Korean", "ko"),
        "10": ("Chinese (Simplified)", "zh"),
        "11": ("Arabic", "ar"),
        "12": ("Hindi", "hi"),
        "13": ("Dutch", "nl"),
        "14": ("Swedish", "sv"),
        "15": ("Norwegian", "no"),
        "16": ("Danish", "da"),
        "17": ("Finnish", "fi"),
        "18": ("Polish", "pl"),
        "19": ("Turkish", "tr"),
        "20": ("Greek", "el")
    }
    
    # Display language options
    print("\nAvailable languages:")
    for key, (name, code) in languages.items():
        print(f"  {key}. {name} ({code})")
    
    # Get source language
    while True:
        try:
            source_choice = input("\nSelect source language (1-20): ").strip()
            if source_choice in languages:
                source_lang_name, source_lang = languages[source_choice]
                break
            else:
                print("Invalid choice. Please select 1-20.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return
    
    # Get target language
    while True:
        try:
            target_choice = input("Select target language (1-20): ").strip()
            if target_choice in languages:
                target_lang_name, target_lang = languages[target_choice]
                if target_lang == source_lang:
                    print("Source and target languages cannot be the same. Please select different languages.")
                    continue
                break
            else:
                print("Invalid choice. Please select 1-20.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return
    
    # Get input text
    print(f"\nTranslating from {source_lang_name} to {target_lang_name}")
    input_text = input("Enter text to translate: ").strip()
    
    if not input_text:
        print("No text entered. Exiting.")
        return
    
    # Perform translation
    print("\n🔄 Translating...")
    try:
        translated_text = translate_text(source_lang, target_lang, input_text)
        print(f"✅ Translation: {translated_text}")
        
        # Ask if user wants audio
        audio_choice = input("\nGenerate audio file? (y/n): ").strip().lower()
        if audio_choice in ['y', 'yes']:
            print("🔊 Generating audio...")
            try:
                # Create a temporary file for the audio
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                    audio_file_path = tmp_file.name
                
                # Generate audio
                audio_file = text_to_speech(
                    translated_text, 
                    target_lang, 
                    audio_file_path
                )
                
                print(f"✅ Audio file created: {audio_file}")
                print(f"📁 File size: {os.path.getsize(audio_file)} bytes")
                
                # Ask if user wants to keep the file
                keep_choice = input("Keep the audio file? (y/n): ").strip().lower()
                if keep_choice not in ['y', 'yes']:
                    os.unlink(audio_file)
                    print("Audio file deleted.")
                else:
                    print(f"Audio file saved as: {audio_file}")
                    
            except Exception as e:
                print(f"❌ Audio generation failed: {str(e)}")
        
    except Exception as e:
        print(f"❌ Translation failed: {str(e)}")

if __name__ == "__main__":
    main()
