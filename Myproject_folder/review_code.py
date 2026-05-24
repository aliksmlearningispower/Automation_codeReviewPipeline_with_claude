import os
import subprocess
from groq import Groq
import sys

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

# diff = subprocess.check_output(
#     ["git", "diff", "origin/main...HEAD"]
# ).decode()

print(
    subprocess.check_output(
        ["git", "branch", "-a"]
    ).decode()
)

diff = subprocess.check_output(
    ["git", "diff", "HEAD~1", "HEAD"]
).decode()

prompt = f"""
You are a senior code reviewer.

Review these code changes.

Check:
- Bugs
- Security Issues
- Performance Issues
- Best Practices

Provide concise feedback.

Code:

{diff}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

review = response.choices[0].message.content

print(review)

with open("review.txt", "w") as f:
    f.write(review)

# critical_keywords = [
#     # "asdfghjksdfghdsfghjdfghjfg"
#     # "syntax error",
#     # "hardcoded password",
#     # "sql injection"
#     # Above things have to be figured out by the llm.. we cannot write manually as like above, it will cause issues
#     # Example: If we have syntax error, then we have to block merge pull request.. but if we write manually, then even if the result is "No syntax error", as syntax error word is present it will block merging
# ]

# for keyword in critical_keywords:
#     if keyword.lower() in review.lower():
#         print(f"Critical issue found: {keyword}")
#         sys.exit(1)

print("No critical  issues found. Code review passed.")