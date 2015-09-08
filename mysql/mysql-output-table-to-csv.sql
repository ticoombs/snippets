(select "Copy from mysql-column-here" ) UNION (select * from table_name INTO OUTFILE '/tmp/table_name.csv' fields enclosed by '"' terminated by ',' Escaped by '"' lines terminated by '\r\n');
