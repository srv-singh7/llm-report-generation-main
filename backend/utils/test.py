import google.generativeai as genai
import os
from decouple import config
prompt = """
You are an expert sales analyst. 
From the given sales data and business context, generate a list of 3 recommendations, each with a title and description, and separate them by a pipe symbol |
1. The title should be clear, concise, and not longer than the examples given below, 2-4 words.
2. The description should be clear, concise, and not longer than the examples given below, 10-15 words.
3. Don't include anything else than the bullets in your response, without intros.

### Enhance Average Transaction Value
To counter the dip in average transaction value, explore strategies such as bundling complementary products or introducing upsell and cross-sell opportunities
|
### Customer Segmentation
Consider implementing customer segmentation to tailor marketing efforts more effectively
|
### Continuous Training and Development
Continue investing in the training and development of the sales team to ensure they remain at the forefront of industry knowledge and sales techniques

"""
input = "this is related to the sales data and business context of the company"

genai.configure(api_key=config("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

response = model.generate_content(contents = [ input,prompt])

# response = model.chat(messages)
print("debug-1" ,response.text)
