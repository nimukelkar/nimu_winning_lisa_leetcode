# Write your MySQL query statement below
SELECT name AS Customers FROM Customers c
WHERE c.id NOT IN 
(SELECT customerId FROM Orders)