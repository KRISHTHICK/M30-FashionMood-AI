import streamlit as st
from PIL import Image
from fashion_utils import get_dominant_color, map_color_to_mood, generate_caption, generate_hashtags

st.set_page_config(page_title="👗 FashionMood AI", layout="wide")

st.title("👗 FashionMood AI – Outfit Mood & Vibe Recommender")
st.markdown("Upload an outfit and get vibe, captions, and hashtag suggestions for your posts.")

uploaded_file = st.file_uploader("📸 Upload Your Outfit Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Outfit", use_column_width=True)

    with st.spinner("Analyzing your outfit..."):
        dominant_color = get_dominant_color(image)
        mood = map_color_to_mood(dominant_color)
        caption = generate_caption(mood)
        hashtags = generate_hashtags(mood)

    st.subheader("🎨 Dominant Outfit Color")
    st.code(f"RGB: {dominant_color}")

    st.subheader("🔮 Detected Mood / Vibe")
    st.success(mood)

    st.subheader("📝 Suggested Instagram Caption")
    st.text_area("Caption:", caption, height=80)

    st.subheader("🏷️ Hashtags")
    st.code(hashtags)

    st.subheader("📍Recommended Occasion")
    occasion = {
        "Bold & Confident": "Perfect for parties, fashion events, streetwear posts.",
        "Fresh & Chill": "Ideal for casual day-outs, cafes, beach vibes.",
        "Cool & Mysterious": "Great for night events, concerts, moody shoots.",
        "Romantic & Warm": "Date nights, brunches, romantic walks.",
        "Minimal & Elegant": "Weddings, interviews, formal evenings."
    }
    st.info(occasion.get(mood, "Wear it anywhere with confidence!"))
