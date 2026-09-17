with dates as (
    select generate_series(
        (select min(order_timestamp::date) from {{ ref('stg_orders') }}),
        (select max(order_timestamp::date) from {{ ref('stg_orders') }}),
        interval '1 day'
    )::date as full_date
)
select
    to_char(full_date,'YYYYMMDD')::integer as date_key,
    full_date,
    extract(year from full_date)::integer as year,
    extract(quarter from full_date)::integer as quarter,
    extract(month from full_date)::integer as month,
    to_char(full_date,'Month') as month_name,
    extract(dow from full_date)::integer as day_of_week
from dates
