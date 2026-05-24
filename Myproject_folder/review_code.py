import os
import subprocess
from groq import Groq

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