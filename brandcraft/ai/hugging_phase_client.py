import frappe
from openai import OpenAI

def call_hf_model(model, prompt):
    api_key = frappe.conf.get("huggingface_api_key")
    if not api_key:
        frappe.throw("Hugging Face API key not configured")

    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200,
    )

    return completion.choices[0].message.content
