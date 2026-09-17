select
    payment_id,
    order_id,
    initcap(trim(payment_method)) as payment_method,
    payment_amount::numeric(14,2) as payment_amount,
    payment_timestamp::timestamp as payment_timestamp
from raw.payments
