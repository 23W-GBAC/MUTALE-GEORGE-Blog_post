# A DEEP DIVE INTO AUTOMATION
Greetings, 
This is the moment for everyone to deeply understand the script I wrote that help me to generate a simple website that displays my circulum vitae or portofolio.
Let me break down how the script or main automation work
## 1. JSON Data:

The JSON file (portfolio_data.json) contains structured data of my portofilio, including projects, skills, education, and contact details.
```
{
    "name": "MUTALE GEORGE",
    
    "profile": "Passionate about technology and healthcare",
    "projects": [
      {
        "title": "Photography",
        "description": "I have been a wedding photography since 2020",
        "link": "https://www.facebook.com/photo/?fbid=471283727677735&set=a.124926355646809"
      },
      {"title": "Graphics",
        "description": "I started this project inorder to improve my photo outputs",
        "link": ""
      },
      {"title": "Programming",
        "description": "Creation of automations is my game.Checkout this",
        "link": "https://23w-gbac.github.io/MUTALE-GEORGE-Blog_post"
      }
    
    ],
    "skills": ["Python", "JSON", "HTML/CSS"],
    "education": [
      {
        "Award": "Uganda Certificate of Education",
        "institution": "Kajjansi Progressive Senior Secondary School",
        "year": 2021
      },
      {
        "Award": "Uganda Advanced Certificate of Education",
        "institution": "Kajjansi Progressive Senior Secondary School",
        "year": 2021
      },
      {
        "Award": "Bachelor of Science in Health Informatics",
        "institution": "Deggendorf Institute of Applied Sciences",
        "year": "Currently enrolled"
      }
    
    ],
    "contact": {
      "email": "mutalegeorge367.com",
      "Facebook": "https://www.facebook.com/george.williamson.3538039",
      "LinkedIn": "https://www.linkedin.com/in/mutale-george-a66466268?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app",
      "github": "https://github.com/GEORGEMUTALE"
    }
  }
  

```
This file is designed in the way that I can I can add more content as I build on my CV with time
## 2. Python Script:

The Python script (generate_portfolio.py) reads the JSON data from the file and uses Jinja2 to render the HTML template.
It defines a function generate_portfolio(data) that takes the data from the JSON file and renders the HTML template with the provided data.
The main() function reads the JSON file, calls the generate_portfolio() function, and writes the generated HTML to an output file (index.html).
The script is set up to run when executed, and it prints a message indicating that the portfolio has been generated successfully.
```
import json
from jinja2 import Environment, FileSystemLoader

def generate_portfolio(data):
    #Give the directory path for the templates
    templates = "C:/Users/User/MUTALE-GEORGE-Blog_post/Scripts/templates"
    env = Environment(loader=FileSystemLoader(templates))
    index_template = env.get_template("index_template.html")
    
  # Give a path where the output should be saved
    with open("C:/Users/User/MUTALE-GEORGE-Blog_post/Scripts/output/index.html", "w") as file:
        file.write(index_template.render(
            name=data["name"],
            profile=data["profile"],
            projects=data["projects"],
            skills=data["skills"],
            education=data["education"],
            contact=data["contact"]
        ))

def main():
    # read the data file but remember to replace the directory path
    with open("C:/Users/User/MUTALE-GEORGE-Blog_post/Scripts/data/portfolio_data.json", "r") as file:
        data = json.load(file)

    generate_portfolio(data)
    print("Portfolio generated successfully.")

if __name__ == "__main__":
    main()


```
## 3. HTML Template:

The HTML template (index_template.html) uses Jinja2 syntax to create a dynamic HTML page. It includes placeholders ({{ name }}, {{ project.title }}, etc.) that will be replaced with actual data during the rendering process.
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ name }} - CV</title>
</head>
<body>
  <h1>{{ name }}</h1>
  <p>{{ profile }}</p>
  <h2>Projects</h2>
  <ul>
    {% for project in projects %}
      <li>
        <strong>{{ project.title }}</strong>: {{ project.description }} - <a href="{{ project.link }}">Link</a>
      </li>
    {% endfor %}
  </ul>
  <h2>Skills</h2>
  <ul>
    {% for skill in skills %}
      <li>{{ skill }}</li>
    {% endfor %}
  </ul>
  <h2>Education</h2>
  <ul>
    {% for education_item in education %}
      <li>
        <strong>{{ education_item.Award }}</strong> - {{ education_item.institution }} ({{ education_item.year }})
      </li>
    {% endfor %}
  </ul>
  <h2>Contact</h2>
  <p>Email: <a href = "{{ contact.email }}">Link</a></p>
  <p>Facebook: <a href = "{{ contact.Facebook }}">Link</a></p>
  <p>LinkedIn: <a href = "{{ contact.LinkedIn }}">Link</a></p>
  <p>github: <a href = "{{ contact.github }}">Link</a></p>
</body>
</html>

```

# POWER OF AUTOMATION
It costed me four weeeks to come up with the scripts that can generate a cv.Right now a person can come up with a cv within 2 minutes in a simple and an organised way.
In most cases CVs are required in several business companies because they summarise ones skills and projects which saves time of convincing an employer.However much this document is an essential document in the business world, 
- Most people lack the creativity of designing one.Actually some see it as tiresome to comeup with a better design to present to their employers.
- In the 5 years time, an employee will only have to feed in the information as required and the cv is automatically generated which reduces the use of papers in the community as well as conserving the environment.
- This format of cv also creates the option of updating your skills as many as you want and can add links to several social media platforms which gives an employer a broad spectrum to dive into your personal projects as far as they would want.

## RECEIVE MY CALL
I am kindly requesting for the class participation to fork my repository and pull requsts in case of any inquire but it would add much more value if you use my template to build your personal cover letters or cirrculum vitae. Remember to always subscribe on my social media platforms follow share like and comment if you find my work helpful.

*[Home](https://23w-gbac.github.io/MUTALE-GEORGE-Blog_post/)*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
*[Previous](Automation2.md)*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*[Generated CV](Generated_CV.md)*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[Back to Repository](https://github.com/23W-GBAC/MUTALE-GEORGE-Blog_post)*

