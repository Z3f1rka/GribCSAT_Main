from fastapi import FastAPI
import uvicorn
import psycopg2

app = FastAPI()


def connection():
    return psycopg2.connect("dbname=db user=postgres password=postgres")


@app.get("/")
async def root():
    return {"message": "Hello World"}


# example how to connect to db and get sth
@app.get('/get_users')
async def get_users():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('select * from users')
    return cursor.fetchall()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
