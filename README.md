# PULSE-ASSIGNMENT3  
AI-Driven Documentation Structure Analyzer

---

## 📌 Project Overview
PULSE-ASSIGNMENT3 is a documentation analysis system designed to extract
high-level product modules and submodules from official documentation
websites. The project converts unstructured help pages into a clean,
structured JSON format that is easy to understand and process.

This system is useful for product analysis, onboarding automation,
knowledge organization, and documentation intelligence applications.

---

## 🎯 Objective
The main objective of this project is to:
- Analyze product documentation URLs
- Identify major functional modules
- Group related features as submodules
- Generate structured JSON output automatically

---

## ⚙️ How the System Works
1. The user provides one or more documentation URLs.
2. The system fetches textual content from the web pages.
3. Meaningful headings and paragraphs are analyzed.
4. Modules are identified using keyword-based rules.
5. Optional AI enhancement is used when available.
6. Final results are formatted into structured JSON.

---

## 🧠 Key Features
- Accepts multiple documentation URLs
- Rule-based module identification
- Optional AI-based enhancement
- Clean and standardized JSON output
- Simple and lightweight implementation
- Easy to run and understand

---

## 🏗️ Project Structure
PULSE-ASSIGNMENT3/
├── main.py # Application entry point
├── fetcher.py # Fetches documentation content
├── analyzer.py # Module and submodule analysis logic
├── formatter.py # Output formatting
├── requirements.txt
├── README.md
└── outputs/ # Sample tested outputs


---

## 📂 Sample Outputs
The `outputs/` folder contains tested JSON results generated from real
documentation websites:

- WordPress Documentation
- Instagram Help Center
- Chargebee Documentation
- Zluri Help Pages

These files demonstrate that the system was tested successfully on
multiple real-world documentation sources.

---

## 🧾 Output Format
The extracted information is returned in the following JSON structure:

```json
[
  {
    "module": "Module Name",
    "Description": "Brief description of the module",
    "Submodules": {
      "Submodule Name": "Submodule description"
    }
  }
]

🛠️ Technologies Used

Python

Requests

BeautifulSoup

Streamlit

JSON

▶️ How to Run the Project

Install required dependencies:

pip install -r requirements.txt


Start the application:

streamlit run main.py


Enter documentation URLs in the UI.

View the extracted modules in JSON format.

🧪 Testing

The project has been tested on multiple official documentation websites.
Sample outputs are included in the repository for verification without
executing the code.

⚠️ Limitations

Rule-based logic may not capture all modules in complex documentation.

AI enhancement depends on API availability.

Deep nested documentation structures are simplified.

🚀 Future Enhancements

Advanced NLP-based module extraction

Support for deep crawling

Improved UI visualization

API endpoint support
