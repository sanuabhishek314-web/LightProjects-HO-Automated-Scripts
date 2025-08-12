from flask import Flask, request, jsonify
import os
import uuid
import json
from datetime import datetime

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DATA_FILE'] = 'dummy_data.json'

# Create folders if they don’t exist
for folder in ['aadhar', 'pan', 'voter', 'selfies']:
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], folder), exist_ok=True)

# Load existing data

def load_data():
    if not os.path.exists(app.config['DATA_FILE']):
        return []
    with open(app.config['DATA_FILE'], 'r') as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(app.config['DATA_FILE'], 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/upload_kyc', methods=['POST'])
def upload_kyc():
    kyc_id = str(uuid.uuid4())
    data = {
        'kyc_id': kyc_id,
        'timestamp': datetime.now().isoformat(),
        'mobile': request.form.get('mobile'),
        'otp': request.form.get('otp'),
    }

    # Upload & Save all documents
    def save_file(file_key, folder):
        file = request.files.get(file_key)
        if file:
            filename = f"{kyc_id}_{file_key}.jpg"
            path = os.path.join(app.config['UPLOAD_FOLDER'], folder, filename)
            file.save(path)
            return path
        return None

    data['documents'] = {
        'aadhar_front': save_file('aadhar_front', 'aadhar'),
        'aadhar_back': save_file('aadhar_back', 'aadhar'),
        'pan_front': save_file('pan_front', 'pan'),
        'pan_back': save_file('pan_back', 'pan'),
        'voter_front': save_file('voter_front', 'voter'),
        'voter_back': save_file('voter_back', 'voter'),
        'selfie': save_file('selfie', 'selfies')
    }

    all_data = load_data()
    all_data.append(data)
    save_data(all_data)

    return jsonify({'status': 'success', 'kyc_id': kyc_id}), 201

@app.route('/get_dummy_kyc', methods=['GET'])
def get_dummy_kyc():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
