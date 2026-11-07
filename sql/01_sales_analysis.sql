
-- RETAIL SALES ANALYSIS
-- Project: Retail Sales Data Analysis
-- Database: retail_analysis

-- 1. Total gross sales value
SELECT
    ROUND(SUM(total_price), 2) AS gross_revenue
FROM sales; 