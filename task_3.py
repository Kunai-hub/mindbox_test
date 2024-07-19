from pyspark.sql import DataFrameNaFunctions
from pyspark.sql import functions as F


def get_product_category_pairs_and_non_categorized_products(products_df, categories_df, product_category_links_df):
    """
    Возвращает датафрейм со всеми парами «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.

    :param products_df: датафрейм с продуктами._
    :param categories_df: датафрейм с категориями.
    :param product_category_links_df: датафрейм со связями между продуктами и категориями.
    :return: датафрейм с парами «Имя продукта – Имя категории» и именами некатегоризованных продуктов.
    """

    # Объединяем датафреймы по продуктам
    joined_df = products_df.join(
        product_category_links_df, products_df.product_id == product_category_links_df.product_id, "left"
    )

    # Объединяем с датафреймом с категориями по ключу категории
    joined_df = joined_df.join(
        categories_df, product_category_links_df.category_id == categories_df.category_id, "left"
    )

    # Фильтруем некатегоризованные продукты
    non_categorized_products = products_df.join(
        product_category_links_df, products_df.product_id == product_category_links_df.product_id, "left_anti"
    )

    # Выбираем только нужные столбцы
    result_df = joined_df.selectExpr("product_name", "category_name")

    # Добавляем имена некатегоризованных продуктов
    result_df = result_df.union(non_categorized_products.drop_duplicates().selectExpr(
        'product_name without category_name'))

    # Удаляем дубликаты и сортируем по имени продукта
    result_df = result_df.drop_duplicates().sort("product_name")

    return result_df