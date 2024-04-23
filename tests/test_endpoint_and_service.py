import os
import json
from fastapi.testclient import TestClient
import pytest

from main import result

client = TestClient(result)

os.environ["NLTK_DATA"] = "/usr/share/nltk_data"
import nltk
nltk.download("vader_lexicon")

from services.text_analyzer import analyze_text


# Define test cases
@pytest.mark.parametrize(
        "input_text, expected_label", [
            ("I love this product!", "positive"),
            ("I hate this product!", "negative"),
            ("This product is normal.", "neutral"),
            ("", "neutral")  
        ])

def test_analyze_comment(input_text, expected_label):  
    response = client.post("/analyze_comment", json={"text": input_text})
    assert response.status_code == 200
    data = response.json()
    assert data["label"] == expected_label


def test_analyze_text():
    results = analyze_text("This is a positive comment.")
    assert results["label"] == "positive"
    assert results["score"] > 0

def test_analyze_text_long_text():
    long_text = "a" * 10000  # Very long text
    results = analyze_text(long_text)
    assert results["label"] == "neutral"  # Assuming sentiment analyzer would label it as neutral

def test_analyze_comment_file_write():
    # Clear the file if it already exists
    with open("analyzed_comments.jsonl", "w") as f:
        f.write("")

    response = client.post("/analyze_comment", json={"text": "This is a comment."})
    assert response.status_code == 200

    # Check if the file was written correctly
    with open("analyzed_comments.jsonl", "r") as f:
        lines = f.readlines()
        assert len(lines) == 1
        data = json.loads(lines[0])
        assert "text" in data
        assert "score" in data
        assert "label" in data
        assert "timestamp" in data

def test_analyze_comment_error_handling():
    # Test if service function handles errors gracefully
    with pytest.raises(Exception):
        analyze_text(None)  # Passing None should raise an exception


