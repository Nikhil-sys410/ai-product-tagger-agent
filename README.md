🤖 AI-Powered Product Tagging & Trend Analysis Agent

A high-performance Python-based AI agent designed to transform unstructured product descriptions into structured, business-ready metadata and actionable trend intelligence.

🌟 Overview

In modern e-commerce, manual product categorization is slow and prone to error. This project implements an Intelligent Agent that utilizes NLP techniques to automate catalog enrichment and market trend tracking.

Core Capabilities:

Automated Tagging: Extracts Category, Color, Style, and Occasion from raw text.

Trend Intelligence: Analyzes text velocity and keyword frequency to identify emerging market patterns.

Modern UI: A premium, dark-themed dashboard built with Tailwind CSS for seamless user interaction.

🚀 Technical Stack

Backend: Python 3.9+ / Flask (RESTful API Design)

AI Logic: Pattern Matching & Heuristic Analysis (Extensible to LLM integration like Gemini/OpenAI)

Frontend: HTML5, Tailwind CSS (Modern UI/UX), JavaScript (Async/Await API handling)

Styling: Modern Dark-Mode aesthetic with Glassmorphism effects.

🛠️ Installation & Setup

Clone the repository:

git clone (https://github.com/Nikhil-sys410/ai-product-agent.git)
cd ai-product-agent


Create a virtual environment (Recommended):

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


Install dependencies:

pip install flask


Run the application:

python app.py


Access the dashboard at http://127.0.0.1:5000.

📖 Usage Example

Paste the following unstructured text into the agent's input:

"Introducing our new Cyberpunk Limited Edition high-tops. They feature a sleek Midnight Black finish. Ideal for Casual streetwear or high-energy Party environments. A must-have Footwear for the Minimalist enthusiast."

Resulting Data Structure:

{
  "category": "Footwear",
  "color": "Midnight Black",
  "style": "Minimalist",
  "occasion": "Casual",
  "confidence_score": 0.92
}


📂 Project Structure

├── app.py              # Main Flask application & AI Agent logic
├── README.md           # Project documentation
└── static/             # (Optional) Static assets if separated


🛣️ Roadmap & Future Enhancements

[ ] LLM Integration: Connect to Gemini 2.5 Flash for advanced zero-shot extraction.

[ ] Batch Processing: Ability to upload CSV/Excel files for bulk tagging.

[ ] Data Persistence: Integration with Firestore/PostgreSQL to save analyzed trends.

[ ] Visual Analysis: Image-to-Tag capabilities using Computer Vision.

📄 License

Distributed under the MIT License. See LICENSE for more information.

Developed by Nikhil - AI Engineer specializing in Modern Frontend & Python Automation.
