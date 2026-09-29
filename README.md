# 🔐 PhishGuard – URL Security Analyzer

PhishGuard is a beginner-friendly Python cybersecurity tool that analyzes URLs for common phishing indicators and provides a simple risk assessment.

The project is designed for educational purposes to demonstrate how suspicious URL characteristics can be identified using Python.

## 🎯 Project Objective

The objective of PhishGuard is to analyze a URL for common phishing-related indicators and help users understand why a URL may appear suspicious.

## ✨ Features

* 🔒 HTTPS security check
* 🌐 IP address detection
* ⚠️ Suspicious keyword detection
* 🔗 `@` symbol detection
* 📏 Unusually long URL detection
* 📊 Risk score from 0–100
* 🚦 LOW, MEDIUM, and HIGH risk classification
* 💡 Security recommendation
* 🖥️ Simple command-line interface

## 🛠️ Technologies Used

* Python 3
* `urllib.parse`
* `re` (Regular Expressions)

## 📂 Project Structure

```text
PhishGuard/
│
├── phishguard.py
├── README.md
└── .gitignore
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Radhikaajadeja/PhishGuard-URL-Analyzer.git
```

### 2. Open the project folder

```bash
cd PhishGuard-URL-Analyzer
```

### 3. Run the program

```bash
python phishguard.py
```

### 4. Enter a URL

Example:

```text
https://www.google.com
```

The program analyzes the URL and displays the detected indicators, risk score, risk level, and recommendation.

## 🧪 Example

### Suspicious URL

```text
http://192.168.1.10/login?verify=account
```

Possible output:

```text
Risk Score: 65/100
Risk Level: HIGH

Detected Indicators:
- No HTTPS connection
- IP address used instead of domain name
- Suspicious keyword detected: login
- Suspicious keyword detected: verify
- Suspicious keyword detected: account

Recommendation:
Treat this URL with caution.
```

## 📚 What I Learned

Through this project, I practiced:

* Python programming
* URL parsing
* Regular expressions
* Basic phishing detection concepts
* Risk scoring logic
* Git and GitHub
* Writing technical documentation

## ⚠️ Disclaimer

PhishGuard is an **educational cybersecurity project**.

It uses simple heuristic checks and **cannot guarantee that a URL is safe or malicious**. A low-risk result does not mean that a website is trustworthy.

Do not use this tool as a replacement for professional security analysis or trusted URL reputation services.

## 👩‍💻 Author

**Radhikaba Jadeja**

MSc / Computer Science Student
Interested in Cybersecurity & Information Security

## ⭐ Future Improvements

Possible future enhancements include:

* Integration with threat-intelligence APIs
* Domain reputation checking
* WHOIS information
* DNS analysis
* URL reputation databases
* Web-based user interface
* More advanced phishing detection techniques

---

⭐ If you find this project useful for learning, consider giving the repository a star.
