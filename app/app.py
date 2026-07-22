from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    namespace = os.environ.get("POD_NAMESPACE", "non défini")
    version = os.environ.get("APP_VERSION", "v1")

    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Aminata Lo Fall - GitOps Platform</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Segoe UI', system-ui, sans-serif;
                background: linear-gradient(135deg, #1e3a5f 0%, #4a2f6b 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }}
            .card {{
                background: rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 20px;
                padding: 50px 60px;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }}
            .badge {{
                display: inline-block;
                background: rgba(255,255,255,0.15);
                padding: 6px 16px;
                border-radius: 20px;
                font-size: 13px;
                letter-spacing: 1px;
                margin-bottom: 20px;
                text-transform: uppercase;
            }}
            h1 {{
                font-size: 42px;
                margin-bottom: 10px;
                background: linear-gradient(90deg, #ffffff, #c9d6ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            p.subtitle {{
                opacity: 0.7;
                margin-bottom: 30px;
                font-size: 15px;
            }}
            .info {{
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
            }}
            .info-item {{
                background: rgba(0,0,0,0.2);
                padding: 12px 20px;
                border-radius: 10px;
                font-size: 13px;
            }}
            .info-item span {{
                display: block;
                opacity: 0.5;
                font-size: 11px;
                text-transform: uppercase;
                margin-bottom: 4px;
            }}
            .status {{
                margin-top: 25px;
                font-size: 13px;
                color: #6dffb0;
            }}
            .status::before {{
                content: "●";
                margin-right: 6px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="badge">GitOps Platform</div>
            <h1>Aminata Lo Fall</h1>
            <p class="subtitle">Plateforme observable déployée sur Kubernetes</p>
            <div class="info">
                <div class="info-item"><span>Hostname</span>{hostname}</div>
                <div class="info-item"><span>Namespace</span>{namespace}</div>
                <div class="info-item"><span>Version</span>{version}</div>
            </div>
            <div class="status">Application en ligne</div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)