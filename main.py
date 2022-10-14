from ast import main
from app.layouts.player_layout import * 
from app.test.test_library import MyTestCase

def main():
    MyTestCase()
    Player.main_window()
    

if __name__ == "__main__":
    main()
