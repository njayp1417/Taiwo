from docx import Document
import PyPDF2
import json
import os
import re

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return '\n'.join([page.extract_text() for page in reader.pages])

def read_docx(file_path):
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_key_concepts(text):
    """Extract key concepts, definitions, and important points from text"""
    concepts = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for definitions (contains "is", "are", "means", "refers to")
        if any(word in line.lower() for word in ['is defined as', 'refers to', 'means', 'is the', 'are the']):
            concepts.append({'type': 'definition', 'text': line, 'context': lines[max(0,i-1):min(len(lines),i+2)]})
        
        # Look for lists or enumerations
        if re.match(r'^\d+[\.\)]\s+', line) or re.match(r'^[a-z][\.\)]\s+', line):
            concepts.append({'type': 'list_item', 'text': line, 'context': lines[max(0,i-1):min(len(lines),i+2)]})
        
        # Look for important statements (contains keywords)
        keywords = ['important', 'key', 'main', 'primary', 'essential', 'fundamental', 'critical', 'significant']
        if any(kw in line.lower() for kw in keywords):
            concepts.append({'type': 'important', 'text': line, 'context': lines[max(0,i-1):min(len(lines),i+2)]})
    
    return concepts

def generate_questions_from_concepts(concepts, course_name):
    """Generate questions from extracted concepts"""
    questions = []
    question_id = 1
    
    for concept in concepts[:100]:  # Limit to avoid too many questions
        text = concept['text']
        
        if concept['type'] == 'definition':
            # Create definition-based questions
            parts = re.split(r'\s+is\s+|\s+are\s+|\s+means\s+|\s+refers to\s+', text, flags=re.IGNORECASE)
            if len(parts) >= 2:
                term = parts[0].strip()
                definition = parts[1].strip()
                
                # Question: What is X?
                questions.append({
                    'id': question_id,
                    'question': f"What is {term}?",
                    'options': [
                        definition[:100],
                        "A type of software application",
                        "A research methodology",
                        "A theoretical framework"
                    ],
                    'correct': 0
                })
                question_id += 1
        
        elif concept['type'] == 'list_item':
            # Create list-based questions
            questions.append({
                'id': question_id,
                'question': f"Which of the following is correct regarding {course_name}?",
                'options': [
                    text[:100],
                    "None of the above",
                    "All of the above",
                    "Only in specific cases"
                ],
                'correct': 0
            })
            question_id += 1
    
    return questions

def generate_general_questions(text, course_name):
    """Generate general questions based on course content"""
    questions = []
    
    # Split into paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 50]
    
    for i, para in enumerate(paragraphs[:30]):  # Limit paragraphs
        sentences = [s.strip() for s in para.split('.') if len(s.strip()) > 20]
        
        for sentence in sentences[:2]:  # Max 2 questions per paragraph
            if len(sentence) > 30:
                questions.append({
                    'id': len(questions) + 1,
                    'question': f"According to the course material, which statement is true?",
                    'options': [
                        sentence[:150],
                        "This is not covered in the course",
                        "The opposite is true",
                        "This only applies in rare cases"
                    ],
                    'correct': 0
                })
    
    return questions

def create_question_database(file_path, output_name):
    """Main function to create question database from a document"""
    print(f"\nProcessing: {file_path}")
    
    # Read document
    if file_path.endswith('.pdf'):
        content = read_pdf(file_path)
    elif file_path.endswith('.docx'):
        content = read_docx(file_path)
    else:
        print(f"Unsupported file type: {file_path}")
        return
    
    # Extract course name from filename
    course_name = os.path.splitext(os.path.basename(file_path))[0]
    course_name = re.sub(r'[^a-zA-Z0-9\s]', '', course_name).replace(' ', '_')
    
    print(f"Extracting concepts from {course_name}...")
    concepts = extract_key_concepts(content)
    
    print(f"Generating questions from {len(concepts)} concepts...")
    questions = generate_questions_from_concepts(concepts, course_name)
    
    # Add general questions
    print("Generating general questions...")
    general_qs = generate_general_questions(content, course_name)
    questions.extend(general_qs)
    
    # Remove duplicates and limit to reasonable number
    unique_questions = []
    seen = set()
    for q in questions:
        q_text = q['question']
        if q_text not in seen and len(unique_questions) < 50:
            seen.add(q_text)
            unique_questions.append(q)
    
    # Reassign IDs
    for i, q in enumerate(unique_questions, 1):
        q['id'] = i
    
    # Create database
    database = {
        'course_name': course_name,
        'questions': unique_questions
    }
    
    # Save to JSON
    output_path = f'databases/{output_name}.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(database, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Created {output_path} with {len(unique_questions)} questions")
    
    # Also save PDF content as text
    pdf_txt_path = f'pdfs/{output_name}.txt'
    with open(pdf_txt_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Saved content to {pdf_txt_path}")

if __name__ == "__main__":
    # Process all documents in current directory
    files = [
        ('CCMAS HANDBOOK HEALTH EDUCATION_okueso (3).pdf', 'health_education'),
        ('COMPUTER APPLICATIONS IN HUMAN KINETICS AND HEALTH EDUCATION_072732.docx', 'computer_applications'),
        ('EHE 201 ABRIDGE.docx', 'ehe_201'),
        ('EHE 211 FIRST LECTURES.pdf', 'ehe_211'),
        ('IGBOKOYI Emergency Health Care Education - OOU EHE 201.docx', 'emergency_healthcare'),
        ('Mass Media Healthcare Education 2E.docx', 'mass_media_healthcare'),
        ('OOU  HED 203  HEALTHY LIFESTYLE EDUCATION.docx', 'healthy_lifestyle'),
        ('OOU EDU 201 - FACULTY OFFICIAL.pdf', 'edu_201'),
        ('OOU EDU 201 - FACULTY OFFICIALS-1.docx', 'edu_201_alt'),
        ('reproductive health.docx', 'reproductive_health'),
        ('SUMMARY NOTE ON ENT211.pdf', 'ent_211')
    ]
    
    for file_name, output_name in files:
        if os.path.exists(file_name):
            try:
                create_question_database(file_name, output_name)
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
    
    print("\n✓ All courses processed!")
    print("Run 'python app.py' to start the website")
