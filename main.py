from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from game.engine import GameEngine

def main():
    # ゲームエンジンの初期化
    engine = GameEngine(SCREEN_WIDTH, SCREEN_HEIGHT)
    engine.run()

if __name__ == "__main__":
    main()
