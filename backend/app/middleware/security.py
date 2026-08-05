from fastapi import Request
from fastapi.responses import JSONResponse


async def rate_limit_middleware(request: Request, call_next):
    """Minimal middleware placeholder for rate-limiting and request safety policies."""
    if request.url.path.startswith('/api/v1/auth'):
        return await call_next(request)
    return await call_next(request)


async def prompt_guard_middleware(request: Request, call_next):
    """Prompt guard placeholder for unsafe content or policy enforcement."""
    return await call_next(request)
