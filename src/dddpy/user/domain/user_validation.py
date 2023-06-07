from marshmallow import Schema, fields, validate


class CreateUserValidationSchema(Schema):
    name = fields.Str(required=True, validate=[validate.Length(
        min=1, max=100), validate.Regexp(r'^[A-Za-z]+(?:\s[A-Za-z]+)*$')])
    email = fields.Str(required=True, metadata={'max': 150})
    password = fields.Str(required=True, validate=validate.Length(min=8))


class UpdateUserValidationSchema(Schema):
    name = fields.Str(validate=[validate.Length(
        min=1, max=100), validate.Regexp(r'^[A-Za-z]+(?:\s[A-Za-z]+)*$')])
    email = fields.Str(metadata={'max': 150})
    password = fields.Str(validate=validate.Length(min=8), required=False, allow_none=True)
