# Rename table prefix
 select concat ('alter table ', table_name, ' RENAME ', replace(table_name, 'fromValue', 'toValue') ) 
 from information_schema.tables 
 where table_name like 'fromValue%' 
 and table_schema = 'database_name';
