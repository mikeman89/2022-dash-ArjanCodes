"""
This type stub file was generated by pyright.
"""

import abc

MutableSequence = ...
rd = ...
class ComponentRegistry:
    """Holds a registry of the namespaces used by components."""
    registry = ...
    children_props = ...
    @classmethod
    def get_resources(cls, resource_name): # -> list[Unknown]:
        ...
    


class ComponentMeta(abc.ABCMeta):
    def __new__(mcs, name, bases, attributes): # -> Self@ComponentMeta:
        ...
    


def is_number(s): # -> bool:
    ...

class Component(metaclass=ComponentMeta):
    _children_props = ...
    _base_nodes = ...
    class _UNDEFINED:
        def __repr__(self): # -> Literal['undefined']:
            ...
        
        def __str__(self) -> str:
            ...
        
    
    
    UNDEFINED = ...
    class _REQUIRED:
        def __repr__(self): # -> Literal['required']:
            ...
        
        def __str__(self) -> str:
            ...
        
    
    
    REQUIRED = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def to_plotly_json(self): # -> dict[str, dict[Unknown, Any] | Unknown]:
        ...
    
    def __getitem__(self, id):
        """Recursively find the element with the given ID through the tree of
        children."""
        ...
    
    def __setitem__(self, id, item):
        """Set an element by its ID."""
        ...
    
    def __delitem__(self, id):
        """Delete items by ID in the tree of children."""
        ...
    
    def __iter__(self): # -> Generator[Unknown, None, None]:
        """Yield IDs in the tree of children."""
        ...
    
    def __len__(self): # -> int:
        """Return the number of items in the tree."""
        ...
    
    def __repr__(self): # -> str:
        ...
    

