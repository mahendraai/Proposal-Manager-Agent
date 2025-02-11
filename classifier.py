import docx
from jinja2 import Template

def classify_and_fill(file, template):
    # Simulating section classification using basic keyword detection
    text = file.read().decode('utf-8')
    
    sections = {
        "Scope of Work": extract_section(text, "scope"),
        "Deliverables": extract_section(text, "deliverables"),
        "Timeline": extract_section(text, "timeline")
    }
    
    # Use Jinja2 to fill the template
    with open(f'templates/{template}', 'r') as f:
        template_content = f.read()
    
    filled_template = Template(template_content).render(sections)
    return filled_template

def extract_section(text, keyword):
    # Dummy extraction based on keyword (can be enhanced)
    if keyword in text.lower():
        return f"Extracted {keyword.capitalize()} section"
    else:
        return "Not provided"
