from fastapi import FastAPI #fastapi 라이브러리 안에 있는 FastAPI 클래스 가져오기

app = FastAPI() # FastAPI 라는 클래스를 호출해서 app이라는 객체를하나 만듬 
#app : 서버 본체, 이 app이 브라우저 요청을 받고, 응답

@app.get("/")
def read_root():
    return {"message": "Hello World"}

fake_db = {}

# 할 일 추가
@app.post("/todo")
def create_todo(todo_id: int, task: str):
    fake_db[todo_id] = task
    return {"message": "할 일이 추가 되었습니다.", "task": task}

# 할 일 조회
@app.get("/todo/{todo_id}")
def read_todo(todo_id: int):
    task = fake_db.get(todo_id)
    if task:
        return {"todo_id": todo_id, "task": task}
    else:
        return {"message" : "할 일이 없습니다"}
    
# 할 일 수정
@app.put("/todo/{todo_id}")
def update_todo(todo_id: int, new_task: str):
    if todo_id in fake_db:
        fake_db[todo_id] = new_task
        return {"message": "할 일이 수정 되었습니다", "new_task": new_task}
    else:
        return {"message": "수정 할 일이 없습니다"}

# 할 일 삭제
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id in fake_db:
        del fake_db[todo_id]
        return {"message": "할 일이 삭제 되었습니다."}
    else:
        return {"message": "삭제 할 일이 없습니다."}





# @app.get("/")
# def read_root():
#     return {"message" : "Hello FastAPI!"} 
# fastAPI는 함수에서 딕셔너리 리턴 하면 자동으로 json 형태 변환
# 딕셔너리(Dictionary)는 Key를 바로 지정하면 바로 나온다. (빠름)

# uvicorn main:app --reload