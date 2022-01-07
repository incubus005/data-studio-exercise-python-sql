'Entrypoint to populate the database'

import sqlite3

from db import tables_set_up
from operations import expand_tags, normalise_tags, read_xml

posts_path = 'uncommitted/Posts.xml'
tags_path = 'uncommitted/Tags.xml'
connection_string = 'uncommitted/warehouse.db'


def main():
    posts = read_xml(posts_path)
    tags = read_xml(tags_path)

    post_tag = expand_tags(posts[['Id', 'Tags']])
    post_tag_ids = normalise_tags(post_tag, tags)

    if tables_set_up(connection_string):

        with sqlite3.connect(connection_string) as con:
            posts.to_sql('staging_posts', if_exists='append', con=con, index=False)
            tags.to_sql('staging_tags', if_exists='append', con=con, index=False)
            post_tag_ids.to_sql('staging_post_tags',
                                if_exists='append', con=con, index=False)


if __name__ == '__main__':
    main()
