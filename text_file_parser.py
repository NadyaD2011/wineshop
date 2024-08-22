import pandas
import collections


def read_wine_table(table_name):
    products = pandas.read_excel(
        table_name, na_values=None, keep_default_na=False
    ).to_dict(orient="records")
    grouped_products = collections.defaultdict(list)

    for product in products:
        grouped_products[product["Категория"]].append(product)

    return catalog_drinks


def parse_text(catalog_drinks):
    drinks = []
    for drinks_by_type in catalog_drinks:
        drink_units = []
        for drink in catalog_drinks[drinks_by_type]:
            if drink["Категория"] == drinks_by_type:
                drink_units.append(parse_drinks(drink))

        one_type_drinks = {
            "type": drinks_by_type,
            "units": drink_units,
        }

        drinks.append(one_type_drinks)

    return drinks


def fetch_drinks(table_name):
    excel_data_df = read_wine_table(table_name)
    drinks = parse_text(excel_data_df)

    return drinks
