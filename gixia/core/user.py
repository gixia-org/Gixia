from dataclasses import dataclass, fields


@dataclass
class User:
    """
    Entity class for User
    """

    email: str
    name: str
    google_info: dict

    @classmethod
    def from_document(cls, document: dict):
        """
        Convert a MongoDB document to a User object.
        """
        # Keep only data fields
        field_names = [field.name for field in fields(cls)]
        data = {key: document[key] for key in field_names}
        return cls(**data)