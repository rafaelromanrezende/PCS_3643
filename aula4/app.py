from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from controller import filme_controller, sala_controller, sessao_controller, tipo_ingresso_controller
from model.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cinema API", description="Sistema de venda de ingressos - PCS3643")

app.include_router(filme_controller.router)
app.include_router(sala_controller.router)
app.include_router(sessao_controller.router)
app.include_router(tipo_ingresso_controller.router)

# --- interface web -------------------------------------------------------
# A interface e' 100% estatica: o HTML/JS em static/ consome os mesmos
# endpoints REST acima via fetch(). Nenhum template le' o banco direto.
ESTATICOS = Path(__file__).parent / "static"

app.mount("/static", StaticFiles(directory=ESTATICOS), name="static")


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(ESTATICOS / "index.html")
