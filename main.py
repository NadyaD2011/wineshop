from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import get_wine_list
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
    age_site = round(datetime.datetime.now().year - 1921)

    number_of_years = age_site % 100
    if number_of_years >= 10 and number_of_years <= 20:
        return f"{age_site} лет"
    else:
        number_of_years = age_site % 10
        if number_of_years == 1:
            return f"{age_site} год"
        elif number_of_years >= 2 and number_of_years <= 4:
            return f"{age_site} года"
        else:
            return f"{age_site} лет"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        help="Название файла таблицы",
    )
    args = parser.parse_args()
    file_name = args.file
    drinks = get_wine_list.fetch_drinks(file_name)
    template = get_template_file()
    rendered_page = template.render(
        years=get_number_years_winery(),
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
