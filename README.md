# ヘーゼルナッツ異常検知AIアプリケーション

AI を活用したヘーゼルナッツの不良品検知 Web アプリケーションです。転移学習を用いた画像分類により、ヘーゼルナッツの良品・不良品を高精度で判定します。

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-orange.svg)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)

## 概要

このリポジトリは、[ヘーゼルナッツの不良品検知をAIアプリで実装してみた](https://qiita.com/rcky225/items/625fac2459246352834b)の実装コードを格納しています。

**最新の更新（2025年11月）：**

- TensorFlow 2.x互換のモダンなコードベースに更新
- グラスモーフィズムを採用した最先端のUI/UXデザイン
- ドラッグ&ドロップ、画像プレビューなどの機能追加

詳細な変更内容は[MODERNIZATION.md](MODERNIZATION.md)をご覧ください。

## 主な機能

- **AI 画像分類** - 転移学習による高精度な良品/不良品判定
- **ドラッグ&ドロップアップロード** - 直感的なファイルアップロード
- **画像プレビュー** - アップロード前の画像確認
- **高速処理** - 平均50-166msの処理時間
- **レスポンシブデザイン** - モバイル・タブレット対応
- **モダンUI** - グラスモーフィズムとアニメーション効果

## クイックスタート

### 必要要件

- Python 3.8以上
- pip

### インストール

1. **リポジトリのクローン**

```bash
git clone https://github.com/rcky225/hazelnut-anomaly-detection.git
cd hazelnut-anomaly-detection
```

2. **依存関係のインストール**

```bash
pip install -r requirements.txt
```

3. **アプリケーションの起動**

```bash
python hazelnut.py
```

4. **ブラウザでアクセス**

```text
http://localhost:8080
```

## 格納物

- **コード類** - Flask Webアプリケーション（Python）
- **学習済みモデル** - 転移学習による訓練済みファイル（`hazelnut_model.h5`）
- **静的ファイル** - モダンなCSS、画像アセット
- **テンプレート** - HTMLテンプレート

## 技術スタック

- **バックエンド**: Flask 2.3+
- **機械学習**: TensorFlow 2.13+, Keras
- **画像処理**: Pillow, NumPy
- **フロントエンド**: HTML5, CSS3 (グラスモーフィズム), Vanilla JavaScript
- **デプロイ**: Gunicorn, Render

## デザイン特徴

- **グラスモーフィズム** - 半透明のすりガラス効果
- **グラデーション** - 鮮やかな紫/青のカラースキーム
- **アニメーション** - スムーズなトランジションとマイクロインタラクション
- **Google Fonts** - Inter フォントファミリー
- **Bootstrap Icons** - 視覚的に魅力的なアイコン

## デプロイ

mainブランチを更新すると、自動的に[Render](https://dashboard.render.com/web/srv-cn4v9ken7f5s73940n7g/events)がデプロイを開始します。

## ライセンス

このプロジェクトはオープンソースです。

## 関連リンク

- [Qiita記事](https://qiita.com/rcky225/items/625fac2459246352834b) - 実装の詳細解説
- [最新化ドキュメント](MODERNIZATION.md) - 最新の変更内容

## 作成者

[@rcky225](https://github.com/rcky225)
