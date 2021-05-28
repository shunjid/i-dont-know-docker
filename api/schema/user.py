from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    firstName = fields.Str(
        required=True,
        error_messages={"required": "First name is required"},
    )
    lastName = fields.Str(
        required=True,
        error_messages={"required": "Last name is required"},
    )
    emailAddress = fields.Email(
        required=True,
        error_messages={"required": "Email address is required"},
    )
    mobileNumber = fields.Str(
        required=True,
        validate=validate.And(
            validate.Regexp(
                regex="^(?:\+?88)?01[13-9]\d{8}$",
                error="Invalid Bangladeshi Mobile Number",
            )
        ),
        error_messages={"required": "Mobile number is required"},
    )
