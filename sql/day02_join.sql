SELECT
  customers.name AS customer_name,
  COUNT(orders.customer_id) AS order_count,
  SUM(orders.amount) AS total_amount
FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.name;