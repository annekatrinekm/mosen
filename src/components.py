from dash import dcc, html
def get_upload(id: str, path: str):
    return dcc.Input(
        id = id,
        placeholder = path,
        type="text",
        minLength=1
    )