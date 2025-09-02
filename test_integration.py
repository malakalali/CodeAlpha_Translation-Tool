#!/usr/bin/env python3
"""
Integration test script for translation and text-to-speech functionality.
Tests the complete workflow: translate text and then convert to speech.
"""

import sys
import os

# Add the current directory to the Python path to import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import translate_text, text_to_speech

def test_integration():
    """Test the complete translation and TTS workflow."""
    
    print("🔄 Testing Translation + TTS Integration")
    print("=" * 50)
    
    # Test case: Translate "Hello" to Spanish and convert to speech
    test_case = {
        "input_text": "Hello",
        "source_lang": "en",
        "target_lang": "es",
        "expected_translation_start": "Hola",
        "output_file": "integration_test.mp3"
    }
    
    print(f"\n📝 Integration Test: English → Spanish Translation + TTS")
    print(f"   Input: '{test_case['input_text']}' ({test_case['source_lang']} → {test_case['target_lang']})")
    
    try:
        # Step 1: Translate the text
        print(f"   🔄 Step 1: Translating...")
        translated_text = translate_text(
            test_case['source_lang'],
            test_case['target_lang'],
            test_case['input_text']
        )
        print(f"   ✅ Translation: '{translated_text}'")
        
        # Verify translation is correct
        if translated_text.lower().startswith(test_case['expected_translation_start'].lower()):
            print(f"   ✅ Translation verified")
        else:
            print(f"   ❌ Translation verification failed")
            return False
        
        # Step 2: Convert to speech
        print(f"   🔊 Step 2: Converting to speech...")
        audio_file = text_to_speech(
            translated_text,
            test_case['target_lang'],
            test_case['output_file']
        )
        print(f"   ✅ Audio file: '{audio_file}'")
        
        # Verify audio file was created
        if os.path.exists(audio_file):
            file_size = os.path.getsize(audio_file)
            print(f"   ✅ Audio file created successfully ({file_size} bytes)")
            
            if file_size > 1000:
                print(f"   ✅ Audio file size is acceptable")
            else:
                print(f"   ❌ Audio file too small")
                return False
        else:
            print(f"   ❌ Audio file was not created")
            return False
        
        # Clean up
        print(f"\n🧹 Cleaning up...")
        if os.path.exists(audio_file):
            os.remove(audio_file)
            print(f"   Removed: {audio_file}")
        
        print(f"\n🎉 Integration test passed! Complete workflow is working.")
        return True
        
    except Exception as e:
        print(f"   ❌ FAILED - Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_integration()
    sys.exit(0 if success else 1)
