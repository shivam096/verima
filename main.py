from models import UAJob
from verima.tasks import get_token


def main(request):
    """API Gateway

    Args:
        request (flask.Request): HTTP request

    Raises:
        NotImplementedError: No module found

    Returns:
        dict: HTTP Response
    """

    data = request.get_json()
    print(data)

    if "view_id" in data and "broadcast" not in data:
        response = UAJob(
            headers=get_token(),
            view_id=data["view_id"],
            start=data.get("start"),
            end=data.get("end"),
        ).run()
    else:
        raise NotImplementedError(data)

    print(response)
    return response
