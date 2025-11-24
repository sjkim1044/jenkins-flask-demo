from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Jenkins + GitHub + Docker + Flask</h1>
    <p>이 페이지가 보이면 CI/CD가 잘 동작한 거야 😎</p>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    # 도커 컨테이너에서 외부 접속 가능하게 0.0.0.0 사용
    app.run(host="0.0.0.0", port=5000, debug=False)
