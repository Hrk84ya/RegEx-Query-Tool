# RegEx Query Tool 🔍

A professional, web-based regular expression testing tool built with Django. Test and validate regex patterns with real-time matching and detailed results.

![RegEx Tool Screenshot](https://img.shields.io/badge/Django-4.0+-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Real-time Pattern Matching**: Test regex patterns against input text instantly
- **Professional UI**: Modern, responsive design with gradient backgrounds and smooth animations
- **Error Handling**: Clear error messages for invalid regex patterns
- **Match Details**: Shows exact matches with position information
- **Mobile Responsive**: Works seamlessly on desktop and mobile devices
- **Zero Database**: Lightweight tool with no database requirements

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hrk84ya/RegEx-Query-Tool
   cd regex-query-tool
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Open your browser**
   Navigate to `http://127.0.0.1:8000`

## 🎯 Usage

1. **Enter your text** in the "Input Text" area
2. **Write your regex pattern** in the "Regular Expression Pattern" field
3. **Click "Find Matches"** to see results
4. **View matches** with their exact text and position information

### Example Patterns

| Pattern | Description | Example Match |
|---------|-------------|---------------|
| `\\d+` | One or more digits | `123`, `456` |
| `[a-zA-Z]+` | One or more letters | `Hello`, `World` |
| `\\w+@\\w+\\.\\w+` | Simple email pattern | `user@domain.com` |
| `\\b\\w{4}\\b` | Exactly 4-letter words | `test`, `word` |
| `^\\d{3}-\\d{3}-\\d{4}$` | Phone number format | `123-456-7890` |

## 🏗️ Project Structure

```
regex-query-tool/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── regexapp/             # Main Django application
│   ├── settings.py       # Django settings
│   ├── urls.py          # URL routing
│   └── views.py         # Application logic
└── templates/
    └── regex_tool.html   # Main template
```

## 🛠️ Technical Details

### Built With

- **Django 4.0+**: Web framework
- **Python 3.8+**: Programming language
- **HTML5/CSS3**: Frontend markup and styling
- **Font Awesome**: Icons
- **Responsive Design**: Mobile-first approach

### Key Components

- **Views**: Single view handling GET/POST requests for regex testing
- **Templates**: Professional UI with modern CSS styling
- **Error Handling**: Graceful handling of invalid regex patterns
- **No Database**: Stateless application for simplicity

## 🎨 UI Features

- **Modern Design**: Gradient backgrounds and smooth animations
- **Professional Layout**: Clean, organized interface
- **Responsive**: Works on all screen sizes
- **Accessibility**: Proper labels and semantic HTML
- **Visual Feedback**: Clear success/error states

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production Deployment

1. **Set environment variables**
   ```bash
   export DEBUG=False
   export SECRET_KEY='your-production-secret-key'
   export ALLOWED_HOSTS='yourdomain.com'
   ```

2. **Install production server** (e.g., Gunicorn)
   ```bash
   pip install gunicorn
   gunicorn regexapp.wsgi:application
   ```

3. **Configure web server** (Nginx, Apache, etc.)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 👨‍💻 Author

Created with ❤️ by Harsh Kumar

---

**⭐ Star this repository if you find it helpful!**
