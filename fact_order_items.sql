select
    x.order_item_id,
    x.order_id,
    p.product_key,
    x.quantity,
    x.unit_price,
    x.discount_amount,
    x.gross_sales,
    x.net_sales,
    x.profit
from {{ ref('int_order_detail') }} x
join {{ ref('dim_product') }} p on x.product_id = p.product_id
