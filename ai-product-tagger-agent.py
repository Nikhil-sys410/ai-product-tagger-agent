import json
import re
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# --- AI AGENT LOGIC (SIMULATED FOR STANDALONE RUNNABILITY) ---
class TaggingAgent:
    """
    AI Agent that structures unstructured text into catalog metadata.
    In a production environment, this would call an LLM (OpenAI/Gemini).
    Here, it uses sophisticated pattern matching and logic to simulate the behavior.
    """
    def __init__(self):
        self.categories = ["Apparel", "Footwear", "Accessories", "Electronics", "Home Decor"]
        self.colors = ["Midnight Black", "Emerald Green", "Crimson Red", "Ocean Blue", "Sand Beige"]
        self.styles = ["Minimalist", "Vintage", "Cyberpunk", "Bohemian", "Athleisure"]
        self.occasions = ["Formal", "Casual", "Workwear", "Party", "Outdoor"]

    def extract_tags(self, text):
        text_lower = text.lower()
        tags = {
            "category": "Uncategorized",
            "color": "Neutral",
            "style": "Modern",
            "occasion": "Versatile",
            "confidence": 0.92
        }
        
        # Simple heuristic mapping for simulation
        for cat in self.categories:
            if cat.lower() in text_lower: tags["category"] = cat
        for col in self.colors:
            if col.lower().split()[-1] in text_lower: tags["color"] = col
        for sty in self.styles:
            if sty.lower() in text_lower: tags["style"] = sty
        for occ in self.occasions:
            if occ.lower() in text_lower: tags["occasion"] = occ
            
        return tags

class TrendAgent:
    """
    Analyzes multiple text sources to identify 'trending' keywords.
    """
    def analyze_trends(self, corpus):
        # Simulated NLP Trend Analysis
        stop_words = ["the", "and", "is", "for", "with", "this"]
        words = re.findall(r'\w+', corpus.lower())
        filtered_words = [w for w in words if w not in stop_words and len(w) > 3]
        
        # Count frequencies
        freq = {}
        for w in filtered_words:
            freq[w] = freq.get(w, 0) + 1
            
        # Sort and return top "trends"
        sorted_trends = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        return [{"keyword": k, "score": v * 10, "growth": f"+{v*2}%"} for k, v in sorted_trends[:5]]

# Initialize Agents
tagger = TaggingAgent()
trender = TrendAgent()

# --- WEB UI (Single File Architecture) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Product Agent | Intelligence Suite</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #0f172a; color: #f8fafc; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.1); }
        .neon-border { border: 1px solid #6366f1; box-shadow: 0 0 15px rgba(99, 102, 241, 0.3); }
        .gradient-text { background: linear-gradient(90deg, #818cf8, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    </style>
</head>
<body class="min-h-screen p-4 md:p-8">
    <div class="max-w-6xl mx-auto">
        <!-- Header -->
        <header class="flex justify-between items-center mb-12">
            <div>
                <h1 class="text-3xl font-bold gradient-text">ProductAI Agent</h1>
                <p class="text-slate-400 text-sm">Automated Tagging & Trend Intelligence</p>
            </div>
            <div class="flex gap-4">
                <span class="px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-indigo-400 animate-pulse"></span> System Active
                </span>
            </div>
        </header>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Left Panel: Input -->
            <div class="lg:col-span-2 space-y-6">
                <div class="glass p-6 rounded-2xl">
                    <label class="block text-sm font-semibold mb-4 text-slate-300">Product Description Input</label>
                    <textarea id="productText" rows="6" 
                        class="w-full bg-slate-900/50 border border-slate-700 rounded-xl p-4 text-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 transition-all"
                        placeholder="e.g. A vintage-inspired midnight black leather jacket perfect for casual outdoor nights..."></textarea>
                    
                    <div class="mt-4 flex gap-3">
                        <button onclick="processTagging()" class="bg-indigo-600 hover:bg-indigo-500 text-white px-6 py-2.5 rounded-lg font-semibold transition-all flex items-center gap-2">
                            <i class="fas fa-tags"></i> Extract Attributes
                        </button>
                        <button onclick="processTrends()" class="bg-slate-800 hover:bg-slate-700 text-white px-6 py-2.5 rounded-lg font-semibold transition-all flex items-center gap-2">
                            <i class="fas fa-chart-line"></i> Analyze Trends
                        </button>
                    </div>
                </div>

                <!-- Result Area -->
                <div id="resultBox" class="hidden glass p-6 rounded-2xl animate-fade-in">
                    <h3 class="text-lg font-semibold mb-6 flex items-center gap-2">
                        <i class="fas fa-robot text-indigo-400"></i> Agent Intelligence Output
                    </h3>
                    <div id="tagResults" class="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <!-- Dynamic Tags -->
                    </div>
                </div>
            </div>

            <!-- Right Panel: Market Trends -->
            <div class="space-y-6">
                <div class="glass p-6 rounded-2xl">
                    <h3 class="text-lg font-semibold mb-4 flex items-center gap-2">
                        <i class="fas fa-fire text-orange-400"></i> Global Trend Pulse
                    </h3>
                    <div id="trendList" class="space-y-4">
                        <div class="text-slate-500 text-sm italic">Run Trend Analysis to see live patterns...</div>
                    </div>
                </div>

                <div class="glass p-6 rounded-2xl bg-gradient-to-br from-indigo-900/20 to-transparent">
                    <h4 class="text-sm font-bold text-indigo-300 uppercase tracking-wider mb-2">Agent Capability</h4>
                    <ul class="text-xs text-slate-400 space-y-2">
                        <li><i class="fas fa-check text-emerald-500 mr-2"></i> Unstructured to JSON</li>
                        <li><i class="fas fa-check text-emerald-500 mr-2"></i> Zero-Shot Classification</li>
                        <li><i class="fas fa-check text-emerald-500 mr-2"></i> Keyword Velocity Tracking</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        async function processTagging() {
            const text = document.getElementById('productText').value;
            if(!text) return;

            const response = await fetch('/api/tag', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text})
            });
            const data = await response.json();
            
            const box = document.getElementById('resultBox');
            const tagContainer = document.getElementById('tagResults');
            box.classList.remove('hidden');
            
            tagContainer.innerHTML = Object.entries(data).map(([key, val]) => `
                <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-700/50">
                    <p class="text-[10px] uppercase tracking-widest text-slate-500 mb-1">${key}</p>
                    <p class="font-bold text-indigo-300">${val}</p>
                </div>
            `).join('');
        }

        async function processTrends() {
            const text = document.getElementById('productText').value;
            const response = await fetch('/api/trends', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text})
            });
            const data = await response.json();
            
            const list = document.getElementById('trendList');
            list.innerHTML = data.map(item => `
                <div class="flex items-center justify-between p-3 bg-slate-800/40 rounded-lg">
                    <div>
                        <span class="text-sm font-medium text-slate-200">#${item.keyword}</span>
                        <p class="text-[10px] text-emerald-400">${item.growth} velocity</p>
                    </div>
                    <span class="text-xs font-mono text-slate-500">${item.score} pts</span>
                </div>
            `).join('');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/tag', methods=['POST'])
def tag_endpoint():
    data = request.json
    result = tagger.extract_tags(data.get('text', ''))
    return jsonify(result)

@app.route('/api/trends', methods=['POST'])
def trend_endpoint():
    data = request.json
    result = trender.analyze_trends(data.get('text', ''))
    return jsonify(result)

if __name__ == '__main__':
    # Running on port 5000 for standard local development
    app.run(debug=True, port=5000)