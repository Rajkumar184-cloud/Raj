from flask import Flask, jsonify

# Flask অ্যাপ তৈরি করা
app = Flask(__name__)

# চ্যানেল এবং তাদের URL-এর ডিকশনারি
channels = {
    "Star Jalsha HD": "https://baskardo.vip/IN_JALSHAS/index.m3u8",
    "Zee Bangla HD": "https://baskardo.vip/IN_ZEBS/index.m3u8",
    "Colors Bangla HD": "https://baskardo.vip/IN_ColorsBengali/index.m3u8",
    "Jalsha Movies HD": "https://baskardo.vip/IN_JALSHAMOVIES/index.m3u8",
    "Star Plus HD": "https://baskardo.vip/IN_STS/index.m3u8",
    "Sony HD": "https://baskardo.vip/IN_STVS/index.m3u8",
    "Star Sports 1 Hindi": "https://baskardo.vip/In_Hin/index.m3u8",
}

# হোম রুট
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the TV Channel API!"})

# চ্যানেলের রুট
@app.route('/channels', methods=['GET'])
def get_channels():
    return jsonify(channels)

# অ্যাপ রান করা
if __name__ == '__main__':
    app.run(debug=True)
