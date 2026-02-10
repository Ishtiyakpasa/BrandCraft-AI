import frappe
import random # Import random
from frappe.utils.file_manager import save_file
from brandcraft.ai.hugging_phase_image_client import call_hf_image_model
from brandcraft.prompts.prompts import brand_logo_prompt

@frappe.whitelist(allow_guest=True, methods=["POST"])
def generate_brand_logo():
    data = frappe.local.form_dict

    brand_name = data.get("brand_name")
    industry = data.get("industry")
    style = data.get("style")
    colors = data.get("colors")
    icon = data.get("icon")
    target_audience = data.get("target_audience")

    if not industry:
        frappe.throw("Industry is required")

    prompt = brand_logo_prompt(
        brand_name, industry, style, colors, icon, target_audience
    )

    # ✅ Generate a random seed to ensure a different variation every time
    random_seed = random.randint(1, 1000000)

    # ✅ Pass the seed in the call (check your client implementation to ensure it handles it)
    image_bytes = call_hf_image_model(
        model="black-forest-labs/FLUX.1-schnell",
        prompt=prompt,
        seed=random_seed # Add this parameter
    )

    # Add a timestamp or random string to the filename to avoid browser caching issues
    filename = f"{brand_name or 'brand'}_{random_seed}.png"

    file_doc = save_file(
        fname=filename,
        content=image_bytes,
        dt=None,
        dn=None,
        is_private=0
    )

    return {
        "status": "success",
        "logo_url": file_doc.file_url,
        "seed": random_seed # Helpful for debugging
    }