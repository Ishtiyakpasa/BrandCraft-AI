import frappe
from brandcraft.ai.hugging_phase_client import call_hf_model
from brandcraft.prompts.prompts import brand_name_prompt

@frappe.whitelist(allow_guest=True, methods=["POST"])
def generate_brand_name():
    data = frappe.local.form_dict

    industry = data.get("industry")
    tone = data.get("tone")
    target_audience = data.get("target_audience")
    keywords = data.get("keywords")

    if not industry:
        frappe.throw("Industry is required")

    prompt = brand_name_prompt(
        industry, tone, target_audience, keywords
    )

    # THIS IS NOW A STRING
    text = call_hf_model(
        model="Qwen/Qwen3-4B-Instruct-2507:nscale",
        prompt=prompt
    )

    try:
        brand_names = frappe.parse_json(text)
    except Exception:
        frappe.throw("AI response is not valid JSON")

    return {
        "brand_names": brand_names
    }
