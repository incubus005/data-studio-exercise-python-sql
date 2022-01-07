"""
Utility and data transformation functions
"""

import defusedxml.ElementTree as ET
import pandas as pd


def read_xml(path: str) -> pd.DataFrame:
    """
    Read xml file
    """
    root = ET.parse(path).getroot()
    df = pd.DataFrame([row.attrib for row in root])
    return df


def expand_tags(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tranform combined tags column into multiple rows with single tag per row
    """
    post_tag = df.copy().set_index('Id')
    post_tag['Tags'] = post_tag['Tags'].str.replace('><', '>|<')\
        .apply(lambda x: x.split('|') if not pd.isnull(x) else [])
    post_tag = post_tag.explode('Tags').reset_index()
    post_tag['Tags'] = post_tag['Tags'].str.strip('<>')
    post_tag = post_tag.rename(columns={'Tags': 'TagName'})
    return post_tag


def normalise_tags(post_tag: pd.DataFrame, tags: pd.DataFrame) -> pd.DataFrame:
    """
    Translate tag name to tag id
    """
    res = pd.merge(
        post_tag.loc[post_tag['TagName'].notnull(), ['Id', 'TagName']]
            .rename(columns={'Id': 'PostId'}),
        tags[['Id', 'TagName']]
            .rename(columns={'Id': 'TagId'}),
        on='TagName')
    res = res[['PostId', 'TagId']]

    return res
