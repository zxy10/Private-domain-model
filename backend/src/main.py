import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# TODO
from src.utils.logging_config import setup_logger
# TODO
from src.routers import router
from fastapi.staticfiles import StaticFiles
# from utils.logging_config import setup_logger
'''
    整个程序的一个入口
    主要实现的是启动程序  调用日志函数记录日志  统一管理各个路由
'''
load_dotenv()   # 默认从当前工作目录下找.env 文件

app = FastAPI()
app.include_router(router)  # 创建路由模块，把多个路由统一管理
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# CORS 设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logger = setup_logger("server:main")    # 记录日志


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, workers=10, reload=True)
