import os
import numpy as np
from flask import Flask, request, redirect, render_template, flash
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

# TensorFlow の警告レベルを設定
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# クラスラベルと画像サイズを設定
classes = ["不良品", "良品"]
image_size = 100

# アップロードフォルダと許可された拡張子を設定
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Flask アプリケーションを初期化
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 必要に応じてアップロードフォルダを作成
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ファイル拡張子を確認する関数
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 学習済みモデルをロード（SavedModel 形式）
model = load_model('./saved_model')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # ファイルが送信されていない場合
        if 'file' not in request.files:
            flash('ファイルが選択されていません')
            return redirect(request.url)
        file = request.files['file']

        # ファイル名が空の場合
        if file.filename == '':
            flash('有効なファイルが選択されていません')
            return redirect(request.url)

        # ファイルが許可された形式の場合
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                # 画像を読み込み、np.array に変換
                img = load_img(filepath, target_size=(image_size, image_size))
                img = img_to_array(img) / 255.0  # 正規化
                data = np.expand_dims(img, axis=0)

                # モデルで予測
                result = model.predict(data)[0]
                predicted = result.argmax()
                pred_answer = "これは " + classes[predicted] + " です"
            except Exception as e:
                pred_answer = f"予測中にエラーが発生しました: {e}"
            finally:
                # 処理後にアップロードされたファイルを削除
                os.remove(filepath)

            return render_template("index.html", answer=pred_answer)

        else:
            flash('許可されていないファイル形式です')
            return redirect(request.url)

    # 初期画面またはエラー後のリダイレクト
    return render_template("index.html", answer="")

if __name__ == "__main__":
    # サーバーを起動
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
