
#!/usr/bin/python3
"""The script that holds the class State."""
from models.base_model import BaseModel


class State(BaseModel):
    """A class template \state that inherits BaseModel.

    Attributes:
        name (str): A name assigned to a State Variable.
    """

    name = ""
