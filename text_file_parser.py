import pandas
import collections


def read_wine_table(table_name):
    products = pandas.read_excel(
        table_name, na_values=None, keep_default_na=False
    ).to_dict(orient="records")
    grouped_products = collections.defaultdict(list)

    for product in products:
        grouped_products[product["Категория"]].append(product)

    return grouped_products


def fetch_drinks(table_name):
    drinks = []
    is_profitable = "Выгодное предложение"

    catalog_drinks = read_wine_table(table_name)

    for drinks_by_type in catalog_drinks:
        drink_units = []
        for drink in catalog_drinks[drinks_by_type]:
            if drink["Категория"] == drinks_by_type:
                drink_info = {
                    "name": drink["Название"],
                    "variety": drink["Сорт"],
                    "price": drink["Цена"],
                    "picture": f'images\{drink["Картинка"]}',
                    "is_profitable": "",
                }

                if drink["Акция"]:
                    drink_info["is_profitable"] = is_profitable
                    drink_units.append(drink_info)

        one_type_drinks = {
            "type": drinks_by_type,
            "units": drink_units,
        }

        drinks.append(one_type_drinks)

    return drinks
