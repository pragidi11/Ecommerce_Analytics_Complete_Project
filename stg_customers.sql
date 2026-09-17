select
    customer_id,
    trim(first_name) as first_name,
    trim(last_name) as last_name,
    lower(trim(email)) as email,
    upper(trim(state)) as state,
    trim(city) as city,
    signup_date::date as signup_date
from raw.customers
