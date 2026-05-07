from fastapi import FastAPI, HTTPException, status
from sqlmodel import select

from db import SessionDep, create_all_tables
from model import Dog, DogCreate, DogUpdate

app = FastAPI(
    title="Parcial FastAPI",
    version="1.0.0"
)


@app.on_event("startup")
def on_startup():
    create_all_tables()


@app.get("/")
def root():
    return {
        "message": "Servidor funcionando correctamente"
    }



@app.get("/dogs", response_model=list[Dog])
def get_dogs(session: SessionDep):
    statement = select(Dog)
    dogs = session.exec(statement).all()
    return dogs


@app.get("/dogs/{dog_id}", response_model=Dog)
def get_dog(dog_id: int, session: SessionDep):
    dog = session.get(Dog, dog_id)

    if not dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perro no encontrado"
        )

    return dog


@app.post(
    "/dogs",
    response_model=Dog,
    status_code=status.HTTP_201_CREATED
)
def create_dog(data: DogCreate, session: SessionDep):
    new_dog = Dog.model_validate(data)

    session.add(new_dog)
    session.commit()
    session.refresh(new_dog)

    return new_dog

@app.put("/dogs/{dog_id}", response_model=Dog)
def update_dog(
    dog_id: int,
    data: DogUpdate,
    session: SessionDep
):
    dog = session.get(Dog, dog_id)

    if not dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perro no encontrado"
        )

    dog_data = data.model_dump(exclude_unset=True)

    for key, value in dog_data.items():
            setattr(dog, key, value)

    session.add(dog)
    session.commit()
    session.refresh(dog)

    return dog


@app.delete("/dogs/{dog_id}")
def delete_dog(dog_id: int, session: SessionDep):
    dog = session.get(Dog, dog_id)

    if not dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perro no encontrado"
        )

    session.delete(dog)
    session.commit()

    return {
        "message": "Perro eliminado correctamente"
    }
