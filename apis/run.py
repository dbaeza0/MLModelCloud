from apis.inference.online.api import OnlineInference
from uvicorn.main import run


if __name__ == '__main__':
    api = OnlineInference.instantiate_api()
    run(api.app, host="0.0.0.0", port=8000)
