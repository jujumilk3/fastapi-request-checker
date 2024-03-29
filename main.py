from fastapi import FastAPI, Request, Body

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/check")
def check_get(request: Request):
    request_query_params = request.query_params
    request_headers = request.headers
    request_cookies = request.cookies
    request_client = request.client
    request_state = request.state
    request_url = request.url
    request_method = request.method
    request_body = request.body
    request_path_params = request.path_params
    request_query_params = request.query_params

    return {
        "request_query_params": request_query_params,
        "request_headers": request_headers,
        "request_cookies": request_cookies,
        "request_client": request_client,
        "request_state": request_state,
        "request_url": request_url,
        "request_method": request_method,
        "request_body": request_body,
        "request_path_params": request_path_params,
        "request_query_params": request_query_params,
    }


@app.post("/check")
def check_post(request: Request, body: dict = Body(...)):
    request_query_params = request.query_params
    request_headers = request.headers
    request_cookies = request.cookies
    request_client = request.client
    request_state = request.state
    request_url = request.url
    request_method = request.method
    request_path_params = request.path_params
    request_query_params = request.query_params
    request_body = body

    return {
        "request_query_params": request_query_params,
        "request_headers": request_headers,
        "request_cookies": request_cookies,
        "request_client": request_client,
        "request_state": request_state,
        "request_url": request_url,
        "request_method": request_method,
        "request_body": request_body,
        "request_path_params": request_path_params,
        "request_query_params": request_query_params,
    }
