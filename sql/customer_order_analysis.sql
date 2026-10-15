
-- 1. View all customer orders
SELECT *
FROM orders;

-- 2. Find completed orders
SELECT *
FROM orders
WHERE order_status = 'Completed';

-- 3. Display latest orders first
SELECT *
FROM orders
ORDER BY order_date DESC;

-- 4. Calculate total revenue
SELECT
    SUM(quantity * unit_price) AS total_revenue
FROM orders
WHERE order_status = 'Completed';

-- 5. Calculate total orders and average order value
SELECT
    COUNT(*) AS total_orders,
    SUM(quantity * unit_price) AS total_revenue,
    AVG(quantity * unit_price) AS average_order_value
FROM orders
WHERE order_status = 'Completed';

-- 6. Analyse revenue by customer
SELECT
    customer_id,
    SUM(quantity * unit_price) AS customer_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM orders
WHERE order_status = 'Completed'
GROUP BY customer_id
ORDER BY customer_revenue DESC;

-- 7. Find products generating the highest revenue
SELECT
    product_id,
    SUM(quantity * unit_price) AS product_revenue,
    SUM(quantity) AS units_sold
FROM orders
WHERE order_status = 'Completed'
GROUP BY product_id
ORDER BY product_revenue DESC;

-- 8. Find products with revenue above 10000
SELECT
    product_id,
    SUM(quantity * unit_price) AS product_revenue
FROM orders
WHERE order_status = 'Completed'
GROUP BY product_id
HAVING SUM(quantity * unit_price) > 10000;

-- 9. Combine product details with sales performance
SELECT
    p.product_name,
    p.category,
    SUM(o.quantity) AS units_sold,
    SUM(o.quantity * o.unit_price) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Completed'
GROUP BY p.product_name, p.category
ORDER BY total_revenue DESC;

-- 10. Rank products by revenue
SELECT
    product_id,
    product_revenue,
    RANK() OVER (
        ORDER BY product_revenue DESC
    ) AS revenue_rank
FROM (
    SELECT
        product_id,
        SUM(quantity * unit_price) AS product_revenue
    FROM orders
    WHERE order_status = 'Completed'
    GROUP BY product_id
) AS product_sales;
