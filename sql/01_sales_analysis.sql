
-- RETAIL SALES ANALYSIS
-- Project: Retail Sales Data Analysis
-- Database: retail_analysis

-- 1. Total gross sales value
SELECT
    ROUND(SUM(total_price), 2) AS gross_revenue
FROM sales; 

--2. Revenue by country
SELECT
    country,
    COUNT(DISTINCT invoice_no) AS total_orders,
    ROUND(SUM(total_price), 2) AS total_revenue
FROM sales
GROUP BY country
ORDER BY total_revenue DESC;

-- 3. Which top 10 products generate the most revenue?
SELECT
    stock_code,
    description,
    SUM(quantity) AS units_sold,
    ROUND(SUM(total_price), 2) AS revenue
FROM sales
GROUP BY stock_code, description
ORDER BY revenue DESC
LIMIT 10;

-- 4. How much revenue does the business generete per month?
SELECT
    year_month,
    COUNT(DISTINCT invoice_no) AS total_orders,
    ROUND(SUM(total_price), 2) AS monthly_revenue
FROM sales
GROUP BY year_month
ORDER BY year_month ASC;

-- 5. On average, how much does a customer spend per order?
SELECT
    COUNT(DISTINCT invoice_no) AS total_orders,
    ROUND(SUM(total_price), 2) AS total_revenue,
    ROUND(
        SUM(total_price) / COUNT(DISTINCT invoice_no),
        2
    ) AS avg_order_value
FROM sales;