SELECT
  customers.name AS customer_name,
  COUNT(orders.customer_id) AS order_count,
  COALESCE(SUM(orders.amount), 0) AS total_amount
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.name;