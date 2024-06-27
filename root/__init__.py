from fastapi import FastAPI
from root.routes.routes import routes_users
from root.shared.database import Base, engine

Base.metadata.create_all(engine)


app = FastAPI()


app.include_router(routes_users)