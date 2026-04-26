from flask import Flask, render_template, request
import tldextract
import re

app = Flask(__name__)

def analyze_url(url):
    score = 0
    reasons = []
    
    # 1. Check for IP address instead of domain
    if re.search(r'(\d{1,3}\.){3}\d{1,3}', url):
        score += 1
        reasons.append("IP address used instead of domain")

    # 2. Extract domain info
    ext = tldextract.extract(url)
    
    # 3. Check for suspicious subdomains (e.g., login.google.com.secure-update.tk)
    if url.count('.') > 3:
        score += 1
        reasons.append("High number of subdomains")

    # 4. Check for @ symbol (often used to mask real URL)
    if "@" in url:
        score += 1
        reasons.append("contains '@' symbol")

    # 5. Check for common phishing keywords
    keywords = ['login', 'verify', 'bank', 'secure', 'update', 'account']
    if any(keyword in url.lower() for keyword in keywords):
        score += 0.5

    # Final Verdict
    status = "⚠️ MALICIOUS" if score >= 1 else "✅ LEGITIMATE"
    return {"status": status, "score": score, "reasons": reasons}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        target_url = request.form.get('url')
        result = analyze_url(target_url)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
