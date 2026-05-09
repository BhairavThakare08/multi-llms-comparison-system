def calculate_metrics(start, end, text):
    return {
        "time": round(end - start, 2),
        "words": len(text.split())
    }
