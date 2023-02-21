"""
This type stub file was generated by pyright.
"""

def validate_callback(outputs, inputs, state, extra_args, types): # -> None:
    ...

def validate_callback_arg(arg): # -> None:
    ...

def validate_id_dict(arg): # -> None:
    ...

def validate_id_string(arg): # -> None:
    ...

def validate_output_spec(output, output_spec, Output): # -> None:
    """
    This validation is for security and internal debugging, not for users,
    so the messages are not intended to be clear.
    `output` comes from the callback definition, `output_spec` from the request.
    """
    ...

def validate_and_group_input_args(flat_args, arg_index_grouping): # -> tuple[list[Unknown] | list[list[Unknown] | AttributeDict | Unknown], list[Unknown] | AttributeDict | Unknown | dict[Unknown, Unknown]]:
    ...

def validate_multi_return(outputs_list, output_value, callback_id): # -> None:
    ...

def fail_callback_output(output_value, output):
    ...

def check_obsolete(kwargs): # -> None:
    ...

def validate_js_path(registered_paths, package_name, path_in_package_dist): # -> None:
    ...

def validate_index(name, checks, index): # -> None:
    ...

def validate_layout_type(value): # -> None:
    ...

def validate_layout(layout, layout_value): # -> None:
    ...

def validate_template(template): # -> None:
    ...

def check_for_duplicate_pathnames(registry): # -> None:
    ...

def validate_registry(registry): # -> None:
    ...

def validate_pages_layout(module, page): # -> None:
    ...

def validate_use_pages(config): # -> None:
    ...

def validate_module_name(module): # -> str:
    ...

def validate_long_callbacks(callback_map): # -> None:
    ...
