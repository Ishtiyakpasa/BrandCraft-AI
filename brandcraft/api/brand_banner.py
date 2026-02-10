import frappe
import random
from frappe.utils.file_manager import save_file
from brandcraft.ai.hugging_phase_image_client import call_hf_banner_image_model
from brandcraft.prompts.prompts import brand_banner_prompt

@frappe.whitelist(allow_guest=True, methods=["POST"])
def generate_brand_banner():
    data = frappe.local.form_dict

    brand_name = data.get("brand_name")
    industry = data.get("industry")
    style = data.get("style") or "cinematic and minimalist"
    colors = data.get("colors") or "brand-appropriate professional colors"
    target_audience = data.get("target_audience")

    if not brand_name or not industry:
        frappe.throw("Brand Name and Industry are required")

    # Generate the banner-specific prompt
    prompt = brand_banner_prompt(brand_name, industry, style, colors, target_audience)

    random_seed = random.randint(1, 999999)

    # ✅ Call model with Banner Dimensions (e.g., 1280x720 or 1024x576)
    image_bytes = call_hf_banner_image_model(
        model="black-forest-labs/FLUX.1-schnell",
        prompt=prompt,
        seed=random_seed,
        width=1024,
        height=576
    )

    filename = f"{brand_name.replace(' ', '_')}_banner_{random_seed}.png"

    file_doc = save_file(
        fname=filename,
        content=image_bytes,
        dt=None,
        dn=None,
        is_private=0
    )

    return {
        "status": "success",
        "banner_url": file_doc.file_url,
        "dimensions": "1024x576"
    }