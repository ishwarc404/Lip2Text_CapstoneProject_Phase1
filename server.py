from flask import Flask, request,make_response,send_file, send_from_directory
from flask_cors import CORS
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib
import os
from PIL import Image
app = Flask(__name__)
CORS(app)


app.config['UPLOAD_FOLDER'] = "inputvideos_unprocessed"

@app.route("/mediaUpload",methods=["POST"])
def mediaUpload():
    file = request.files['video']
    filename = file.filename
    video_tag = request.form["video_tag"]
    print("Video tag is:",video_tag)
    file.save(os.path.join(app.config['UPLOAD_FOLDER']+"/{}".format(video_tag), filename))
    return "200"

@app.route("/trimming")
def trimming():
    os.system("python3 trimmer.py")
    return "200"

@app.route("/splitting")
def splitting():
    os.system("python3 splitter.py")
    return "200"

@app.route("/areacalculation")
def areacalculation():
    os.system("python3 frames2area.py")
    return "200"


@app.route("/training")
def training():
    return "200"

@app.route("/prediction")
def prediction():
    return "200"


@app.route("/signature",methods=["GET","POST"])
def signature():
    dataset = request.args.get("dataset")
    dataset_path = "datasets/{}data.csv".format(dataset)
    print("Dataset quested is:",dataset)
    df = pd.read_csv(dataset_path)
    df_list = df.values.tolist()
    x_values = [i for i in range(10,91)]
    matplotlib.use('agg')
    for eachrow in df_list[:10]:
        y_values = eachrow[10:91]
        plt.plot(x_values,y_values)

    plt.savefig('Signature.jpg',dpi=150)
    #posting image to s3
    import boto3
    access_key = 'AKIA5UMB7FLMOO2HZQPL'
    secret_key = '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'
    s3 = boto3.client('s3', aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,)
    bucket = 'deltax.adpreviewtool'
    file_name = 'Signature.jpg'
    key_name = "Images/{}".format(file_name)
    
    s3.upload_file(file_name, bucket, key_name)
    return "200"

if __name__ == "__main__":
    app.run(debug=True)