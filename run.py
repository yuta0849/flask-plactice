from .app import app

if __name__ == "__main__":
    app.debug = True  # デバッグモードをオンにする
    app.run(debug=True, host="0.0.0.0")