from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "World"}

@app.get("/About")
def about():
	return {"msg": "About msg"}

@app.get("/Contact-us")
def contact_us():
	return {"email": "abc@gmail.com", "mob" : "1234567890"}