from marshmallow import Schema, fields, validate  # Import Marshmallow for schema validation.


class CreateUserValidationSchema(Schema):
    """
    Validation schema for creating a user.
    Ensures that the input data for creating a user meets the required constraints.
    """

    # Field 'name': Required, must be a string between 1 and 100 characters, and match a pattern of letters and spaces.
    name = fields.Str(required=True, validate=[validate.Length(
        min=1, max=100), validate.Regexp(r'^[A-Za-z]+(?:\s[A-Za-z]+)*$')])

    # Field 'email': Required, must be a string with a maximum length of 150 characters.
    email = fields.Str(required=True, metadata={'max': 150})

    # Field 'password': Required, must be a string with a minimum length of 8 characters.
    password = fields.Str(required=True, validate=validate.Length(min=8))


class UpdateUserValidationSchema(Schema):
    """
    Validation schema for updating a user.
    Ensures that the input data for updating a user meets the required constraints.
    """

    # Field 'name': Optional, must be a string between 1 and 100 characters, and match a pattern of letters and spaces.
    name = fields.Str(validate=[validate.Length(
        min=1, max=100), validate.Regexp(r'^[A-Za-z]+(?:\s[A-Za-z]+)*$')])

    # Field 'email': Optional, must be a string with a maximum length of 150 characters.
    email = fields.Str(metadata={'max': 150})

    # Field 'password': Optional, must be a string with a minimum length of 8 characters. Can be null or not required.
    password = fields.Str(validate=validate.Length(min=8), required=False, allow_none=True)
