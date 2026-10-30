# 🔍 Google SERP Keyword Searcher (English Version)

A reliable full-stack Flask web application for querying Google search results via SerpAPI and exporting structured data into JSON format.

## ✨ Key Features
- **External REST API Integration:** Fetches search results via SerpAPI localized for the Czech Republic (`gl=cz`, `hl=cs`).
- **Resilient Network Layer:** Handles network timeouts and HTTP errors gracefully (`timeout=10` and `requests.RequestException` catch).
- **Security (Zero Leak):** The API key is never hardcoded; it is loaded securely from environment variables (`os.getenv("SERPAPI_KEY")`).
- **Enhanced UX:**
  - Dynamic loading spinner while awaiting the external API response.
  - Multi-click prevention (search button disabled upon submission).
  - Form re-submission prevention on page reload (`window.history.replaceState`).
- **Optimized Data Export:** Results are passed directly to the `/download` endpoint without re-querying the paid API. Provides instant JSON download via HTTP `Content-Disposition: attachment` headers.
- **Unit Test Coverage:** Automated tests powered by `unittest.mock` (simulates success and network failure scenarios with zero API credit consumption and offline capability).

---

## 🚀 Getting Started Locally

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/YOUR-USERNAME/google-serp-searcher.git
cd google-serp-searcher
pip install -r requirements.txt
```

### 2. Configure Environment Variable
Obtain a free API key at [serpapi.com](https://serpapi.com) and export it:
```bash
export SERPAPI_KEY="your_api_key_here"
```

### 3. Run the Development Server
```bash
python app.py
```
The application will be accessible at: `http://localhost:5000`

---

## 🧪 Running Automated Tests
The test suite runs completely offline without consuming API credits:
```bash
python -m unittest test_app.py
```
