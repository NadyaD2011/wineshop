import pandas
import collections


def parse_drinks(drink):
    is_profitable = "Выгодное предложение"
    drink_info = {
        "name": drink["Название"],
        "variety": drink["Сорт"],
        "price": drink["Цена"],
        "picture": f'images\{drink["Картинка"]}',
        "is_profitable": "",
    }
    
    if drink["Акция"]:
        drink_info["is_profitable"] = is_profitable

    return drink_info


def read_wine_table(table_name):
    excel_data_df = pandas.read_excel(
        table_name, sheet_name="Лист1", keep_default_na=False
    )
    excel_data_df = excel_data_df.to_json(orient="records", force_ascii=False)
    excel_data_df = list(json.loads(excel_data_df))
    catalog_drinks = collections.defaultdict(list)
    catalog_drinks["Красные вина"]
    catalog_drinks["Белые вина"]
    catalog_drinks["Напитки"]

    for index_wine in range(len(excel_data_df)):
        catalog_drinks[excel_data_df[index_wine]["Категория"]].append(
            excel_data_df[index_wine]
        )

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
