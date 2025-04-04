import streamlit as st
import pandas as pd
from PIL import Image

# --- Load Outfit Recommendations (Mock Data) ---
def load_recommendations():
    data = {
        "Body Shape": ["Rectangle", "Triangle", "Inverted Triangle", "Hourglass", "Apple"],
        "Fair": [
            "Monochromatic outfits, structured blazers, straight-leg pants.",
            "A-line skirts, wide-leg pants, off-shoulder tops.",
            "V-neck tops, dark bottoms, fitted jackets.",
            "Wrap dresses, belted coats, high-waisted pants.",
            "Empire waist dresses, flowy tops, bootcut jeans."
        ],
        "Light": [
            "Vertical stripes, tailored blazers, mid-rise jeans.",
            "Peplum tops, flared skirts, cropped jackets.",
            "Scoop neck tops, straight-leg jeans, layered necklaces.",
            "Bodycon dresses, fitted blazers, pencil skirts.",
            "V-neck tunics, dark leggings, long cardigans."
        ],
        "Medium": [
            "Bold prints, fitted tops, straight-cut trousers.",
            "High-waisted jeans, ruffled tops, wedge heels.",
            "Off-shoulder tops, bootcut pants, structured bags.",
            "Belted trench coats, fitted sweaters, knee-length skirts.",
            "Tunic tops, wide-leg pants, long scarves."
        ],
        "Tan": [
            "Pastel colors, tailored suits, slim-fit trousers.",
            "Wrap tops, flared jeans, statement earrings.",
            "Deep V-necks, slim-fit pants, layered jackets.",
            "Corset tops, high-waisted skirts, pointed heels.",
            "Dark-wash jeans, flowy blouses, long vests."
        ],
        "Dark": [
            "Bright colors, structured dresses, wide belts.",
            "High-neck tops, pencil skirts, ankle boots.",
            "Asymmetrical tops, skinny jeans, bold accessories.",
            "Off-shoulder dresses, cinched waists, stilettos.",
            "Maxi dresses, empire waist tops, draped scarves."
        ]
    }
    return pd.DataFrame(data)

# --- Main App ---
def main():
    st.title("👗 Outfit Recommendation Based on Body Shape & Skin Tone")
    st.markdown("Select your body shape and skin tone to get personalized outfit suggestions!")

    # --- Body Shape Selection ---
    body_shapes = ["Rectangle", "Triangle", "Inverted Triangle", "Hourglass", "Apple"]
    selected_shape = st.selectbox("Select Your Body Shape:", body_shapes)

    # --- Skin Tone Selection ---
    skin_tones = ["Fair", "Light", "Medium", "Tan", "Dark"]
    selected_tone = st.selectbox("Select Your Skin Tone:", skin_tones)

    # --- Get Recommendations ---
    if st.button("Get Outfit Recommendations"):
        df = load_recommendations()
        shape_row = df[df["Body Shape"] == selected_shape]
        recommendation = shape_row[selected_tone].values[0]

        st.subheader(f"Outfit Recommendations for {selected_shape} Body & {selected_tone} Skin:")
        st.write(recommendation)

        # --- Display Example Outfit Images (Optional) ---
        st.subheader("Example Outfits:")
        if selected_shape == "Rectangle":
            st.image("https://example.com/rectangle_outfit.jpg", caption="Rectangle Shape Outfit", width=300)
        elif selected_shape == "Triangle":
            st.image("https://example.com/triangle_outfit.jpg", caption="Triangle Shape Outfit", width=300)
        elif selected_shape == "Inverted Triangle":
            st.image("https://example.com/inverted_outfit.jpg", caption="Inverted Triangle Outfit", width=300)
        elif selected_shape == "Hourglass":
            st.image("https://example.com/hourglass_outfit.jpg", caption="Hourglass Shape Outfit", width=300)
        elif selected_shape == "Apple":
            st.image("https://example.com/apple_outfit.jpg", caption="Apple Shape Outfit", width=300)

if __name__ == "__main__":
    main()