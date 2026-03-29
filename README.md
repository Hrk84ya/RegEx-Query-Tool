# RegEx Query Tool 🔍

A web-based regular expression testing tool built with Django. Test and validate regex patterns with detailed match results including position information.

![Django](https://img.shields.io/badge/Django-4.0+-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Pattern Matching**: Test regex patterns against input text with `re.finditer`
- **Match Positions**: Each match displays the matched text and its start:end index
- **ReDoS Protection**: 5-second timeout prevents catastrophic backtracking from hanging the server
- **Dark UI**: Warm amber-on-dark theme with JetBrains Mono for code inputs
- **Mobile Responsive**: Works on desktop and mobile
- **Zero Database**: Fully stateless — no database configured or needed

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hrk84ya/RegEx-Query-Tool
   cd RegEx-Query-Tool
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Open your browser** at `http://127.0.0.1:8000`

## 🎯 Usage

1. Paste or type text in the **Input Text** area
2. Enter a regex pattern in the **Regex Pattern** field (shown with `/pattern/g` delimiters)
3. Click **Find Matches**
4. View results — each match shows its index, matched text, and character range

### Example Patterns

| Pattern | Description | Example Match |
|---------|-------------|---------------|
| `\d+` | One or more digits | `123`, `456` |
| `[a-zA-Z]+` | One or more letters | `Hello`, `World` |
| `\w+@\w+\.\w+` | Simple email pattern | `user@domain.com` |
| `\b\w{4}\b` | Exactly 4-letter words | `test`, `word` |
| `^\d{3}-\d{3}-\d{4}` | Phone number format | `123-456-7890` |

## 🏗️ Project Structure

```
RegEx-Query-Tool/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── regexapp/              # Main Django application
│   ├── __init__.py        # Package init
│   ├── settings.py        # Django settings (env-configurable)
│   ├── urls.py            # URL routing
│   ├── views.py           # Regex matching logic with timeout
│   ├── wsgi.py            # WSGI entry point
│   └── asgi.py            # ASGI entry point
└── templates/
    └── regex_tool.html    # Single-page UI template
```

## 🛠️ Technical Details

### Built With

- **Django 4.0+** — web framework
- **Python re module** — regex engine with SIGALRM timeout guard
- **HTML5 / CSS3** — dark themed UI with CSS custom properties
- **Font Awesome 6** — icons
- **JetBrains Mono + Inter** — typography (loaded from Google Fonts)

### Security

- **SECRET_KEY** is generated randomly at startup; set the `SECRET_KEY` env var in production
- **DEBUG**, **ALLOWED_HOSTS** are configurable via environment variables
- **ReDoS protection** — regex execution is wrapped in a 5-second `signal.alarm` timeout

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production

```bash
export DEBUG=False
export SECRET_KEY='your-production-secret-key'
export ALLOWED_HOSTS='yourdomain.com'

pip install gunicorn
gunicorn regexapp.wsgi:application
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created with ❤️ by Harsh Kumar

---

⭐ Star this repository if you find it helpful!
