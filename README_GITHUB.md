# 📚 Taiwo's Study Hub

A web-based learning platform with PDF resources and CBT (Computer-Based Testing) exam system. Built with Flask, featuring automatic question generation from course materials.

![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-3.0.0-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

- 📖 **PDF Reader** - Read course materials directly in browser
- ✍️ **CBT Exam System** - Randomized questions for practice
- 🤖 **Auto Question Generation** - AI extracts questions from PDFs
- ⏱️ **Timer** - Track exam progress
- 📊 **Instant Results** - Get scores immediately
- 📱 **Responsive Design** - Works on all devices

## 🚀 Quick Start

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/taiwo-study-hub.git
cd taiwo-study-hub
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open browser**
```
http://localhost:5000
```

### Using the Platform

1. **Read Materials** - Click "📖 Read Material" on any course
2. **Take Exams** - Click "✍️ Take Exam" for practice tests
3. **View Results** - Get instant feedback and scores

## 📚 Available Courses

- Health Education
- Computer Applications in Human Kinetics
- EHE 201 - Emergency Healthcare
- EHE 211 - Emergency Health Lectures
- Mass Media Healthcare Education
- HED 203 - Healthy Lifestyle Education
- EDU 201 - Education Fundamentals
- Reproductive Health
- ENT 211 - Entrepreneurship

## 🔧 Project Structure

```
taiwo/
├── app.py                 # Main Flask application
├── generate_questions.py  # AI question generator
├── document_reader.py     # PDF/DOCX reader
├── requirements.txt       # Python dependencies
├── databases/             # Question databases (JSON)
├── pdfs/                  # Course materials
├── templates/             # HTML templates
│   ├── home.html
│   ├── course.html
│   ├── exam.html
│   └── pdf_viewer.html
└── static/                # Static files
```

## 🤖 Auto Question Generation

The system automatically generates questions from course materials:

```bash
python generate_questions.py
```

**How it works:**
1. Reads PDF and DOCX files
2. Extracts key concepts and definitions
3. Generates 30-50 questions per course
4. Creates randomized exam pools

## 🎯 Adding New Courses

1. Add PDF/DOCX files to the project root
2. Run the question generator:
```bash
python generate_questions.py
```
3. Restart the application
4. New courses appear automatically!

## 📊 Question Database Format

```json
{
  "course_name": "Course Name",
  "questions": [
    {
      "id": 1,
      "question": "Question text?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct": 0
    }
  ]
}
```

## 🌐 Deployment

### Heroku

```bash
heroku create taiwo-study-hub
git push heroku main
```

### Render

1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`

### PythonAnywhere

1. Upload files to your account
2. Set up virtual environment
3. Configure WSGI file to point to `app.py`

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **PDF Processing**: PyPDF2
- **Document Processing**: python-docx
- **Data Storage**: JSON

## 📝 API Endpoints

- `GET /` - Home page with course list
- `GET /course/<course_name>` - Course reading page
- `GET /exam/<course_name>` - Exam page
- `GET /api/get_questions/<course_name>` - Get random questions
- `POST /api/submit_exam` - Submit exam answers
- `GET /pdf/<course_name>` - View PDF
- `GET /pdf_content/<course_name>` - View as text

## 🎓 Grading System

- **90-100%**: Excellent! 🌟
- **80-89%**: Very Good! 👏
- **70-79%**: Good! 👍
- **60-69%**: Fair 📚
- **Below 60%**: Keep Studying! 💪

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Taiwo**

## 🙏 Acknowledgments

- Built for educational purposes
- Inspired by the need for accessible study materials
- Thanks to all contributors

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Made with ❤️ for students**
