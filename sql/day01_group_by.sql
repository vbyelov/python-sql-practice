SELECT
  customer,
  COUNT(amount) AS order_count,
  SUM(amount) AS total_amount
FROM orders
GROUP BY customer;