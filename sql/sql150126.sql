SELECT
  customers.name AS name,
  SUM(orders.amount) AS total_amount
FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.name
HAVING SUM(orders.amount) > 200;