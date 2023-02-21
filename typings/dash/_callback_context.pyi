"""
This type stub file was generated by pyright.
"""

context_value = ...
def has_context(func): # -> (*args: Unknown, **kwargs: Unknown) -> Unknown:
    ...

class FalsyList(list):
    def __bool__(self): # -> Literal[False]:
        ...
    
    def __nonzero__(self): # -> Literal[False]:
        ...
    


falsy_triggered = ...
class CallbackContext:
    @property
    @has_context
    def inputs(self): # -> Any | dict[Any, Any]:
        ...
    
    @property
    @has_context
    def states(self): # -> Any | dict[Any, Any]:
        ...
    
    @property
    @has_context
    def triggered(self): # -> Any | FalsyList | list[Any]:
        """
        Returns a list of all the Input props that changed and caused the callback to execute. It is empty when the
        callback is called on initial load, unless an Input prop got its value from another initial callback.
        Callbacks triggered by user actions typically have one item in triggered, unless the same action changes
        two props at once or the callback has several Input props that are all modified by another callback based on
        a single user action.

        Example:  To get the id of the component that triggered the callback:
        `component_id = ctx.triggered[0]['prop_id'].split('.')[0]`

        Example:  To detect initial call, empty triggered is not really empty, it's falsy so that you can use:
        `if ctx.triggered:`
        """
        ...
    
    @property
    @has_context
    def triggered_prop_ids(self): # -> AttributeDict:
        """
        Returns a dictionary of all the Input props that changed and caused the callback to execute. It is empty when
        the callback is called on initial load, unless an Input prop got its value from another initial callback.
        Callbacks triggered by user actions typically have one item in triggered, unless the same action changes
        two props at once or the callback has several Input props that are all modified by another callback based
        on a single user action.

        triggered_prop_ids (dict):
        - keys (str) : the triggered "prop_id" composed of "component_id.component_property"
        - values (str or dict): the id of the component that triggered the callback. Will be the dict id for pattern matching callbacks

        Example - regular callback
        {"btn-1.n_clicks": "btn-1"}

        Example - pattern matching callbacks:
        {'{"index":0,"type":"filter-dropdown"}.value': {"index":0,"type":"filter-dropdown"}}

        Example usage:
        `if "btn-1.n_clicks" in ctx.triggered_prop_ids:
            do_something()`
        """
        ...
    
    @property
    @has_context
    def triggered_id(self): # -> None:
        """
        Returns the component id (str or dict) of the Input component that triggered the callback.

        Note - use `triggered_prop_ids` if you need both the component id and the prop that triggered the callback or if
        multiple Inputs triggered the callback.

        Example usage:
        `if "btn-1" == ctx.triggered_id:
            do_something()`

        """
        ...
    
    @property
    @has_context
    def args_grouping(self): # -> Any | list[Any]:
        """
        args_grouping is a dict of the inputs used with flexible callback signatures. The keys are the variable names
        and the values are dictionaries containing:
        - “id”: (string or dict) the component id. If it’s a pattern matching id, it will be a dict.
        - “id_str”: (str) for pattern matching ids, it’s the stringified dict id with no white spaces.
        - “property”: (str) The component property used in the callback.
        - “value”: the value of the component property at the time the callback was fired.
        - “triggered”: (bool)Whether this input triggered the callback.

        Example usage:
        @app.callback(
            Output("container", "children"),
            inputs=dict(btn1=Input("btn-1", "n_clicks"), btn2=Input("btn-2", "n_clicks")),
        )
        def display(btn1, btn2):
            c = ctx.args_grouping
            if c.btn1.triggered:
                return f"Button 1 clicked {btn1} times"
            elif c.btn2.triggered:
                return f"Button 2 clicked {btn2} times"
            else:
               return "No clicks yet"

        """
        ...
    
    @property
    @has_context
    def outputs_grouping(self): # -> Any | list[Any]:
        ...
    
    @property
    @has_context
    def outputs_list(self): # -> Any | list[Any]:
        ...
    
    @property
    @has_context
    def inputs_list(self): # -> Any | list[Any]:
        ...
    
    @property
    @has_context
    def states_list(self): # -> Any | list[Any]:
        ...
    
    @property
    @has_context
    def response(self): # -> Any:
        ...
    
    @staticmethod
    @has_context
    def record_timing(name, duration=..., description=...): # -> None:
        """Records timing information for a server resource.

        :param name: The name of the resource.
        :type name: string

        :param duration: The time in seconds to report. Internally, this
            is rounded to the nearest millisecond.
        :type duration: float or None

        :param description: A description of the resource.
        :type description: string or None
        """
        ...
    
    @property
    @has_context
    def using_args_grouping(self): # -> Any | list[Any]:
        """
        Return True if this callback is using dictionary or nested groupings for
        Input/State dependencies, or if Input and State dependencies are interleaved
        """
        ...
    
    @property
    @has_context
    def using_outputs_grouping(self): # -> Any | list[Any]:
        """
        Return True if this callback is using dictionary or nested groupings for
        Output dependencies.
        """
        ...
    
    @property
    @has_context
    def timing_information(self): # -> Any | dict[Any, Any]:
        ...
    


callback_context = ...
