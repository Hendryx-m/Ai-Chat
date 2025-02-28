# Ai-Chat 

This mini AI project implements the behavior and characteristics of your typical average AI chat bot.

**Requires Python**
The required python packages are listed in [requirements.txt](requirements.txt).

To install, run :
Powershell
pip install -r requirements.txt
python app.py
**At this point it should say running on https://127.0.0.1:5000/ , to cancel, CTRL + C**
Example:
Invoke-RestMethod -Uri http://127.0.0.1:5000/chat -Method Post -Body '{"message": "Hello, how are you?"}' -ContentType "application/json"

You will then get a response.
