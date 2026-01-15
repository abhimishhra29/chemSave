"""
Minimal Streamlit frontend for the ChemCheck application.
"""
import streamlit as st

from client import APIError, identify_chemical


st.set_page_config(page_title="ChemCheck", page_icon="🧪")

st.title("🧪 ChemCheck")
st.write("Upload a label image to extract details.")

image = st.file_uploader("Label image", type=["png", "jpg", "jpeg"])

if st.button("Run OCR", type="primary"):
    if not image:
        st.error("Upload an image to continue.")
        st.stop()

    with st.spinner("Processing..."):
        try:
            result_data = identify_chemical(front_image=image, back_image=None)
        except APIError as exc:
            st.error(f"API error: {exc}")
            st.stop()
        except ValueError as exc:
            st.error(f"Invalid input: {exc}")
            st.stop()

    def display_value(label: str, value: str | None) -> None:
        st.markdown(f"**{label}:** {value or '—'}")

    display_value("Product Name", result_data.get("product_name"))
    display_value("Product Code", result_data.get("product_code"))
    display_value("CAS Number", result_data.get("cas_number"))
    display_value("Manufacturer", result_data.get("manufacturer_name"))
    display_value("Manufacturer URL", result_data.get("manufacturer_url"))
    display_value("SDS URL", result_data.get("sds_search_results"))
    display_value(
        "Validation Status",
        str(result_data.get("validation_status"))
        if result_data.get("validation_status") is not None
        else None,
    )

    ocr_text = result_data.get("ocr_text")
    if ocr_text:
        st.text_area("OCR Text", ocr_text, height=300)
    else:
        st.info("No OCR text returned.")
