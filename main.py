from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import text_file_parser
import argparse


def get_template_file():
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(
            ["html", "xml"],
        ),
    )

    template = env.get_template("template.html")

    return template


def get_number_years_winery():
    age = round(datetime.datetime.now() - 1921)

    number_of_years = age % 100
    if number_of_years >= 10 and number_of_years <= 20:
        return f"{age} лет"
    else:
        number_of_years = age % 10
        if number_of_years == 1:
            return f"{age} год"
        elif number_of_years >= 2 and number_of_years <= 4:
            return f"{age} года"
        else:
            return f"{age} лет"


def main():
    parser = argparse.ArgumentParser(
        description="Путь к файлу таблицы",
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Путь к файлу таблицы",
    )
    args = parser.parse_args()
    file_name = args.file
    drinks = text_file_parser.fetch_drinks(file_name)
    template = get_file()
    string_age = get_number_years_winery()
    rendered_page = template.render(
        years=string_age,
        drinks=drinks,
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(
        ("0.0.0.0", 8000),
        SimpleHTTPRequestHandler,
    )
    server.serve_forever()


if __name__ == "__main__":
    main()
