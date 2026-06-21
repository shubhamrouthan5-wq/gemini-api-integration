import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content(
    "Explain Petroleum Engineering"
)

print(response.text)
