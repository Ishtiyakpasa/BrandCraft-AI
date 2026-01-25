def brand_name_prompt(industry, tone, target_audience, keywords):
    return f"""
You are a professional branding expert.

Generate 5 unique brand names.

Industry: {industry}
Tone: {tone}
Target Audience: {target_audience}
Keywords: {keywords}

Return ONLY a valid JSON array of strings.
No explanation.
No markdown.

Example:
["BrandOne", "BrandTwo", "BrandThree"]
"""
