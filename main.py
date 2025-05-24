from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/up")
def check_up():
    # Catat waktu awal
    start_time = datetime.now()
    
    # Simulasikan proses (bisa berupa operasi apa pun)
    dummy_data = {"status": "OK"}
    
    # Catat waktu akhir
    end_time = datetime.now()
    
    # Hitung waktu respons dalam milidetik (ms)
    response_time_ms = (end_time - start_time).total_seconds() * 1000
    
    # Kembalikan respons JSON
    return jsonify({
        "status": "success",
        "message": "API is up and running!",
        "response_time_ms": round(response_time_ms, 2)  # Bulatkan ke 2 desimal
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)