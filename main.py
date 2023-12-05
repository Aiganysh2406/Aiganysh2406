# ORM - технология позволяющая автоматически связать бд с кодом

# psycopg2 - Это библиотекаб которая предоставляет интерфейс Python для взаимодействия с Postgresql

# import psycopg2
# 
# db_params = {
    # 'host':'localhost',
    # 'database':'practice_psyco',
    # 'user': 'hello',
    # 'password':'1'
# }
# connection = psycopg2.connect(**db_params)
#  
# create_table = """
# CREATE TABLE test(
# id serial primary key,
# name varchar(30),
# age integer
# );
# """

data = ('Nikita', 20)
insert_query = """
insert into (name, age) values {data};

insert_query = """
insert into (name, age) values {%s, %s};
"""
select_query = """
select * from test;

# написать 
update_query = """
update test
set name = 'Tima' where id = 1
"""
# написать DELETE запросб который динамично удаляеть юзеров по id
delete_query = f """
delete frojm test
where id = {del_id} """


"""
try: 
    cursor = connection.cursor()
    cursor.execute # запись одной информации
    cursor.executemany (insert_querty, data)) #  выполнение sql запроса
    # connection.commit()
    results = cursor.fetchall()
    print(results)

finally:
    cursor.close()
    connection.close(
    """

# peewee
# sqlalchemy


