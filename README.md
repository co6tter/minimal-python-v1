# Python基礎学習リポジトリ

## Overview

Python の基本文法と標準ライブラリを学習するためのサンプルコード集です。変数、制御構文、関数、データ構造、クラス、ファイル操作など、Python プログラミングの基礎を段階的に学べるように構成されています。

## Tech Stack

- Python 3.12
- Dev Containers (VS Code)

## Setup

このプロジェクトは Dev Container を使用して開発環境を構築できます。

1. VS Code で本リポジトリを開く
2. Dev Container 拡張機能がインストールされていることを確認
3. コマンドパレット（`Cmd+Shift+P` / `Ctrl+Shift+P`）から「Dev Containers: Reopen in Container」を実行
4. コンテナのビルドが完了するまで待機

または、ローカル環境で Python 3.12 以上をインストールして実行することも可能です。

## Usage

各 Python ファイルを個別に実行して学習できます：

- **main01.py**: 文字列操作、入力処理、条件分岐（match文）、ループ、例外処理の基本
- **main02.py**: 関数の定義、引数（位置引数、キーワード引数、デフォルト引数）、lambda式
- **main03.py**: データ構造（リスト、タプル、辞書、集合）の操作と活用
- **main04.py**: 標準ライブラリ（random、math、datetime、calendar、os、collections、copy）とファイル入出力
- **main05.py**: オブジェクト指向プログラミング（クラス、継承、プロパティ、クラスメソッド、staticmethod）

実行例：
```bash
python main01.py
python main02.py
python main03.py
python main04.py
python main05.py
```

## Directory Structure

```
.
├── main01.py          # 基本文法（文字列、制御構文、例外処理）
├── main02.py          # 関数
├── main03.py          # データ構造
├── main04.py          # 標準ライブラリとファイル操作
├── main05.py          # クラスとオブジェクト指向
├── names.txt          # main04.py で使用するサンプルデータ
├── .devcontainer/     # Dev Container 設定
└── README.md          # 本ファイル
```

## License

This repository is for personal/private use only.
