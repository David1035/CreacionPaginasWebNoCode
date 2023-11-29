import PyPDF2
import spacy
import textdistance

nlp = spacy.load('es_core_news_sm')

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

def process_text(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    return entities

def evaluate_user_input(user_input, entities):
    best_match = None
    highest_similarity = 0
    for entity, label in entities:
        similarity = textdistance.jaccard(user_input.split(), entity.split())
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = (entity, label)
    return best_match

pdf_file_path = 'documento.pdf'
pdf_text = extract_text_from_pdf(pdf_file_path)
extracted_entities = process_text(pdf_text)

user_input = input("Ingresa una entrada: ")

best_match = evaluate_user_input(user_input, extracted_entities)

if best_match:
    entity, label = best_match
    print(f"ingresa los datos a verificar: '{entity}' (Tipo: {label})")
else:
    print("No se encontraron coincidencias.")
