select
    c.customer_id,
    c.customer_name,
    c.state,
    c.city,
    count(distinct fo.order_id) as total_orders,
    sum(fi.quantity) as units_purchased,
    sum(fi.net_sales) as lifetime_revenue,
    sum(fi.profit) as lifetime_profit,
    max(fo.order_timestamp) as last_order_date,
    case when count(distinct fo.order_id) > 1 then true else false end as repeat_customer
from {{ ref('fact_orders') }} fo
join {{ ref('fact_order_items') }} fi on fo.order_id = fi.order_id
join {{ ref('dim_customer') }} c on fo.customer_key = c.customer_key
where fo.order_status not in ('cancelled','refunded')
group by 1,2,3,4
