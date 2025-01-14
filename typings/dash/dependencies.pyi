"""
This type stub file was generated by pyright.
"""

class _Wildcard:
    def __init__(self, name) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def to_json(self): # -> str:
        ...
    


MATCH = ...
ALL = ...
ALLSMALLER = ...
class DashDependency:
    def __init__(self, component_id, component_property) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def component_id_str(self): # -> str | Any | Unknown:
        ...
    
    def to_dict(self): # -> dict[str, str | Any | Unknown]:
        ...
    
    def __eq__(self, other) -> bool:
        """
        We use "==" to denote two deps that refer to the same prop on
        the same component. In the case of wildcard deps, this means
        the same prop on *at least one* of the same components.
        """
        ...
    
    def __hash__(self) -> int:
        ...
    
    def has_wildcard(self): # -> bool:
        """
        Return true if id contains a wildcard (MATCH, ALL, or ALLSMALLER)
        """
        ...
    


class Output(DashDependency):
    """Output of a callback."""
    allowed_wildcards = ...


class Input(DashDependency):
    """Input of callback: trigger an update when it is updated."""
    allowed_wildcards = ...


class State(DashDependency):
    """Use the value of a State in a callback but don't trigger updates."""
    allowed_wildcards = ...


class ClientsideFunction:
    def __init__(self, namespace=..., function_name=...) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


def extract_grouped_output_callback_args(args, kwargs): # -> list[Unknown]:
    ...

def extract_grouped_input_state_callback_args_from_kwargs(kwargs): # -> dict[Unknown, Unknown] | list[DashDependency]:
    ...

def extract_grouped_input_state_callback_args_from_args(args): # -> list[Unknown]:
    ...

def extract_grouped_input_state_callback_args(args, kwargs): # -> dict[Unknown, Unknown] | list[DashDependency]:
    ...

def compute_input_state_grouping_indices(input_state_grouping): # -> tuple[list[Input], list[State], list[Unknown] | dict[Unknown, Unknown] | Unknown]:
    ...

def handle_grouped_callback_args(args, kwargs): # -> tuple[Unknown | list[Unknown], list[Input], list[State], list[Unknown] | dict[Unknown, Unknown] | Unknown, Unknown]:
    """Split args into outputs, inputs and states"""
    ...

def extract_callback_args(args, kwargs, name, type_): # -> list[Unknown] | tuple[Unknown, ...]:
    """Extract arguments for callback from a name and type"""
    ...

def handle_callback_args(args, kwargs): # -> tuple[Unknown | list[Unknown] | tuple[Unknown, ...], list[Unknown] | tuple[Unknown, ...] | Unknown, list[Unknown] | tuple[Unknown, ...] | Unknown, Unknown]:
    """Split args into outputs, inputs and states"""
    ...

