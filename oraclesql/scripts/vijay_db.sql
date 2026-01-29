select * from books;
select sysdate from dual;

select to_char(sysdate,'DDth-Month-YYYY HH:mi:ss ') formatted_date
from dual;

select to_char(12345.67, '99,999,99') from dual;

select to_number('100') + 400 total
from dual;

select '100' + 400 total
from dual;