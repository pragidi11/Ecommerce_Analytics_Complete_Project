select
    oi.order_item_id,
    o.order_id,
    o.customer_id,
    oi.product_id,
    o.order_status,
    o.order_timestamp,
    o.shipping_fee,
    oi.quantity,
    oi.unit_price,
    oi.discount_amount,
    oi.gross_sales,
    oi.net_sales,
    p.unit_cost,
    (oi.net_sales - (oi.quantity * p.unit_cost))::numeric(14,2) as profit
from {{ ref('stg_order_items') }} oi
join {{ ref('stg_orders') }} o on oi.order_id = o.order_id
join {{ ref('stg_products') }} p on oi.product_id = p.product_id
