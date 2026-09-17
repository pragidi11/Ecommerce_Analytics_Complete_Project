select
    row_number() over(order by state, city) as geography_key,
    state,
    city
from (
    select distinct state, city
    from {{ ref('stg_customers') }}
) x
