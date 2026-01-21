SELECT name, amount
FROM customers
JOIN orders ON customers.id = orders.customer_id;