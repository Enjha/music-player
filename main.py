from ast import main
from app.layouts.main_window import MainWindow
from app.layouts.player_layout import * 

def main():
    main_window = MainWindow('Spotizer')
    main_window.init_window()
    

if __name__ == "__main__":
    main()
