class Settings:
    def __init__(self, default_screen_width, default_screen_height, path_file_name):
        self.default_screen_width = default_screen_width
        self.default_screen_height = default_screen_height
        self.audio_file_path, self.script_file_path = read_paths(path_file_name)

@staticmethod
def read_paths(path_file_name):
    paths = {}
    try:
        with open(path_file_name, 'r') as f:
            for line in f:
                line = line.strip()
                if line and '=' in line:
                      key, value = line.split('=', 1)
                      paths[key.strip()] = value.strip()

        if "audio_file" not in paths or "script_file" not in paths:
                raise KeyError("必要なキー 'audio_file' または 'script_file' が file_paths.txt にありません。")

    except FileNotFoundError:
        print(f"Error: {path_file_name} が見つかりません。")
        raise
    except KeyError as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"Error: ファイルの読み込み中にエラーが発生しました: {e}")
        raise
    
    return paths["audio_file"], paths["script_file"]