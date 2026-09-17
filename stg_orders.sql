select
    order_id,
    customer_id,
    lower(trim(order_status)) as order_status,
    order_timestamp::timestamp as order_timestamp,
    shipping_fee::numeric(12,2) as shipping_fee
from raw.orders
