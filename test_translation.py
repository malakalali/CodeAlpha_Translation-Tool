#!/usr/bin/env python3
"""
Test script for the translation functionality.
Tests the translate_text function with various language pairs.
"""

import sys
import os

# Add the current directory to the Python path to import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import translate_text

def test_translation():
    """Test the translate_text function with various language pairs."""
    
    print("🧪 Testing Translation Functionality")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        {
            "name": "English to Spanish",
            "source_lang": "en",
            "target_lang": "es", 
            "text": "Hello",
            "expected_start": "Hola"  # Expected translation should start with "Hola"
        },
        {
            "name": "French to English",
            "source_lang": "fr",
            "target_lang": "en",
            "text": "Bonjour",
            "expected_start": "Good"  # Expected translation should start with "Good" (Good morning)
        }
    ]
    
    passed_tests = 0
    total_tests = len(test_cases)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test_case['name']}")
        print(f"   Input: '{test_case['text']}' ({test_case['source_lang']} → {test_case['target_lang']})")
        
        try:
            # Perform translation
            result = translate_text(
                test_case['source_lang'], 
                test_case['target_lang'], 
                test_case['text']
            )
            
            print(f"   Result: '{result}'")
            
            # Check if result starts with expected translation
            if result.lower().startswith(test_case['expected_start'].lower()):
                print(f"   ✅ PASSED")
                passed_tests += 1
            else:
                print(f"   ❌ FAILED - Expected to start with '{test_case['expected_start']}'")
                
        except Exception as e:
            print(f"   ❌ FAILED - Error: {str(e)}")
    
    # Test empty input handling
    print(f"\n📝 Test {total_tests + 1}: Empty Input Handling")
    try:
        result = translate_text("en", "es", "")
        print(f"   ❌ FAILED - Should have raised ValueError for empty input")
    except ValueError as e:
        print(f"   ✅ PASSED - Correctly handled empty input: {str(e)}")
        passed_tests += 1
    except Exception as e:
        print(f"   ❌ FAILED - Unexpected error: {str(e)}")
    
    total_tests += 1
    
    # Summary
    print("\n" + "=" * 50)
    print(f"📊 Test Summary: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! Translation functionality is working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
        return False

if __name__ == "__main__":
    success = test_translation()
    sys.exit(0 if success else 1)
