"""import streamlit as st
import pandas as pd
from PIL import Image
import os


# --- Constants ---
IMAGE_WIDTH = 150  # Set your desired width for all images
IMAGE_HEIGHT = 200  # Set your desired height for all images

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

# --- Load Image with Error Handling ---
def load_image(img_path, width=80):
    try:
        if os.path.exists(img_path):
            image = Image.open(img_path)
            return image
        else:
            st.warning(f"Image not found at: {img_path}")
            # Return a placeholder image or None
            return None
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

# --- Main App ---
def main():
    st.title("👗 Outfit Recommendation Based on Body Shape & Skin Tone")
    st.markdown("Select your body shape and skin tone to get personalized outfit suggestions!")

    # Initialize session state for selected shape if it doesn't exist
    if 'selected_shape' not in st.session_state:
        st.session_state.selected_shape = None

    # --- Body Shape Selection ---
    body_shapes_info = {
        "Rectangle": "rectangle_img.png",
        "Triangle": "triangle_img.png",
        "Inverted Triangle": "inverted_triangle_img.png",
        "Hourglass": "hourglass_img.png",
        "Apple": "apple_img.png"
    }
    
    st.subheader("Select Your Body Shape:")
    
    cols = st.columns(len(body_shapes_info))
    for i, (shape, img_path) in enumerate(body_shapes_info.items()):
        with cols[i]:
            image = load_image(img_path)
            if image:
                st.image(image, width=80)
            if st.button(shape):
                st.session_state.selected_shape = shape

    # Display the current selection
    if st.session_state.selected_shape:
        st.write(f"You selected: {st.session_state.selected_shape}")
    else:
        st.write("Please select a body shape")

    # --- Skin Tone Selection ---
    skin_tones = ["Fair", "Light", "Medium", "Tan", "Dark"]
    selected_tone = st.selectbox("Select Your Skin Tone:", skin_tones)

    # --- Get Recommendations ---
    if st.button("Get Outfit Recommendations"):
        if not st.session_state.selected_shape:
            st.warning("Please select a body shape first!")
            return
            
        df = load_recommendations()
        shape_row = df[df["Body Shape"] == st.session_state.selected_shape]
        
        if not shape_row.empty:
            recommendation = shape_row[selected_tone].values[0]
            st.subheader(f"Outfit Recommendations for {st.session_state.selected_shape} Body & {selected_tone} Skin:")
            st.write(recommendation)
        else:
            st.error("No recommendations found for the selected body shape.")

        # --- Display Example Outfit Images (Optional) ---
        # This is just a placeholder - replace with your actual image paths
        st.subheader("Example Outfits:")
        example_images = {
            "Rectangle": "rectangle_outfit.jpg",
            "Triangle": "triangle_outfit.jpg",
            "Inverted Triangle": "inverted_outfit.jpg",
            "Hourglass": "hourglass_outfit.jpg",
            "Apple": "apple_outfit.jpg"
        }
        
        img_path = example_images.get(st.session_state.selected_shape)
        if img_path and os.path.exists(img_path):
            try:
                st.image(img_path, caption=f"{st.session_state.selected_shape} Shape Outfit", width=300)
            except Exception as e:
                st.warning(f"Could not display outfit example: {e}")
        else:
            st.info("Example image not available for this body shape.")

if __name__ == "__main__":
    main()"""
import streamlit as st
import pandas as pd
from PIL import Image
import os

# --- Constants ---
BODY_SHAPE_IMAGE_WIDTH = 150  # Size for body shape selection images
BODY_SHAPE_IMAGE_HEIGHT = 200
OUTFIT_IMAGE_WIDTH = 300      # Larger size for example outfit images
OUTFIT_IMAGE_HEIGHT = 400

# Folder paths
BODY_SHAPE_IMAGES_FOLDER = "bodyshapeimages"
EXAMPLE_OUTFITS_FOLDER = "examples"

# --- Load Outfit Recommendations ---
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

# --- Image Handling Functions ---
def load_and_resize_image(img_path, target_width, target_height, background_color=(240, 240, 240)):
    """Load and resize an image with padding to maintain exact dimensions"""
    try:
        if os.path.exists(img_path):
            image = Image.open(img_path)
            # Resize while maintaining aspect ratio
            image.thumbnail((target_width, target_height))
            # Create new blank image with target size
            new_image = Image.new("RGB", (target_width, target_height), background_color)
            # Paste the resized image centered
            new_image.paste(
                image,
                (
                    (target_width - image.width) // 2,
                    (target_height - image.height) // 2
                )
            )
            return new_image
        return None
    except Exception as e:
        st.error(f"Error loading image {img_path}: {e}")
        return None

def display_image(img_path, width, height, caption=""):
    """Display an image with consistent sizing"""
    resized_img = load_and_resize_image(img_path, width, height)
    if resized_img:
        st.image(resized_img, caption=caption, width=width)
    else:
        # Show placeholder if image not found
        placeholder = Image.new("RGB", (width, height), (240, 240, 240))
        st.image(placeholder, caption="Image not available", width=width)

# --- Get Outfit Image Path ---
def get_outfit_image_path(body_shape, skin_tone):
    """Get the path to the outfit image based on body shape and skin tone"""
    # Mapping of outfit images for each combination
    outfit_images = {
        "Rectangle": {
            "Fair": f"{EXAMPLE_OUTFITS_FOLDER}/rectangle_fair.jpg",
            "Light": f"{EXAMPLE_OUTFITS_FOLDER}/rectangle_light.jpg",
            "Medium": f"{EXAMPLE_OUTFITS_FOLDER}/rectangle_medium.jpg",
            "Tan": f"{EXAMPLE_OUTFITS_FOLDER}/rectangle_tan.jpg",
            "Dark": f"{EXAMPLE_OUTFITS_FOLDER}/rectangle_dark.jpg"
        },
        "Triangle": {
            "Fair": f"{EXAMPLE_OUTFITS_FOLDER}/triangle_fair.jpg",
            "Light": f"{EXAMPLE_OUTFITS_FOLDER}/triangle_light.jpg",
            "Medium": f"{EXAMPLE_OUTFITS_FOLDER}/triangle_medium.jpg",
            "Tan": f"{EXAMPLE_OUTFITS_FOLDER}/triangle_tan.jpg",
            "Dark": f"{EXAMPLE_OUTFITS_FOLDER}/triangle_dark.jpg"
        },
        "Inverted Triangle": {
            "Fair": f"{EXAMPLE_OUTFITS_FOLDER}/inverted_fair.jpg",
            "Light": f"{EXAMPLE_OUTFITS_FOLDER}/inverted_light.jpg",
            "Medium": f"{EXAMPLE_OUTFITS_FOLDER}/inverted_medium.jpg",
            "Tan": f"{EXAMPLE_OUTFITS_FOLDER}/inverted_tan.jpg",
            "Dark": f"{EXAMPLE_OUTFITS_FOLDER}/inverted_dark.jpg"
        },
        "Hourglass": {
            "Fair": f"{EXAMPLE_OUTFITS_FOLDER}/hourglass_fair.jpg",
            "Light": f"{EXAMPLE_OUTFITS_FOLDER}/hourglass_light.jpg",
            "Medium": f"{EXAMPLE_OUTFITS_FOLDER}/hourglass_medium.jpg",
            "Tan": f"{EXAMPLE_OUTFITS_FOLDER}/hourglass_tan.jpg",
            "Dark": f"{EXAMPLE_OUTFITS_FOLDER}/hourglass_dark.jpg"
        },
        "Apple": {
            "Fair": f"{EXAMPLE_OUTFITS_FOLDER}/apple_fair.jpg",
            "Light": f"{EXAMPLE_OUTFITS_FOLDER}/apple_light.jpg",
            "Medium": f"{EXAMPLE_OUTFITS_FOLDER}/apple_medium.jpg",
            "Tan": f"{EXAMPLE_OUTFITS_FOLDER}/apple_tan.jpg",
            "Dark": f"{EXAMPLE_OUTFITS_FOLDER}/apple_dark.jpg"
        }
    }
    
    # Try to get specific image, fall back to generic if not found
    try:
        return outfit_images[body_shape][skin_tone]
    except KeyError:
        # Fallback to generic body shape image if specific tone image doesn't exist
        return f"{EXAMPLE_OUTFITS_FOLDER}/{body_shape.lower()}_outfit.jpg"

# --- Main App ---
def main():
    st.title("👗 Outfit Recommendation Based on Body Shape & Skin Tone")
    st.markdown("Select your body shape and skin tone to get personalized outfit suggestions!")

    # Initialize session state
    if 'selected_shape' not in st.session_state:
        st.session_state.selected_shape = None

    # --- Body Shape Selection Section ---
    st.subheader("1. Select Your Body Shape:")
    
    body_shapes_info = {
        "Rectangle": f"{BODY_SHAPE_IMAGES_FOLDER}/rectangle.png",
        "Triangle": f"{BODY_SHAPE_IMAGES_FOLDER}/triangle.png",
        "Inverted Triangle": f"{BODY_SHAPE_IMAGES_FOLDER}/inverted_triangle.png",
        "Hourglass": f"{BODY_SHAPE_IMAGES_FOLDER}/hourglass.png",
        "Apple": f"{BODY_SHAPE_IMAGES_FOLDER}/apple.png"
    }
    
    # Create columns for body shape selection
    cols = st.columns(len(body_shapes_info))
    for i, (shape, img_path) in enumerate(body_shapes_info.items()):
        with cols[i]:
            # Display consistently sized body shape images
            display_image(
                img_path, 
                BODY_SHAPE_IMAGE_WIDTH, 
                BODY_SHAPE_IMAGE_HEIGHT,
                shape
            )
            if st.button(shape, key=f"btn_{shape}"):
                st.session_state.selected_shape = shape

    # Show current selection
    if st.session_state.selected_shape:
        st.success(f"Selected: {st.session_state.selected_shape}")
    else:
        st.warning("Please select a body shape")

    # --- Skin Tone Selection ---
    st.subheader("2. Select Your Skin Tone:")
    skin_tones = ["Fair", "Light", "Medium", "Tan", "Dark"]
    selected_tone = st.selectbox("Choose your skin tone:", skin_tones, key="skin_tone")

    # --- Get Recommendations ---
    if st.button("Get Outfit Recommendations"):
        if not st.session_state.selected_shape:
            st.error("Please select a body shape first!")
            return
            
        df = load_recommendations()
        shape_row = df[df["Body Shape"] == st.session_state.selected_shape]
        
        if not shape_row.empty:
            try:
                recommendation = shape_row[selected_tone].values[0]
                st.subheader(f"✨ Recommendations for {st.session_state.selected_shape} Body & {selected_tone} Skin:")
                st.write(recommendation)

                # --- Example Outfits Section ---
                st.subheader("🎯 Example Outfit:")
                
                # Get the specific outfit image for this combination
                outfit_path = get_outfit_image_path(st.session_state.selected_shape, selected_tone)
                
                # Display the example outfit with larger consistent size
                display_image(
                    outfit_path,
                    OUTFIT_IMAGE_WIDTH,
                    OUTFIT_IMAGE_HEIGHT,
                    f"Example outfit for {st.session_state.selected_shape} shape and {selected_tone} skin tone"
                )
                
                # Additional styling tips
                st.subheader("💡 Styling Tips:")
                st.markdown("""
                - Choose colors that complement your skin tone
                - Select patterns and fabrics that flatter your body shape
                - Consider your occasion when choosing outfits
                - Always ensure proper fit for your body type
                """)
                
                # Color palette recommendation based on skin tone
                st.subheader("🎨 Recommended Color Palette:")
                color_palettes = {
                    "Fair": "Soft pastels, cool blues, light pinks, and mint greens",
                    "Light": "Dusty roses, warm taupes, soft corals, and sage greens",
                    "Medium": "Rich jewel tones, warm reds, deep greens, and golden yellows",
                    "Tan": "Earth tones, warm oranges, deep browns, and olive greens",
                    "Dark": "Vibrant colors, royal blues, deep purples, and bright whites"
                }
                st.write(color_palettes.get(selected_tone, "Various colors that complement your skin tone"))
                
            except KeyError:
                st.error(f"No recommendations available for {selected_tone} skin tone.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.error(f"No recommendations found for {st.session_state.selected_shape} body shape.")

if __name__ == "__main__":
    main()