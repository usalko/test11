from logging import config, getLogger

from fastapi import FastAPI

from .v1.modules import modules_router

# we create the Web API framework
app = FastAPI(
    title='Test11',
    description='Welcome to Test11\'s API documentation! Here you will able to discover all of the ways you can interact with the Test11 API.',
    root_path='/api/v1',
    docs_url=None,
    openapi_url='/docs/openapi.json',
    redoc_url='/docs',
)


for router in [modules_router]:
    app.include_router(router, prefix='/api/v1/modules')


# Setup logging

config.fileConfig('service/logging.ini')
logger1 = getLogger('name1')
logger2 = getLogger('name2')


@app.get('/')
async def root():
    return {'description': 'Fast API + Apache Airflow in Docker'}
