from duckduckgo_search import DDGS
import random

def search_duckduckgo(query):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=3):
            if "body" in r:
                results.append(r["body"])
    return results

def respond_to_user(text):
    text = text.strip()
    
    if len(text) < 2:
        return "❗ أرسل لي شيئًا أستطيع فهمه أكثر."

    responses = search_duckduckgo(text)
    
    if not responses:
        return "🤔 بحثت كثيرًا، لكن لم أجد شيئًا واضحًا لهذا السؤال..."

    # اختيار رد عشوائي من النتائج لواقعية أكثر
    return f"🔎 هذا ما وجدت:\n\n{random.choice(responses)}"
