from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_repository():
    repo_url = request.json.get('repo_url')
    repo_dir = '/tmp/repo'
    if os.path.exists(repo_dir):
        os.system(f'rm -rf {repo_dir}')
    
    # Clone repository
    try:
        os.system(f'git clone {repo_url} {repo_dir}')
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Placeholder logic for analysis
    result = {'AI_Generated_Code_Percentage': 0, 'Human_Written_Code_Percentage': 100}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

