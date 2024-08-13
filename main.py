from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import text_file_parser
import argparse


def get_file():
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(
            ["html", "xml"],
        ),
    )

    template = env.get_template("template.html")

    return template


def get_number_years_winery():
    delta = datetime.datetime.now() - datetime.datetime(
        year=1921,
        month=1,
        day=1,
        hour=0,
    )
    age = round(delta.days / 365.2425)

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


def fill_file(
    template,
    years,
    drinks,
):
    rendered_page = template.render(
        years=years,
        drinks=drinks,
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)


def main():
    parser = argparse.ArgumentParser(
        description="Введите здесь путь к текстовому файлу",
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Введите здесь путь к текстовому файлу",
    )
    args = parser.parse_args()
    file_name = args.file
    drinks = text_file_parser.fetch_drinks(file_name)
    template = get_file()
    string_age = get_number_years_winery()
    fill_file(
        template,
        string_age,
        drinks,
    )


if __name__ == "__main__":
    main()
