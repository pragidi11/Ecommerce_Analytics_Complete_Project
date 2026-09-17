-- Total revenue
SELECT SUM(total_revenue) AS total_revenue
FROM analytics.mart_monthly_revenue;

-- Top 10 products
SELECT product_name, category, units_sold, total_revenue, total_profit
FROM analytics.mart_product_performance
ORDER BY total_revenue DESC
LIMIT 10;

-- Top customers
SELECT customer_name, state, total_orders, lifetime_revenue
FROM analytics.mart_customer_analysis
ORDER BY lifetime_revenue DESC
LIMIT 10;

-- Monthly revenue trend
SELECT month, total_orders, total_revenue, total_profit
FROM analytics.mart_monthly_revenue
ORDER BY month;
