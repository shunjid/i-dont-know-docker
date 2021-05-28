from flask import jsonify


def success(data, single=True):
    """Generate success response for API.

    Args:
      data: Single instance or list of instance
      single: Set false for list of instance

    Returns:
      Response in JSON format.
    """

    response = {
        "status": "ok",
        "data": data.to_dict() if single else [datum.to_dict() for datum in data],
    }
    return jsonify(response)


def error(message="Something went wrong. Please try again.", status_code=404):
    """Generate error response for API.

    Args:
      message: Custom error message
      status_code: Status code for error response

    Returns:
      Error response in JSON format.
    """

    response = jsonify({"status": "failed", "message": message})
    response.status_code = status_code
    return response
