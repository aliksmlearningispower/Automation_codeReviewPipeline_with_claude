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

# prompt = f"""
# You are a senior code reviewer.

# Review these code changes.

# Check:
# - Bugs
# - Security Issues
# - Performance Issues
# - Best Practices

# Provide concise feedback.

# Code:

# {diff}


prompt = f"""
You are a senior code reviewer.

Review these code changes.

Check:
- Bugs
- Security Issues
- Performance Issues
- Best Practices

If is there any syntax error then return "Block Merge Immediately".
If there is no critical issue then return "No critical issues found".

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

critical_keywords = ["Block Merge Immediately"]

for keyword in critical_keywords:
    if keyword.lower() in review.lower():
        print(f"Critical issue found: {keyword}")
        sys.exit(1)

print("No critical  issues found. Code review passed.")