def validate(filled_template):
    validation_report = {}
    mandatory_sections = ["Scope of Work", "Deliverables", "Timeline"]
    
    for section in mandatory_sections:
        if section in filled_template:
            validation_report[section] = "Filled"
        else:
            validation_report[section] = "Missing"
    
    return validation_report
