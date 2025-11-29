import os
import numpy as np
from flask import Flask, request, redirect, render_template, flash, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from PIL import Image

# TensorFlow の不要なログを抑制
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# クラスと画像サイズを定義
classes = ["不良品", "良品"]
image_size = 100

# アップロードフォルダの設定
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "your_secret_key"  # flashメッセージ用

# アップロードフォルダが存在しない場合は作成
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ファイル拡張子の確認
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# H5 フォーマットの学習済みモデルをロード
try:
    model = load_model('./model.h5', compile=False)
except Exception as e:
    raise RuntimeError(f"モデルのロードに失敗しました: {e}")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # ファイルが送信されているか確認
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        
        file = request.files['file']
        
        # ファイル名が空でないか確認
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        
        # 許可されたファイル形式の場合、保存と処理を実行
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                # 画像を読み込み、配列に変換
                img = Image.open(filepath).resize((image_size, image_size))
                img = np.array(img) / 255.0  # 正規化
                data = np.expand_dims(img, axis=0)

                # モデルで予測
                result = model.predict(data)[0]
                predicted = result.argmax()
                pred_answer = f"これは {classes[predicted]} です"

                return render_template("index.html", answer=pred_answer)

            except Exception as e:
                flash(f"画像の処理中にエラーが発生しました: {e}")
                return redirect(request.url)

    # 初回表示時は空のレスポンスを返す
    return render_template("index.html", answer="")

# エラー時のJSONレスポンス
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "内部サーバーエラー", "message": str(error)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
