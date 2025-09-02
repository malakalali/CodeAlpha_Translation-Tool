import streamlit as st
import os
import tempfile
from utils import translate_text, text_to_speech

def main():
    # Page configuration with professional theme
    st.set_page_config(
        page_title="Professional Language Translator",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Professional CSS styling
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hero Section Styling */
    .hero-section {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        padding: 4rem 2rem;
        border-radius: 24px;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    .hero-content {
        display: flex;
        align-items: center;
        gap: 4rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .hero-left {
        flex: 1;
    }
    
    .hero-right {
        flex: 1;
    }
    
    .translation-icon {
        margin-bottom: 2rem;
    }
    
    .icon-circle {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        position: relative;
    }
    
    .icon-text {
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 0.2rem;
    }
    
    .icon-arrow {
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0 0 1rem 0;
        line-height: 1.1;
    }
    
    .title-brand {
        color: #2d3748;
        display: block;
    }
    
    .title-highlight {
        color: #667eea;
        display: block;
    }
    
    .hero-tagline {
        color: #718096;
        font-size: 1.3rem;
        font-weight: 400;
        margin: 0 0 2rem 0;
        line-height: 1.5;
    }
    
    .hero-logos {
        display: flex;
        gap: 1rem;
    }
    
    .logo-item {
        width: 50px;
        height: 50px;
        background: white;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 2px solid #e2e8f0;
    }
    
    .flags-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .flag-item {
        width: 60px;
        height: 60px;
        background: #f7fafc;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .flag-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border-color: #667eea;
    }
    
    .hero-cta {
        margin-top: 2rem;
    }
    
    .cta-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2.5rem;
        font-size: 1.2rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        cursor: pointer;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4);
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
    }
    
    .card-title {
        color: #2d3748;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Language selector styling */
    .language-selector {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Input styling */
    .stTextArea > div > div > textarea {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        padding: 1rem;
        font-size: 1rem;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        font-family: 'Inter', sans-serif;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: white;
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Translation result styling */
    .translation-result {
        background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%);
        border: 2px solid #68d391;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin: 1.5rem 0;
    }
    
    .translation-text {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2d3748;
        margin: 1rem 0;
        line-height: 1.6;
    }
    
    .language-indicator {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        margin: 0.5rem;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Audio section styling */
    .audio-section {
        background: linear-gradient(135deg, #fef5e7 0%, #fed7aa 100%);
        border: 2px solid #f6ad55;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin: 1.5rem 0;
    }
    
    /* Download button styling */
    .download-button {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 1rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
        transition: all 0.3s ease;
    }
    
    .download-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(72, 187, 120, 0.4);
    }
    
    /* Error styling */
    .error-message {
        background: linear-gradient(135deg, #fed7d7 0%, #feb2b2 100%);
        border: 2px solid #fc8181;
        border-radius: 12px;
        padding: 1rem;
        color: #c53030;
        font-weight: 500;
        margin: 1rem 0;
    }
    
    /* Footer styling */
    .footer {
        background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
        color: white;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin-top: 3rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-content {
            flex-direction: column;
            gap: 2rem;
        }
        
        .hero-title {
            font-size: 2.5rem;
        }
        
        .flags-grid {
            grid-template-columns: repeat(3, 1fr);
        }
        
        .flag-item {
            width: 50px;
            height: 50px;
            font-size: 1.5rem;
        }
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
    
    # Hero Section with Flags
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <div class="hero-left">
                <div class="translation-icon">
                    <div class="icon-circle">
                        <span class="icon-text">A</span>
                        <span class="icon-arrow">→</span>
                        <span class="icon-text">文</span>
                    </div>
                </div>
                <h1 class="hero-title">
                    <span class="title-brand">AI powered Language</span>
                    <span class="title-highlight">Translation Tool</span>
                </h1>
                <p class="hero-tagline">Translate with Ease, Your Shortcut to Seamless Language Management!</p>
                <div class="hero-logos">
                    <div class="logo-item">🌐</div>
                    <div class="logo-item">⚡</div>
                    <div class="logo-item">🔊</div>
                </div>
                <div class="hero-cta">
                    <button class="cta-button" onclick="document.querySelector('.translation-section').scrollIntoView({behavior: 'smooth'})">
                        🚀 Get Started
                    </button>
                </div>
            </div>
            <div class="hero-right">
                <div class="flags-grid">
                    <div class="flag-item">🇺🇸</div>
                    <div class="flag-item">🇬🇧</div>
                    <div class="flag-item">🇨🇳</div>
                    <div class="flag-item">🇸🇦</div>
                    <div class="flag-item">🇦🇪</div>
                    <div class="flag-item">🇪🇬</div>
                    <div class="flag-item">🇩🇪</div>
                    <div class="flag-item">🇮🇶</div>
                    <div class="flag-item">🇵🇸</div>
                    <div class="flag-item">🇮🇳</div>
                    <div class="flag-item">🇷🇺</div>
                    <div class="flag-item">🇫🇷</div>
                    <div class="flag-item">🇰🇷</div>
                    <div class="flag-item">🇯🇵</div>
                    <div class="flag-item">🇪🇸</div>
                    <div class="flag-item">🇮🇹</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Language selection card
    st.markdown("""
    <div class="card translation-section">
        <h2 class="card-title">🎯 Language Selection</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Language options
    languages = {
        "🇺🇸 English": "en",
        "🇪🇸 Spanish": "es", 
        "🇫🇷 French": "fr",
        "🇩🇪 German": "de",
        "🇮🇹 Italian": "it",
        "🇵🇹 Portuguese": "pt",
        "🇷🇺 Russian": "ru",
        "🇯🇵 Japanese": "ja",
        "🇰🇷 Korean": "ko",
        "🇨🇳 Chinese (Simplified)": "zh",
        "🇸🇦 Arabic": "ar",
        "🇮🇳 Hindi": "hi",
        "🇳🇱 Dutch": "nl",
        "🇸🇪 Swedish": "sv",
        "🇳🇴 Norwegian": "no",
        "🇩🇰 Danish": "da",
        "🇫🇮 Finnish": "fi",
        "🇵🇱 Polish": "pl",
        "🇹🇷 Turkish": "tr",
        "🇬🇷 Greek": "el"
    }
    
    # Language selection in columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="language-selector">', unsafe_allow_html=True)
        source_lang_name = st.selectbox(
            "**From Language**",
            options=list(languages.keys()),
            index=0,
            help="Select the source language"
        )
        source_lang = languages[source_lang_name]
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="language-selector">', unsafe_allow_html=True)
        target_lang_name = st.selectbox(
            "**To Language**", 
            options=list(languages.keys()),
            index=1,
            help="Select the target language"
        )
        target_lang = languages[target_lang_name]
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Validation
    if source_lang == target_lang:
        st.markdown("""
        <div class="error-message">
            ⚠️ Source and target languages cannot be the same. Please select different languages.
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Text input card
    st.markdown("""
    <div class="card">
        <h2 class="card-title">📝 Text Input</h2>
    </div>
    """, unsafe_allow_html=True)
    
    input_text = st.text_area(
        "Enter your text here",
        placeholder="Type or paste the text you want to translate...",
        height=120,
        help="Enter the text you want to translate"
    )
    
    # Translate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        translate_button = st.button(
            "🔄 Translate Text",
            type="primary",
            disabled=not input_text.strip()
        )
    
    # Translation section
    if translate_button and input_text.strip():
        # Progress indicators
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            status_text.text("🔄 Connecting to translation service...")
            progress_bar.progress(25)
            
            status_text.text("🔄 Translating your text...")
            progress_bar.progress(50)
            
            # Perform translation
            translated_text = translate_text(source_lang, target_lang, input_text.strip())
            
            progress_bar.progress(100)
            status_text.text("✅ Translation complete!")
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
            
            # Display translation result
            st.markdown(f"""
            <div class="translation-result">
                <h3 style="color: #2d3748; margin-bottom: 1rem;">✅ Translation Complete</h3>
                <div class="language-indicator">{source_lang_name.split(' ')[1]}</div>
                <span style="font-size: 1.5rem; color: #667eea;">→</span>
                <div class="language-indicator">{target_lang_name.split(' ')[1]}</div>
                <div class="translation-text">{translated_text}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Success animation
            st.balloons()
            
            # Audio generation section
            st.markdown("""
            <div class="audio-section">
                <h3 style="color: #2d3748; margin-bottom: 1rem;">🔊 Audio Generation</h3>
                <p style="color: #744210; margin-bottom: 1.5rem;">Convert the translation to speech and download as MP3</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🎵 Generate Audio", help="Generate audio file from translation"):
                    with st.spinner("🔊 Generating audio..."):
                        try:
                            # Create temporary file
                            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                                audio_file_path = tmp_file.name
                            
                            # Generate audio
                            audio_file = text_to_speech(
                                translated_text, 
                                target_lang, 
                                audio_file_path
                            )
                            
                            # Read audio file
                            with open(audio_file, "rb") as f:
                                audio_bytes = f.read()
                            
                            # Download button
                            st.markdown("""
                            <div style="text-align: center; margin: 2rem 0;">
                                <h4 style="color: #2d3748; margin-bottom: 1rem;">🎉 Audio Generated Successfully!</h4>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            st.download_button(
                                label="📥 Download Audio (MP3)",
                                data=audio_bytes,
                                file_name=f"translation_{source_lang}_{target_lang}.mp3",
                                mime="audio/mpeg",
                                help="Download the audio file"
                            )
                            
                            # Clean up
                            try:
                                os.unlink(audio_file)
                            except:
                                pass
                                
                        except Exception as e:
                            st.markdown(f"""
                            <div class="error-message">
                                ❌ Audio generation failed: {str(e)}
                            </div>
                            """, unsafe_allow_html=True)
            
        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.markdown(f"""
            <div class="error-message">
                ❌ Translation failed: {str(e)}
            </div>
            """, unsafe_allow_html=True)
    
    # Features section
    st.markdown("""
    <div class="card">
        <h2 class="card-title">✨ Features</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="text-align: center; padding: 1rem;">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">🌐 20+ Languages</h4>
                <p style="color: #718096; font-size: 0.9rem;">Support for major world languages</p>
            </div>
            <div style="text-align: center; padding: 1rem;">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">⚡ Fast Translation</h4>
                <p style="color: #718096; font-size: 0.9rem;">Optimized with caching for speed</p>
            </div>
            <div style="text-align: center; padding: 1rem;">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">🔊 Text-to-Speech</h4>
                <p style="color: #718096; font-size: 0.9rem;">Download translations as MP3</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p style="margin: 0; font-size: 1.1rem;">🌟 Powered by Google Translate and Google Text-to-Speech</p>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.8;">made with love ❤️ by Malak Al Ali</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()