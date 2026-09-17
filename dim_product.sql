select
    row_number() over(order by product_id) as product_key,
    product_id,
    product_name,
    category,
    subcategory,
    unit_cost,
    list_price
from {{ ref('stg_products') }}
