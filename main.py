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

@app.get("/login")
def login_get(username : str, password : str):
	if username == "dev" and password == "123456":
	  return {"data": "This is login page", "mob" : "1234567890"}
	else :
		return {"data" : "Login failed incorrect username or password"}

@app.post("/login")
def login_post(username : str, password : str):
	if username == "dev" and password == "123456":
	  return {"data": "This is login page", "mob" : "1234567890"}
	else :
	  return {"data" : "Login failed incorrect password"}
