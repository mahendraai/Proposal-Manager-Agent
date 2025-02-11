#Developed by Mahendra Ribadiya Proposal Manager AI Agent
from flask import Flask, request, render_template, jsonify
from agents import summarizer, template_finder, classifier, validator, formatter

app = Flask(__name__)

# Route to upload RFP
@app.route('/')
def upload_page():
    return render_template('upload.html')

# Route to handle RFP file upload and processing
@app.route('/process', methods=['POST'])
def process_rfp():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    
    # Step 1: Summarize RFP
    summary = summarizer.summarize_rfp(file)
    
    # Step 2: Find Template
    template = template_finder.find_template(summary)
    
    # Step 3: Classify and Fill Template
    filled_template = classifier.classify_and_fill(file, template)
    
    # Step 4: Validate the Proposal
    validation_report = validator.validate(filled_template)
    
    # Step 5: Format the Final Proposal
    formatted_proposal = formatter.format_document(filled_template)
    
    # Return the results (for MVP, just return text data)
    return jsonify({
        "summary": summary,
        "template": template,
        "validation_report": validation_report,
        "final_proposal": formatted_proposal
    })

if __name__ == "__main__":
    app.run(debug=True)
