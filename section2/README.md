# Section 2: Databases
docker build -t my-postgres-db ./
docker run -d --name my-postgresdb-container -p 5432:5432 my-postgres-db
docker ps
<winpty> docker exec -it my-postgresdb-container bash
psql -U postgres


#connect/use database
\c section2

#describe table
\d car
\d salesperson
\d transaction
\d customers



#SQL Statement

## To know the list of our customers and their spending
SELECT customer_id, sum(price) 
FROM transaction
GROUP BY customer_id


## top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month.
SELECT manufacturer, count(manufacturer) as sales_quantity, sum(price) as sales_number
FROM transaction
WHERE txn_date BETWEEN '2022-01-10' AND '2022-31-10'
group by manufacturer
ORDER BY sales_number DESC
LIMIT 3