from flask import Flask, render_template, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# ── Almacenamiento simulado (memoria) ──────────────────────────
puntos = []

# ── Vista principal ────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html')

# ── API: guardar punto ─────────────────────────────────────────
@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    data = request.get_json(silent=True)

    if not data or 'lat' not in data or 'lng' not in data:
        return jsonify({ 'success': False, 'message': 'Faltan lat o lng' }), 400

    punto = {
        'id': str(uuid.uuid4())[:8],
        'lat': data['lat'],
        'lng': data['lng'],
        'guardado_en': datetime.now().isoformat()
    }
    puntos.append(punto)

    print(f"  Punto guardado → {punto}")

    return jsonify({ 'success': True, 'punto': punto }), 201

# ── (opcional) ver todos los puntos desde la terminal ─────────
@app.route('/puntos')
def ver_puntos():
    return jsonify(puntos)

if __name__ == '__main__':
    app.run(debug=True)