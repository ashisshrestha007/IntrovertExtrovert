from flask import Flask, jsonify
import kagglehub


app = Flask(__name__)

# Default route for homepage
@app.route('/')
def home():
    return '<h1>Welcome to the IntrovertExtrovert API</h1><p>Use <code>/download_model</code> to download the model.</p>'

@app.route('/download_model', methods=['GET'])
def download_model():
    try:
        # Download the latest model
        path = kagglehub.model_download("balajivaraprasad/introverts-5hl-nn/pyTorch/default")
        return jsonify({"status": "success", "model_path": path})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

