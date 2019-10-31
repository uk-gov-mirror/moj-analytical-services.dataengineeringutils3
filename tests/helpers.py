from unittest.mock import Mock


def get_object_attrs(obj):
    return [attr_name for attr_name in dir(obj)]


def mock_object(cls, *args, **kwargs):
    obj = cls(*args, **kwargs)
    mock_obj = Mock()
    for attr_name in get_object_attrs(obj):
        try:
            getattr(mock_obj, attr_name).side_effect = getattr(obj, attr_name)
        except AttributeError:
            pass
    return mock_obj
