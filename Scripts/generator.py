import json
from jinja2 import Environment, FileSystemLoader

def generate_portfolio(data):
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

