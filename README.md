# AI Code Fixer

An AI-powered tool that detects and fixes errors in Python files using the **Google Gemini API**.  
It reads your code, explains the issue, and overwrites the file with corrected code.

## Setup
```bash
pip install google-generativeai
export GEMINI_API_KEY="your_api_key"   # Linux/Mac
setx GEMINI_API_KEY "your_api_key"     # Windows
```
## Usage
```
python agent.py
```

## Example
```
Input (example.py):

print("Hello"


Output:

{
  "explanation": "You missed a closing parenthesis.",
  "fixed_code": "print(\"Hello\")"
}


Fixed file:

print("Hello")
```
