from fastapi import FastAPI
import uvicorn
from subprocess import Popen, PIPE
import json

app = FastAPI()

with open('config/default.json', 'r') as f:
    data = json.load(f)


@app.get('/status')
async def status():
    return {'status': 200}  # Just for test


@app.post('/run_command')
async def run_command(command: str):
    print(command)
    p = Popen(command.split(), shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if stderr:
        return {'status': 500, 'message': stderr.decode('utf-8')}
    return {'status': 200, 'message': stdout.decode('utf-8')}


uvicorn.run(app, host=data['host'], port=data['port'])


