from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>버전 2 - Jenkins 자동 배포 테스트</h1>
    <p>야이녀석아 이 문구가 보이면 GitHub에 push한 내용이 Jenkins를 통해 자동 배포된 거야 🚀</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
