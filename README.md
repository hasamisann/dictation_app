音声ファイルとテキストファイルでディクテーションの練習をするためのPythonプログラムです。
OpenAI Whisperを使用して、音声ファイルを自動でセンテンスごとに区切ってキューマーカーを挿入します。

## 環境
- WSL2 Ubuntu 22.04でしか試してないです。
- python 3.7以上

## 使い方
- このリポジトリをダウンロードして適当なところに展開してください。
- gitがない場合はインストールしてください。
```
sudo apt update
sudo apt install git
```
- ffmpegも
```
sudo apt install ffmpeg
```
- ライブラリのインストール
```
pip3 install -r requirements.txt
```
（venv等の仮想環境の使用を推奨します)

- ファイルパス指定

下記の内容のfile_path.txtをdictation_app-main直下に作成してください.指定したファイルが読み込まれます。パスは適宜変えてください。
現時点ではmp3ファイルとtxtファイルのみ対応しています。
```
audio_file=path/to/audio_file.mp3
script_file=path/to/script_file.txt
```
- 実行
```
python3 sources/main.py
```
センテンスの自動認識を行うため、新しく音声ファイルを指定した場合は起動に時間がかかります。

- 操作
``` 
D : 現在のキューを削除
I : 現在の再生地点にキューを追加
<<: 1つ前のキューに移動
|<: 現在のキューに移動
P : 再生/一時停止
>>: 次のキューに移動
L : ループ切り替え
S : キューをセーブ (./dataに保存)
```
キーボードで入力してEnterで採点します。

誤っている単語は赤文字で、不足している単語は水色の*で表示されます。
大文字と小文字は区別しません。英数字以外の記号等は無視されます。
入力が全て正解だった場合は直後の単語まで進みます。
![image](https://github.com/user-attachments/assets/97f4a40f-db69-4340-ab4e-f3497856ec76)

音声ファイルは各々で用意してください。これとか良いと思います。

https://dailydictation.com/english-listening-materials-audio-free-download
