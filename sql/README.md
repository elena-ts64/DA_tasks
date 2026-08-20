# Задание 1: Абитуриенты
## Описание задачи
Есть таблица examination с двумя полями: id (id абитуриента), scores (кол-во набранных баллов дополнительного вступительного испытания от 0 до 100).\
Требуется реализовать запрос, который создаёт колонку с позицией абитуриента в общем рейтинге.
## Ответ
```sql
ALTER TABLE examination ADD COLUMN position_in_rating INT;

UPDATE examination e
SET position_in_rating = r.rank
FROM (
    SELECT 
        id,
        DENSE_RANK() OVER(ORDER BY scores DESC) AS rank
    FROM 
        examination
) r
WHERE e.id = r.id;
```

# Задание 2: FULL JOIN
## Описание задачи
Представьте две таблицы: первая содержит 30 строк, а вторая — 20 строк. Мы выполняем операцию FULL JOIN между ними.\
Какой диапазон возможного количества строк может быть в результирующей таблице, если учесть, что ключи для соединения могут быть как полностью совпадающими, так и абсолютно уникальными?\
*Примечание: Ответ дать в краткой форме, например: минимально 10 и максимально 3000 строк*
## Ответ
`минимально 30 и максимально 50 строк`

(максимально 600 строк при использовании FULL JOIN ... ON TRUE)

# Задание 3: Покупки
## Описание задачи
```sql
create table account
(
 id integer, -- ID счета
 client_id integer, -- ID клиента
 open_dt date, -- дата открытия счета
 close_dt date -- дата закрытия счета
)

create table transaction
(
 id integer, -- ID транзакции
 account_id integer, -- ID счета
 transaction_date date, -- дата транзакции
 amount numeric(10,2), -- сумма транзакции
 type varchar(3) -- тип транзакции
)
```

Вывести ID клиентов, которые за последний месяц по всем своим счетам совершили покупок меньше, чем на 5000 рублей.\
Без использования подзапросов и оконных функций.
## Ответ
```sql
SELECT a.client_id
FROM account a
RIGHT JOIN transaction t
ON a.id = t.account_id
WHERE t.transaction_date >= CURRENT_DATE - INTERVAL '1 month'
GROUP BY a.client_id
HAVING SUM(t.amount) < 5000;
```
