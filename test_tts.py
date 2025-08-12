#!/usr/bin/env python3
"""
Test script for the text-to-speech functionality.
Tests the text_to_speech function with various inputs.
"""

import sys
import os

# Add the current directory to the Python path to import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import text_to_speech

def test_text_to_speech():
    """Test the text_to_speech function with various inputs."""
    
    print("🔊 Testing Text-to-Speech Functionality")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        {
            "name": "Spanish Text to Speech",
            "text": "Hola",
            "lang": "es",
            "output_file": "test_spanish.mp3",
            "expected_size_min": 1000  # Minimum expected file size in bytes
        }
    ]
    
    passed_tests = 0
    total_tests = len(test_cases)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test_case['name']}")
        print(f"   Input: '{test_case['text']}' (Language: {test_case['lang']})")
        print(f"   Output file: {test_case['output_file']}")
        
        try:
            # Generate audio
            result = text_to_speech(
                test_case['text'], 
                test_case['lang'], 
                test_case['output_file']
            )
            
            print(f"   Result: '{result}'")
            
            # Check if file exists
            if os.path.exists(result):
                print(f"   ✅ File created successfully")
                
                # Check file size
                file_size = os.path.getsize(result)
                print(f"   File size: {file_size} bytes")
                
                if file_size >= test_case['expected_size_min']:
                    print(f"   ✅ File size is acceptable")
                    passed_tests += 1
                else:
                    print(f"   ❌ FAILED - File too small (expected at least {test_case['expected_size_min']} bytes)")
                    
            else:
                print(f"   ❌ FAILED - File was not created")
                
        except Exception as e:
            print(f"   ❌ FAILED - Error: {str(e)}")
    
    # Test empty input handling
    print(f"\n📝 Test {total_tests + 1}: Empty Input Handling")
    try:
        result = text_to_speech("", "en", "test_empty.mp3")
        print(f"   ❌ FAILED - Should have raised ValueError for empty input")
    except ValueError as e:
        print(f"   ✅ PASSED - Correctly handled empty input: {str(e)}")
        passed_tests += 1
    except Exception as e:
        print(f"   ❌ FAILED - Unexpected error: {str(e)}")
    
    total_tests += 1
    
    # Test invalid language handling
    print(f"\n📝 Test {total_tests + 1}: Invalid Language Handling")
    try:
        result = text_to_speech("Hello", "invalid_lang", "test_invalid.mp3")
        print(f"   ❌ FAILED - Should have raised Exception for invalid language")
    except Exception as e:
        print(f"   ✅ PASSED - Correctly handled invalid language: {str(e)}")
        passed_tests += 1
    
    total_tests += 1
    
    # Clean up test files
    print(f"\n🧹 Cleaning up test files...")
    test_files = ["test_spanish.mp3", "test_empty.mp3", "test_invalid.mp3"]
    for file in test_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"   Removed: {file}")
            except Exception as e:
                print(f"   Could not remove {file}: {str(e)}")
    
    # Summary
    print("\n" + "=" * 50)
    print(f"📊 Test Summary: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! Text-to-speech functionality is working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
        return False

if __name__ == "__main__":
    success = test_text_to_speech()
    sys.exit(0 if success else 1)
