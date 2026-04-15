from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@app.put("/users/{user_id}")
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)




@app.post("/ping")
def create_user():
    return "pong"