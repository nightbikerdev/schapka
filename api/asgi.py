#! /usr/bin/env python3
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", port=8777, reload=True, access_log=False, log_level='critical')
