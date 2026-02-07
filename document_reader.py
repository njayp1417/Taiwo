from docx import Document
import PyPDF2
import os

def read_docx(file_path):
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return '\n'.join([page.extract_text() for page in reader.pages])

def save_to_txt(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    files = [f for f in os.listdir('.') if f.endswith(('.docx', '.pdf'))]
    
    for file in files:
        print(f"\nProcessing: {file}")
        
        if file.endswith('.docx'):
            content = read_docx(file)
        else:
            content = read_pdf(file)
        
        output_file = f"{os.path.splitext(file)[0]}.txt"
        save_to_txt(content, output_file)
        print(f"Saved to: {output_file}")
    
    print(f"\nDone! Processed {len(files)} files.")
