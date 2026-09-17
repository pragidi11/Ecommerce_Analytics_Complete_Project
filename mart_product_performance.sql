select
    p.product_id,
    p.product_name,
    p.category,
    p.subcategory,
    count(distinct fo.order_id) as total_orders,
    sum(fi.quantity) as units_sold,
    sum(fi.net_sales) as total_revenue,
    sum(fi.profit) as total_profit
from {{ ref('fact_order_items') }} fi
join {{ ref('fact_orders') }} fo on fi.order_id = fo.order_id
join {{ ref('dim_product') }} p on fi.product_key = p.product_key
where fo.order_status not in ('cancelled','refunded')
group by 1,2,3,4
