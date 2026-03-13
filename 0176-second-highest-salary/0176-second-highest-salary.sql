# Write your MySQL query statement below
select (select distinct salary from (select salary, dense_rank() over (order by salary desc) as rank_s from employee) e where rank_s=2) as SecondHighestSalary;