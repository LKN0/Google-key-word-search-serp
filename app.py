import json
import requests
import os
from flask import Flask, render_template, request, Response

app = Flask(__name__)

API_KEY = os.getenv("SERPAPI_KEY")

def get_google_results(keyword):
    params = {
        "engine": "google",
        "q": keyword,
        "gl": "cz",
        "hl": "cs",
        "api_key": API_KEY
    }
    try:
        response = requests.get("https://serpapi.com/search", params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error calling SerpAPI: {e}")
        return []

    organic_results = data.get("organic_results", [])

    clean_results = []
    for item in organic_results:
        clean_results.append({
            "position": item.get("position"),
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet")
        })

    return clean_results

@app.route("/", methods=["GET", "POST"])

def home():
    searched_word = None
    results = []

    if request.method == "POST":
        searched_word = request.form.get("keyword")
        results = get_google_results(searched_word)
        print(f"SUCCESS! User searched for: {searched_word},found: {len(results)}")

    return render_template("index.html", word=searched_word,results=results)


@app.route("/download", methods=["POST"])
def download():
    searched_word = request.form.get("keyword")
    results_raw = request.form.get("results_json", "[]")

    try:
        results = json.loads(results_raw)
    except json.JSONDecodeError:
        results = []

    data = {
        "searched_keyword": searched_word,
        "results": results
    }

    json_text = json.dumps(data, indent=4, ensure_ascii=False)

    return Response(
        json_text,
        mimetype="application/json",
        headers={"Content-Disposition": "attachment; filename=results.json"}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)