# PersonalProjects

**alarm.py**
Personal alarm clock that you can set for a specific date and time unlike the regular alarm clocks that can be set only within 24 hours. This is a .exe file that can run on Windows. 
References- geeksforgeeks.com, stackoverflow.com

**recommendation.py**
A movie recommender system built using Streamlit and Generative AI (using Gemini AI API)

**recommender_open-ai.py**
A movie recommender system built using Streamlit and Generative AI (using OpenAI API)

**paste_screenshot.py**
Every 15 seconds, the program asks if a screenshot is required. If yes, within the next 5 seconds, it takes the screenshot, giving the user time to set the window to be captured. This loop continues forever until the user terminates the process. I got this idea when I was working with PostgreSQL commands for practice and wanted to capture the commands and their respective output in a folder that I could later push to GitHub. 

**rename_resume.py**
I have been applying to many internships for almost 9 months now and I have a couple of resumes based on the role. But at times, there is some specific technology that the job description mentions, which I have worked on but didn’t add to my resume to avoid cluttering. At times, I also edit certain points based on the role. And while I store the multiple versions of my resume on my laptop, I like to keep the naming consistent and avoid the terms (2), copy, etc. But very often, I have to create multiple folders to keep track of which resume I submit for a particular company. This takes around 10-20 seconds for every application, and if I am submitting my resume with major edits for multiple roles, that takes some additional time. So, I built a short script in Python to save some time. The way it works is - when I make the edits and download my resume, I ensure it is in the following format -FirstNameLastName_Resume_RoleName_Company. This script will create a folder based on the company name and then create a sub-folder for a specific role within the company, all while keeping the file name consistent (FirstNameLastName_Resume.pdf). 
