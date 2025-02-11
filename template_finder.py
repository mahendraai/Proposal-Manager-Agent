templates = {
    "software": "software_proposal_template.docx",
    "financial": "financial_proposal_template.docx"
}

def find_template(summary):
    # Simple keyword matching to find the template
    if "software" in summary.lower():
        return templates["software"]
    elif "financial" in summary.lower():
        return templates["financial"]
    else:
        return "generic_proposal_template.docx"
