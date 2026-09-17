select
    p.payment_id,
    p.order_id,
    p.payment_method,
    p.payment_amount,
    p.payment_timestamp
from {{ ref('stg_payments') }} p
