select
    o.order_id,
    c.customer_key,
    g.geography_key,
    d.date_key,
    o.order_status,
    o.order_timestamp,
    o.shipping_fee
from {{ ref('stg_orders') }} o
join {{ ref('dim_customer') }} c on o.customer_id = c.customer_id
join {{ ref('dim_geography') }} g on c.state = g.state and c.city = g.city
join {{ ref('dim_date') }} d on o.order_timestamp::date = d.full_date
