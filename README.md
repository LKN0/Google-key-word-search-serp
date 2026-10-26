# 🔍 Google SERP Keyword Searcher

[🇬🇧 English Version](README-en.md) | [🇨🇿 Česká verze](README-cz.md)

---

A reliable full-stack Flask web application for querying Google search results via SerpAPI and exporting structured data into JSON format.

## ✨ Key Features
- **External REST API Integration:** Fetches search results via SerpAPI localized for the Czech Republic (`gl=cz`, `hl=cs`).
- **Resilient Network Layer:** Handles network timeouts and HTTP errors gracefully (`timeout=10` and `requests.RequestException` catch).
- **Security (Zero Leak):** The API key is never hardcoded; it is loaded securely from environment variables (`os.getenv("SERPAPI_KEY")`).
- **Enhanced UX:** Dynamic loading spinner, button disabling, and form resubmission prevention.
- **Optimized Data Export:** Results are passed directly to the `/download` endpoint without re-querying the paid API. Instant JSON download via HTTP `Content-Disposition: attachment`.
- **Unit Test Coverage:** Automated offline tests powered by `unittest.mock`.

For full setup instructions, see:
- [English Documentation](README-en.md)
- [Česká dokumentace](README-cz.md)
