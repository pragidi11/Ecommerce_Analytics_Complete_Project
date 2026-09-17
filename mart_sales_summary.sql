select
    d.full_date as order_date,
    count(distinct fo.order_id) as total_orders,
    count(distinct fo.customer_key) as total_customers,
    sum(fi.quantity) as units_sold,
    sum(fi.net_sales) as total_revenue,
    sum(fi.profit) as total_profit,
    round(sum(fi.net_sales) / nullif(count(distinct fo.order_id),0),2) as average_order_value
from {{ ref('fact_orders') }} fo
join {{ ref('fact_order_items') }} fi on fo.order_id = fi.order_id
join {{ ref('dim_date') }} d on fo.date_key = d.date_key
where fo.order_status not in ('cancelled','refunded')
group by 1
order by 1
