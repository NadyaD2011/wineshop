import pandas as pd
import collections


def read_wine_table(table_path):
    products = pd.read_excel(table_path, na_values=None, keep_default_na=False).to_dict(
        orient="records"
    )
    grouped_products = collections.defaultdict(list)

    for product in products:
        grouped_products[product["Категория"]].append(product)

    return grouped_products