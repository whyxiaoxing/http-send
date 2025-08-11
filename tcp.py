import json
import  uvicorn
import fastapi

FAST初始化 = fastapi.FastAPI()



#json文件的读取与dumps的格式化
def Json_answer(need_name):
    try:
        with open("date.json", "r", encoding="utf-8") as f:
            date = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("检查date.json是否存在")
        return "date.json 文件不存在或格式错误"

    try:
        with open("name.dat", "r", encoding="utf-8") as f:
            valid_names = {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        print("检查name.dat是否存在")
    if need_name in valid_names:
        DateMain =date.get(need_name, {})
        DateMain_geshi = json.dumps(DateMain, indent=4, ensure_ascii=False)
        return DateMain_geshi
    else:
        need_names="errors"
        DateMaine = date.get(need_names, {})
        DateMain_geshie = json.dumps(DateMaine, indent=4, ensure_ascii=False)
        return DateMain_geshie

@FAST初始化.post("/send")
async def 接收信息(请求:fastapi.Request):
    客户端发送的信息= await 请求.body()
    if 客户端发送的信息 == None:
        return "发送信息为空，请重新发送"
    格式化客户端数据=客户端发送的信息.decode()
    读取Json文件=Json_answer(格式化客户端数据)
    return 读取Json文件
    


if __name__ == "__main__":
  uvicorn.run(FAST初始化,host="127.0.0.1",port=8000)


# the writer country is China  ,so "print"or "#" follow if Chinese， please translation 。

