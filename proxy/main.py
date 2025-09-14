from contextlib import asynccontextmanager
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from utils.logger import setup_logger
from utils.shared import get_app_version

logger = setup_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(" --- FastProxy Initializing --- ")

    yield 

    logger.info(" --- FastProxy Shutting Down --- ")


app = FastAPI(
    debug=True,
    title="FastAPI Proxy",
    description="FastAPI powered reverse proxy",
    version=get_app_version(),
    default_response_class=ORJSONResponse,
)


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"])
async def proxy_handler(request: Request, path: str):
    """
    Entry point for all requests
    """
    target_base = "https://example.com"
    url = f"{target_base}/{path}"

    async with httpx.AsyncClient() as client:
        proxy_response = await client.request(
            method=request.method,
            url=url,
            content=await request.body(),
            headers=request.headers.raw,
        )

    return proxy_response.json()
