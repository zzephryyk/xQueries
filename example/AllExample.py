from xQueries import QueryBuilder

qb = QueryBuilder('users') #Initialize QueryBuilder with table name.

#Build query SELECT -> SELECT userId, firstName, lastName, email FROM users WHERE userId = '1'
select_query: str = qb.select('userId', 'firstName', 'lastName', 'email').where('userId', '=', 1).buildQuery()

#Build query INSERT -> INSERT INTO users (firstName, lastName, email) VALUES ('John', 'Doe', 'john@example.com')
insert_query: str = qb.insert({'firstName': 'John', 'lastName': 'Doe', 'email': 'john@example.com'})

#Build query UPDATE -> UPDATE users SET firstName = 'Jane', lastName = 'Doe' WHERE userId = '1' AND userId = '1'
update_query: str = qb.where('userId', '=', 1).update({'firstName': 'Jane', 'lastName': 'Doe'})

#Build query DELETE -> DELETE FROM users WHERE userId = '1' AND userId = '1' AND userId = '1'
delete_query: str = qb.where('userId', '=', 1).delete()

