

app = Flask(__name__)

def colorize_image(image_path):
    # Your colorization code here...
    # ...
    return colorized_image


@app.route('/upload', methods=['POST'])
def upload_file():