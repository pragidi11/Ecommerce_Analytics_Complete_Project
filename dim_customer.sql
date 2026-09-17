select
    row_number() over(order by customer_id) as customer_key,
    customer_id,
    first_name,
    last_name,
    first_name || ' ' || last_name as customer_name,
    email,
    state,
    city,
    signup_date
from {{ ref('stg_customers') }}
