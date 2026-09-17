select
    product_id,
    trim(product_name) as product_name,
    initcap(trim(category)) as category,
    initcap(trim(subcategory)) as subcategory,
    unit_cost::numeric(12,2) as unit_cost,
    list_price::numeric(12,2) as list_price
from raw.products
