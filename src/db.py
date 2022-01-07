import sqlite3

connection_string = 'uncommitted/warehouse.db'


def tables_set_up(connection_string: str) -> bool:

    with sqlite3.connect(connection_string) as con:

        cursor = con.cursor()

        cursor.execute('''
        DROP TABLE IF EXISTS staging_post_tags
        ''')

        cursor.execute('''
        DROP TABLE IF EXISTS staging_posts
        ''')

        cursor.execute('''
        DROP TABLE IF EXISTS staging_tags
        ''')

        con.commit()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS staging_posts (
            Id int PRIMARY KEY,
            PostTypeId int,
            AcceptedAnswerId int,
            CreationDate datetime,
            Score int,
            ViewCount int,
            Body text,
            OwnerUserId int,
            LastEditorUserId int,
            LastEditDate datetime,
            LastActivityDate datetime,
            Title text,
            Tags text,
            AnswerCount int,
            CommentCount int,
            FavoriteCount int,
            ContentLicense text,
            ParentId int,
            ClosedDate datetime,
            CommunityOwnedDate datetime,
            LastEditorDisplayName text,
            OwnerDisplayName text
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS staging_tags (
            Id int PRIMARY KEY,
            TagName text,
            Count int,
            ExcerptPostId int,
            WikiPostId int
        )
        ''')
        con.commit()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS staging_post_tags (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            PostId int,
            TagId int,
            FOREIGN KEY(PostId) REFERENCES staging_posts(Id),
            FOREIGN KEY(TagId) REFERENCES staging_tags(Id)

        )
        ''')
        con.commit()
    return True
