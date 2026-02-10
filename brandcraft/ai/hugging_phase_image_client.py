import requests
import frappe

def call_hf_image_model(model, prompt, seed):
    api_key = frappe.conf.get("huggingface_api_key")

    if not api_key:
        frappe.throw("Hugging Face API key not configured")

    url = f"https://router.huggingface.co/hf-inference/models/{model}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "seed": seed, # This ensures variation
            "width": 1024,
            "height": 1024
        }
    }

    response = requests.post(url, headers=headers, json=payload, timeout=120)

    if response.status_code != 200:
        frappe.throw(f"HF Image API Error: {response.text}")

    # ✅ Return raw image bytes (JPEG/PNG)
    return response.content


def call_hf_banner_image_model(model, prompt, seed, width, height):
    api_key = frappe.conf.get("huggingface_api_key")
    if not api_key:
        frappe.throw("Hugging Face API key not configured")

    url = f"https://router.huggingface.co/hf-inference/models/{model}" # Use standard inference URL
    headers = {"Authorization": f"Bearer {api_key}"}

    payload = {
        "inputs": prompt,
        "parameters": {
            "seed": seed,
            "width": width,
            "height": height,
            "target_size": {"width": width, "height": height} # Some models prefer this key
        }
    }

    response = requests.post(url, headers=headers, json=payload, timeout=120)
    
    if response.status_code != 200:
        frappe.throw(f"HF API Error ({response.status_code}): {response.text}")

    return response.content