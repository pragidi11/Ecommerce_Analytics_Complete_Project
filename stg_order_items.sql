select
    order_item_id,
    order_id,
    product_id,
    quantity::integer as quantity,
    unit_price::numeric(12,2) as unit_price,
    discount_amount::numeric(12,2) as discount_amount,
    (quantity * unit_price)::numeric(14,2) as gross_sales,
    ((quantity * unit_price) - discount_amount)::numeric(14,2) as net_sales
from raw.order_items
