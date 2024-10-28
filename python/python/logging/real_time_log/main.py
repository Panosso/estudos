from fastapi import FastAPI
import logging

#Get log file and can be use in the application
logger_debug = logging.getLogger('uvicorn.error')
logger_info = logging.getLogger('uvicorn.info')

app = FastAPI()

@app.get('/')
async def hello():
    logger_debug.debug('Started DEBUG file at hello function')
    logger_info.info('Started Log at hello function')
    return {"Mensaage" : "Hello, World"}