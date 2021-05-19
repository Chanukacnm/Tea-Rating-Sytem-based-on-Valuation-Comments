import os
import shutil
import os.path
 

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer,TfidfTransformer
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from flask import Flask, session
import pandas as pd 
import pickle
import sqlite3 as sql

#from fastai.vision import *

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join('datasets','csvs')
model_path='model/model.h5'
count_vec_path='model/vec_para.pkl'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['csv','xls'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('index.html')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response    


@app.route('/', methods=['POST'])
def upload_file():

    # shutil.rmtree(UPLOAD_FOLDER)
    # os.mkdir(UPLOAD_FOLDER)
    disp_div = 'none'
    disp_div_tumor = 'none'

    d = request.form.to_dict()
    # print("dddd;",d)
    button_name = 'None'
    if (len(d)!=0):
        button_name = list(d.items())[-1][0]

    file = request.files['file']
    print("file:",file)
    if file.filename == '':
        flash('No file selected for uploading','red')
        # return redirect(request.url)
        return render_template('index.html', disp_div = disp_div)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        shutil.rmtree(UPLOAD_FOLDER)
        os.mkdir(UPLOAD_FOLDER)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        csv_file = pd.read_csv(os.path.join(UPLOAD_FOLDER, sorted(os.listdir(app.config['UPLOAD_FOLDER']))[0]))
        csv_shape = csv_file.shape

        trained_model=pickle.load(open(model_path, 'rb'))
        count_vect=pickle.load(open(count_vec_path, 'rb'))

        def vectorize_text_for_test(x_test):
            x_test_counts = count_vect.transform(x_test)
            tf_idf_transformer = TfidfTransformer(use_idf=True, smooth_idf=True, sublinear_tf=True)
            x_test_tf_idf = tf_idf_transformer.fit_transform(x_test_counts)
            return x_test_tf_idf

        X_test = csv_file["Comments1"]
        x_test = vectorize_text_for_test(X_test)
        result = trained_model.predict(x_test)

        df = pd.DataFrame(X_test)
        df["lotno"] = csv_file["lotno"]
        df["gradecode"] = csv_file["gradecode"]
        cols = list(df.columns)
        a, b, c = cols.index('Comments1'), cols.index('lotno'), cols.index('gradecode')
        cols[a], cols[b], cols[c] = cols[b], cols[c], cols[a]
        df = df[cols]
        df.insert(3, "Prediction", result, True)

        if (os.path.isfile('prediction.db')):
            conn = sql.connect('prediction.db')
            df_temp = pd.read_sql('SELECT "Comments1","lotno","gradecode","Prediction" FROM val_comments', conn)
            df_final = pd.concat([df_temp, df], ignore_index=True, sort=False)
            df_final.reset_index(drop=True)
            cursor = conn.cursor()
            cursor.execute("DROP TABLE val_comments")
            conn.commit()
            df_final.to_sql("val_comments", conn)

        else:
            conn = sql.connect('prediction.db')
            df.to_sql('val_comments', conn)

        df.style.apply(lambda x: ["background: red" if x.iloc[3]=="1" else "" for v in x], axis = 1)

        # return render_template('index.html', tables=[df.to_html(index = False,table_id="tbb")], link_column="Prediction", titles=df.columns.values, zip=zip)
        # return render_template('index.html', tables=[df.to_html(index = False,table_id="tbb")], titles=df.columns.values, zip=zip)
        return render_template('index.html', tables=list(df.values.tolist()),link_column="Comments1", link_column2="Prediction", titles=df.columns.values, zip=zip)
        # return render_template('index.html', column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)
        # return redirect('/')
    else:
        flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif', 'red')
        # return redirect(request.url)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, port=5006)

## For deploying the app use `app.run(debug=False, host="0.0.0.0", port=80)`