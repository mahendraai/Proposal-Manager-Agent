import spacy

nlp = spacy.load('en_core_web_sm')

def summarize_rfp(file):
    # Assuming file is a text-based document (txt, docx converted)
    text = file.read().decode('utf-8')
    doc = nlp(text)
    
    # Extracting keywords as a basic summary (can use more advanced techniques)
    summary = ""
    for sentence in doc.sents:
        if 'scope' in sentence.text.lower() or 'deliverables' in sentence.text.lower():
            summary += sentence.text + "\n"
    
    return summary
