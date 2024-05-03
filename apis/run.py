from apis.inference.online.api import OnlineInference
from uvicorn.main import run


if __name__ == '__main__':
    # Add routes to your FastAPI app
    api = OnlineInference()
    api.app.add_api_route("/health_check", api.health_check, methods=["GET"])
    api.app.add_api_route('/favicon.ico', api.favicon, methods=["GET"], include_in_schema=False)
    run(api.app, host="0.0.0.0", port=8000)
