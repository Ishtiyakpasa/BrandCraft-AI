import frappe
from brandcraft.ai.hugging_phase_client import call_hf_model
from brandcraft.prompts.prompts import brand_description

@frappe.whitelist(allow_guest=True, methods=["POST"])
def generate_brand_description():
    data = frappe.local.form_dict

    brand_name = data.get("brand_name") 
    industry = data.get("industry")
    tone = data.get("tone")
    target_audience = data.get("target_audience")
    language = data.get("language")

    keywords = data.get("keywords")
    usp = data.get("usp")

    mission = data.get("mission")
    values = data.get("values")
    story = data.get("story")

    if not industry:
        frappe.throw("Industry is required")
    
    if not brand_name:
        frappe.throw("Brand Name is required")

    prompt = brand_description(
        brand_name, industry, tone, target_audience, language, keywords, usp, mission, values, story
    )

    # THIS IS NOW A STRING
    text = call_hf_model(
        model="Qwen/Qwen3-4B-Instruct-2507:nscale",
        prompt=prompt
    )

    try:
        brand_descriptions = frappe.parse_json(text)
    except Exception:
        frappe.throw("AI response is not valid JSON")

    return {
        "brand_descriptions": brand_descriptions
    }
