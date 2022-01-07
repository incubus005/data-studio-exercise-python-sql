import sqlite3

from db import tables_set_up

connection_string = 'uncommitted/warehouse.db'


def test_sqlite3_connection():
    with sqlite3.connect(connection_string) as con:
        cursor = con.cursor()

        cursor.execute('''
        DROP TABLE IF EXISTS staging_posts
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS staging_posts (
            Id text,
            PostTypeId text,
            AcceptedAnswerId text,
            CreationDate text,
            Score text,
            ViewCount text,
            Body text,
            AnswerCount text,
            CommentCount text,
            FavouriteCount text,
            ContentLicence text
        )
        ''')

        cursor.execute(
            "INSERT INTO staging_posts VALUES ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')")

        con.commit()

        assert list(cursor.execute('SELECT * FROM staging_posts')
                    ) == [('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')]


def test_sqlite3_tables_set_up():
    tables_set_up(connection_string)

    with sqlite3.connect(connection_string) as con:
        cursor = con.cursor()

        assert list(cursor.execute('''
        select name
        from sqlite_master
        where type = 'table'
            AND name in ('staging_posts','staging_tags','staging_post_tags')
        ''')) == [('staging_posts',), ('staging_tags',), ('staging_post_tags',)]
