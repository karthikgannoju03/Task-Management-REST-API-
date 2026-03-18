from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    status = fields.Str()
    priority = fields.Str()