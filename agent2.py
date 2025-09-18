import json
import re
import google.generativeai as genai
import os

genai.configure(api_key="PASTE_YOUR_GEMINI_API_HERE")
model = genai.GenerativeModel("gemini-2.0-flash")

def safe_json_parse(text, fallback_code=""):
    cleaned = re.sub(r"```(json)?", "", text).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"explanation": "Could not parse AI response", "fixed_code": fallback_code}

def fix_code(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    prompt = f"""
    You are an AI coding assistant.
    Task: Analyze the following Python code, explain the errors (if any), and return corrected code.
    Respond strictly in JSON with keys: 'explanation' and 'fixed_code'.

    Code:
    {code}
    """
    response = model.generate_content(prompt)
    print("RAW RESPONSE:\n", response.text, "\n" + "-"*50)

    result = safe_json_parse(response.text, code)
    if "fixed_code" in result:
        with open(file_path, "w") as f:
            f.write(result["fixed_code"])
    else:
        print("⚠️ No fixed_code in result, keeping original file.")

    return result


if __name__ == "__main__":
    file_path = os.path.abspath("example.py")
    result = fix_code(file_path)

    print(json.dumps(result, indent=2))
    print(f"\n✅ Changes applied to {file_path}")
