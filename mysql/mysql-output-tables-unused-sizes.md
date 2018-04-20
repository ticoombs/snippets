## Generates a table of the un-used space that can be gained from running "optimize" - [Optimize Table Mysql Docs](https://dev.mysql.com/doc/refman/5.7/en/optimize-table.html)

```
SELECT  table_schema, SUM(data_length + index_length + data_free)/1024/1024 AS total_mb, SUM(data_length)/1024/1024 AS data
_mb, SUM(index_length)/1024/1024 AS index_mb, SUM(data_free)/1024/1024 AS free_mb, COUNT(*) AS tables, CURDATE() AS today  FROM  i
nformation_schema.tables GROUP BY table_schema ORDER BY 5 DESC;
```
```
+---------------+--------------+--------------+-------------+--------------+--------+------------+
| table_schema  | total_mb     | data_mb      | index_mb    | free_mb      | tables | today      |
+---------------+--------------+--------------+-------------+--------------+--------+------------+
| table5        | 408.69756699 | 118.00054932 | 74.58203125 | 216.11498642 |    390 | 2018-04-20 |
| table3        | 193.18750000 |  12.48437500 |  0.70312500 | 180.00000000 |     19 | 2018-04-20 |
| table2        | 155.76910400 |  22.96760559 | 18.75390625 | 114.04759216 |    390 | 2018-04-20 |
| table1        | 185.29894257 |  40.49063492 | 38.74316406 | 106.06514359 |    401 | 2018-04-20 |

```

