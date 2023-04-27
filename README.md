# aoai-gptdemo

## flask版

### 環境構築
venv1 という環境を作成します

Flaskの作業ディレクトリに移動

```
cd backend-flask
```

初回のみ実施
```
python3 -m venv .venv1
. .venv1/bin/activate
pip install -r requirements.txt
```

環境を切り替え（2回目以降）

```
. .venv1/bin/activate
(.venv1) @xxxxxxx ➜ /workspaces/aoai-gptdemo/backend-flask (main) $ 
```

アプリを起動します

```
export PORT=6000
flask --app run run
```

### Docker環境構築
※簡易版のため、後日修正

```
cd {project-root}
docker build --tag python-flask -f ./docker/Dockerfile-flask .
docker run -d --rm  -p 5000:6000 python-flask 
```

## Fast API版

venv2 という環境を作成します

FastAPIの作業ディレクトリに移動

```
cd backend-fastapi
```

初回のみ実施
```
python3 -m venv .venv1
. .venv2/bin/activate
pip install -r requirements.txt
```

環境を切り替え（2回目以降）

```
. .venv2/bin/activate
(.venv2) @xxxxxxx ➜ /workspaces/aoai-gptdemo/backend-fastapi (main) $ 
```

アプリを起動します

```
$ uvicorn main:app --reload --host 0.0.0.0
```

### Docker環境構築

```
cd {project-root}
docker build --tag fastapi-demo -f ./docker/Dockerfile-fastapi .
docker run -d --rm -p 3100:3100 fastapi-demo
```

## その他

### Docker停止方法

```
docker ps
docker stop {processid}
```

### nenv 終了
```
deactivate
```

## Vue環境構築

```
npm init vue@latest
```

