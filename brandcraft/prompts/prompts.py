def brand_name_prompt(industry, tone, target_audience, keywords, language=None):
    return f"""
You are a professional branding expert.

Generate 5 unique brand names.

Industry: {industry}
Tone: {tone}
Target Audience: {target_audience}
language: {language}
Keywords: {keywords}

Return ONLY a valid JSON array of strings.
No explanation.
No markdown.

Example:
["BrandOne", "BrandTwo", "BrandThree"]
"""

def brand_tagline(brand_name, industry, tone, target_audience, language=None, keywords=None, usp=None, tagline_style=None):
    return f"""
You are a professional branding expert.

Generate 5 unique and catchy brand taglines.

Brand Name: {brand_name}
Industry: {industry}
Tone: {tone}
Target Audience: {target_audience}
Language: {language}
Keywords: {keywords}
Unique Selling Point: {usp}
Tagline Style: {tagline_style}

Each tagline should be short, memorable, and relevant to the brand.

Return ONLY a valid JSON array of strings.
No explanation.
No markdown.

Example:
["Style That Speaks", "Quality You Can Trust", "Designed for Tomorrow"]
"""

def brand_description(brand_name, industry, tone, target_audience, language=None, keywords=None, usp=None, mission=None, values=None, story=None ):
    return f"""
You are a professional branding and marketing expert.

Write a clear, engaging, and professional brand description suitable for an "About Us" section.

Brand Name: {brand_name}
Industry: {industry}
Tone: {tone}
Target Audience: {target_audience}
Language: {language}
Keywords: {keywords}
Unique Selling Point: {usp}
Mission: {mission}
Core Values: {values}
Brand Story: {story}

The description should be:
- Original and well-structured
- Easy to understand
- Aligned with the brand tone
- Suitable for website and marketing use

Length: 120 to 180 words.

Return ONLY a valid JSON object with this format:
{{"description": "generated text here"}}

No explanation.
No markdown.

Example:
{{"description": "UrbanWeave is a modern fashion brand focused on delivering sustainable and affordable clothing for young adults..."}}
"""

def brand_logo_prompt(brand_name, industry, style, colors, icon, target_audience):
    return f"""
A single, high-quality professional logo for "{brand_name}".

CORE REQUIREMENT: 
Generate ONE single logo design centered in the middle of the frame. 
Do NOT create a grid, Do NOT create multiple variations, and Do NOT create a sheet of icons.

Brand Details:
- Name: "{brand_name}" (Ensure correct spelling)
- Industry: {industry}
- Icon: {icon or "a unique minimalist symbol"}
- Style: {style or "modern, clean, flat vector"}
- Color Palette: {colors or "professional high-contrast colors"}

Visual Execution:
- Background: Solid, plain white background only.
- Composition: Large, centered, and isolated. 
- Style: 2D flat design. No 3D effects, no shadows, no photorealism.

Strict Negative Rules:
- No grids, no multiple versions, no collage, no montages.
- No mockups, no t-shirts, no business cards.
- No background elements or environmental scenes.
"""

def brand_banner_prompt(brand_name, industry, style, colors, target_audience):
    return f"""
A professional website hero banner for a brand named "{brand_name}".
Industry: {industry}
Target Audience: {target_audience}

Visual Scene:
- A wide-angle cinematic shot representing {industry}.
- Aesthetic: {style}, modern, high-end.
- Color Palette: {colors}.
- The brand name "{brand_name}" is elegantly integrated into the scene or displayed in clean 3D typography.

Technical Specs:
- Aspect Ratio: 16:9 (Landscape).
- Lighting: Professional studio lighting or natural cinematic sunlight.
- No clutter, no messy details, high-resolution 8k.
- Avoid: Generic stock photo look, blurry faces, or distorted text.
"""