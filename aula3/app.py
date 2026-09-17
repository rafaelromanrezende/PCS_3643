from fastapi import FastAPI

from controller import filme_controller, sala_controller, sessao_controller, tipo_ingresso_controller
from model.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cinema API", description="Sistema de venda de ingressos - PCS3643")

app.include_router(filme_controller.router)
app.include_router(sala_controller.router)
app.include_router(sessao_controller.router)
app.include_router(tipo_ingresso_controller.router)
