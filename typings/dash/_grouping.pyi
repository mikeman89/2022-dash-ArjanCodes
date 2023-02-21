"""
This type stub file was generated by pyright.
"""

from dash.exceptions import InvalidCallbackReturnValue

"""
This module contains a collection of utility function for dealing with property
groupings.

Terminology:

For the purpose of grouping and ungrouping, tuples/lists and dictionaries are considered
"composite values" and all other values are considered "scalar values".

A "grouping value" is either composite or scalar.

A "schema" is a grouping value that can be used to encode an expected grouping
structure

"""
def flatten_grouping(grouping, schema=...): # -> list[Unknown]:
    """
    Convert a grouping value to a list of scalar values

    :param grouping: grouping value to flatten
    :param schema: If provided, a grouping value representing the expected structure of
        the input grouping value. If not provided, the grouping value is its own schema.
        A schema is required in order to be able treat tuples and dicts in the input
        grouping as scalar values.

    :return: list of the scalar values in the input grouping
    """
    ...

def grouping_len(grouping): # -> int:
    """
    Get the length of a grouping. The length equal to the number of scalar values
    contained in the grouping, which is equivalent to the length of the list that would
    result from calling flatten_grouping on the grouping value.

    :param grouping: The grouping value to calculate the length of
    :return: non-negative integer
    """
    ...

def make_grouping_by_index(schema, flat_values): # -> list[Unknown] | dict[Unknown, Unknown]:
    """
    Make a grouping like the provided grouping schema, with scalar values drawn from a
    flat list by index.

    Note: Scalar values in schema are not used

    :param schema: Grouping value encoding the structure of the grouping to return
    :param flat_values: List of values with length matching the grouping_len of schema.
        Elements of flat_values will become the scalar values in the resulting grouping
    """
    ...

def map_grouping(fn, grouping): # -> list[Unknown] | AttributeDict:
    """
    Map a function over all of the scalar values of a grouping, maintaining the
    grouping structure

    :param fn: Single-argument function that accepts and returns scalar grouping values
    :param grouping: The grouping to map the function over
    :return: A new grouping with the same structure as input grouping with scalar
        values updated by the input function.
    """
    ...

def make_grouping_by_key(schema, source, default=...): # -> list[Unknown] | AttributeDict:
    """
    Create a grouping from a schema by using the schema's scalar values to look up
    items in the provided source object.

    :param schema: A grouping of potential keys in source
    :param source: Dict-like object to use to look up scalar grouping value using
        scalar grouping values as keys
    :param default: Default scalar value to use if grouping scalar key is not present
        in source
    :return: grouping
    """
    ...

class SchemaTypeValidationError(InvalidCallbackReturnValue):
    def __init__(self, value, full_schema, path, expected_type) -> None:
        ...
    
    @classmethod
    def check(cls, value, full_schema, path, expected_type): # -> None:
        ...
    


class SchemaLengthValidationError(InvalidCallbackReturnValue):
    def __init__(self, value, full_schema, path, expected_len) -> None:
        ...
    
    @classmethod
    def check(cls, value, full_schema, path, expected_len): # -> None:
        ...
    


class SchemaKeysValidationError(InvalidCallbackReturnValue):
    def __init__(self, value, full_schema, path, expected_keys) -> None:
        ...
    
    @classmethod
    def check(cls, value, full_schema, path, expected_keys): # -> None:
        ...
    


def validate_grouping(grouping, schema, full_schema=..., path=...): # -> None:
    """
    Validate that the provided grouping conforms to the provided schema.
    If not, raise a SchemaValidationError
    """
    ...

def update_args_group(g, triggered): # -> None:
    ...

