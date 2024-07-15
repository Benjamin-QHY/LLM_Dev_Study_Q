from fastapi import Depends, FastAPI,Request,Form,BaseModel
from models.News import News

app = FastAPI()


# 根路径
@app.get("/")  
def root():
    return {"first_info": "Hello World"}


# 无参数的 URL
@app.get("/news/detail/6978125")
async def news_content(q: str = None):
    return {"news_id": "666666", "q": q}


# 带参数的 URL
@app.get("/news/detail/{news_id}")
def news_content(news_id: int,q: str = None):
    return {"news_id": news_id, "q": q}


# 既有默认值也有没有默认值的 URL
@app.get("/news/list")
def news_list(page: int,rows: int = 10):
    return {"page": page, "rows": rows}

# 有 Path、Query、pydantic 参数的 URL
@app.post("/news/update/{news_id}")
def create(news_id: int,news: News,q:str=None):
    return {"news_id": news_id, "news": news}


# 获取 header 中信息
@app.get("/info/header")
def header(*, request:Request):
    return {"header":dict(request.headers)}


# form 中的参数，普通方式
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}


# form 中的参数，使用 pydantic
class LoginForm(BaseModel):
    username: str
    password: str

def login_form(username: str = Form(...), password: str = Form(...)) -> LoginForm:
    return LoginForm(username=username, password=password)

@app.post("/loginForm")
def login(form_data: LoginForm = Depends(login_form)):
    return {"username": form_data.username, "password": form_data.password}