"""
This type stub file was generated by pyright.
"""

CONFIG = ...
def get_asset_url(path): # -> LiteralString:
    ...

def app_get_asset_url(config, path): # -> LiteralString:
    ...

def get_relative_path(path): # -> LiteralString | Literal['/']:
    """
    Return a path with `requests_pathname_prefix` prefixed before it.
    Use this function when specifying local URL paths that will work
    in environments regardless of what `requests_pathname_prefix` is.
    In some deployment environments, like Dash Enterprise,
    `requests_pathname_prefix` is set to the application name,
    e.g. `my-dash-app`.
    When working locally, `requests_pathname_prefix` might be unset and
    so a relative URL like `/page-2` can just be `/page-2`.
    However, when the app is deployed to a URL like `/my-dash-app`, then
    `app.get_relative_path('/page-2')` will return `/my-dash-app/page-2`.
    This can be used as an alternative to `get_asset_url` as well with
    `app.get_relative_path('/assets/logo.png')`

    Use this function with `app.strip_relative_path` in callbacks that
    deal with `dcc.Location` `pathname` routing.
    That is, your usage may look like:
    ```
    app.layout = html.Div([
        dcc.Location(id='url'),
        html.Div(id='content')
    ])
    @app.callback(Output('content', 'children'), [Input('url', 'pathname')])
    def display_content(path):
        page_name = app.strip_relative_path(path)
        if not page_name:  # None or ''
            return html.Div([
                dcc.Link(href=app.get_relative_path('/page-1')),
                dcc.Link(href=app.get_relative_path('/page-2')),
            ])
        elif page_name == 'page-1':
            return chapters.page_1
        if page_name == "page-2":
            return chapters.page_2
    ```
    """
    ...

def app_get_relative_path(requests_pathname, path): # -> LiteralString | Literal['/']:
    ...

def strip_relative_path(path): # -> None:
    """
    Return a path with `requests_pathname_prefix` and leading and trailing
    slashes stripped from it. Also, if None is passed in, None is returned.
    Use this function with `get_relative_path` in callbacks that deal
    with `dcc.Location` `pathname` routing.
    That is, your usage may look like:
    ```
    app.layout = html.Div([
        dcc.Location(id='url'),
        html.Div(id='content')
    ])
    @app.callback(Output('content', 'children'), [Input('url', 'pathname')])
    def display_content(path):
        page_name = app.strip_relative_path(path)
        if not page_name:  # None or ''
            return html.Div([
                dcc.Link(href=app.get_relative_path('/page-1')),
                dcc.Link(href=app.get_relative_path('/page-2')),
            ])
        elif page_name == 'page-1':
            return chapters.page_1
        if page_name == "page-2":
            return chapters.page_2
    ```
    Note that `chapters.page_1` will be served if the user visits `/page-1`
    _or_ `/page-1/` since `strip_relative_path` removes the trailing slash.

    Also note that `strip_relative_path` is compatible with
    `get_relative_path` in environments where `requests_pathname_prefix` set.
    In some deployment environments, like Dash Enterprise,
    `requests_pathname_prefix` is set to the application name, e.g. `my-dash-app`.
    When working locally, `requests_pathname_prefix` might be unset and
    so a relative URL like `/page-2` can just be `/page-2`.
    However, when the app is deployed to a URL like `/my-dash-app`, then
    `app.get_relative_path('/page-2')` will return `/my-dash-app/page-2`

    The `pathname` property of `dcc.Location` will return '`/my-dash-app/page-2`'
    to the callback.
    In this case, `app.strip_relative_path('/my-dash-app/page-2')`
    will return `'page-2'`

    For nested URLs, slashes are still included:
    `app.strip_relative_path('/page-1/sub-page-1/')` will return
    `page-1/sub-page-1`
    ```
    """
    ...

def app_strip_relative_path(requests_pathname, path): # -> None:
    ...
