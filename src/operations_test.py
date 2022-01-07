import pandas as pd
from pandas.testing import assert_frame_equal

from operations import expand_tags, normalise_tags


def test_expanding_tags():
    expected = pd.DataFrame([{'Id': 0, 'TagName': ''},
                            {'Id': 1, 'TagName': 'a'},
                            {'Id': 2, 'TagName': 'a'},
                            {'Id': 2, 'TagName': 'b'},
                            {'Id': 2, 'TagName': 'c'}])

    actual = expand_tags(pd.DataFrame([{'Id': 0, 'Tags': ''},
                         {'Id': 1, 'Tags': '<a>'},
                         {'Id': 2, 'Tags': '<a><b><c>'}]))

    assert assert_frame_equal(expected, actual) is None


def test_normalising_tags():
    pt = pd.DataFrame([{'Id': 1, 'TagName': 'a'},
                       {'Id': 1, 'TagName': 'b'}])
    tags = pd.DataFrame([{'Id': 1, 'TagName': 'a'}])

    expected = pd.DataFrame([{'PostId': 1, 'TagId': 1}])

    actual = normalise_tags(pt, tags)

    assert assert_frame_equal(expected, actual) is None
