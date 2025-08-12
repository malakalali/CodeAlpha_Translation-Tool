import streamlit as st
import os
import tempfile
from utils import translate_text, text_to_speech

def main():
    # Page configuration
    st.set_page_config(
        page_title="Language Translation Tool",
        page_icon="🌍",
        layout="wide"
    )
    
    # Title and description
    st.title("🌍 Language Translation Tool")
    st.markdown("""
    Translate text between multiple languages and convert the translation to speech.
    Powered by Google Translate and Google Text-to-Speech.
    """)
    
    # Language options (ISO codes)
    languages = {
        "English": "en",
        "Spanish": "es", 
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt",
        "Russian": "ru",
        "Japanese": "ja",
        "Korean": "ko",
        "Chinese (Simplified)": "zh",
        "Arabic": "ar",
        "Hindi": "hi",
        "Dutch": "nl",
        "Swedish": "sv",
        "Norwegian": "no",
        "Danish": "da",
        "Finnish": "fi",
        "Polish": "pl",
        "Turkish": "tr",
        "Greek": "el"
    }
    
    # Create two columns for language selection
    col1, col2 = st.columns(2)
    
    with col1:
        source_lang_name = st.selectbox(
            "Source Language",
            options=list(languages.keys()),
            index=0,
            help="Select the language of your input text"
        )
        source_lang = languages[source_lang_name]
    
    with col2:
        target_lang_name = st.selectbox(
            "Target Language", 
            options=list(languages.keys()),
            index=1,
            help="Select the language you want to translate to"
        )
        target_lang = languages[target_lang_name]
    
    # Validation: Prevent same source and target language
    if source_lang == target_lang:
        st.error("⚠️ Source and target languages cannot be the same. Please select different languages.")
        return
    
    # Text input area
    st.subheader("📝 Enter Text to Translate")
    input_text = st.text_area(
        "Input Text",
        placeholder="Type or paste your text here...",
        height=150,
        help="Enter the text you want to translate"
    )
    
    # Translate button
    translate_button = st.button(
        "🔄 Translate",
        type="primary",
        help="Click to translate your text",
        disabled=not input_text.strip()
    )
    
    # Translation section
    if translate_button and input_text.strip():
        with st.spinner("Translating..."):
            try:
                # Perform translation
                translated_text = translate_text(source_lang, target_lang, input_text.strip())
                
                # Display translation
                st.subheader("✅ Translation Result")
                st.markdown(f"**{source_lang_name} → {target_lang_name}**")
                st.success(translated_text)
                
                # Export Audio section
                st.subheader("🔊 Export Audio")
                st.markdown(f"Convert the translation to speech in {target_lang_name}")
                
                # Audio export button
                if st.button("🎵 Generate Audio", help="Generate audio file from translation"):
                    with st.spinner("Generating audio..."):
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
                            
                            # Read the audio file for download
                            with open(audio_file, "rb") as f:
                                audio_bytes = f.read()
                            
                            # Create download button
                            st.download_button(
                                label="📥 Download Audio (MP3)",
                                data=audio_bytes,
                                file_name=f"translation_{source_lang}_{target_lang}.mp3",
                                mime="audio/mpeg",
                                help="Download the audio file"
                            )
                            
                            # Clean up temporary file
                            try:
                                os.unlink(audio_file)
                            except:
                                pass
                                
                        except Exception as e:
                            st.error(f"❌ Audio generation failed: {str(e)}")
                
            except Exception as e:
                st.error(f"❌ Translation failed: {str(e)}")
    
    # Instructions and tips
    with st.expander("ℹ️ How to use this tool"):
        st.markdown("""
        **Step-by-step guide:**
        1. **Select Languages**: Choose your source and target languages from the dropdowns
        2. **Enter Text**: Type or paste the text you want to translate in the text area
        3. **Translate**: Click the "Translate" button to get your translation
        4. **Export Audio**: Optionally generate and download an audio file of the translation
        
        **Tips:**
        - Make sure source and target languages are different
        - For best results, use complete sentences
        - Audio files are generated in MP3 format
        - Supported languages include major world languages
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("*Powered by Google Translate and Google Text-to-Speech*")

if __name__ == "__main__":
    main()
