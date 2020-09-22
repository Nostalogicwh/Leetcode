# Write your MySQL query statement below

SELECT
	p.product_name, 
	s.year,
	s.price
FROM
	Product AS p
	INNER JOIN Sales AS s
		ON p.product_id = s.product_id;