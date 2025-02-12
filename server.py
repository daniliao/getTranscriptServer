from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['GET'])
def get_transcript():
    # hard code video id for testing, use below code instead of request
    # video_id = "eKJmPC_T0dw"
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({'error': 'No video_id provided'}), 400
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify({'transcript': transcript})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
