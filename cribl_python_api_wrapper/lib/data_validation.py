def validate_payload(payload_data, all_fields, required_fields):
    missing_required_fields = []
    incorrectly_formatted_fields = []

    keys_to_delete = []
    for key in payload_data.keys():
        if key not in all_fields.keys():
            keys_to_delete.append(key)
        else:
            field_type = all_fields[key]
            if not isinstance(payload_data[key], field_type):
                incorrectly_formatted_fields.append(key)

    # delete keys that are passed but not defined in the above dict
    for key in keys_to_delete:
        del payload_data[key]

    for field in required_fields:
        if field not in payload_data.keys():
            missing_required_fields.append(field)

    return payload_data, missing_required_fields, incorrectly_formatted_fields
