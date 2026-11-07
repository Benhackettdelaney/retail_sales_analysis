
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

