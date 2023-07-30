import sys
import os
import time

class AsciiArt:
    def print_banner(self):
        banner = r"""
 __    __    ___  ____        _____   ___  ____  __ __    ___  ____        ___     __  __ __  __  _   ___   _____
|  |__|  |  /  _]|    \      / ___/  /  _]|    \|  |  |  /  _]|    \      /   \   /  ]|  |  ||  |/ ] /   \ / ___/
|  |  |  | /  [_ |  o  )    (   \_  /  [_ |  D  )  |  | /  [_ |  D  )    |     | /  / |  |  ||  ' / |     (   \_ 
|  |  |  ||    _]|     |     \__  ||    _]|    /|  |  ||    _]|    /     |  O  |/  /  |  _  ||    \ |  O  |\__  |
|  `  '  ||   [_ |  O  |     /  \ ||   [_ |    \|  :  ||   [_ |    \     |     /   \_ |  |  ||     ||     |/  \ |
 \      / |     ||     |     \    ||     ||  .  \\   / |     ||  .  \    |     \     ||  |  ||  .  ||     |\    |
  \_/\_/  |_____||_____|      \___||_____||__|\_| \_/  |_____||__|\_|     \___/ \____||__|__||__|\_| \___/  \___|
        """
        print(banner)

    def print_response(self, response):
        print(response)

    def move_mouse_to_center(self):
        screen_width, screen_height = pyautogui.size()
        target_x = screen_width // 2
        target_y = screen_height // 2
        pyautogui.moveTo(target_x, target_y, duration=1)

    def install_package(self, package_name):
        try:
            importlib.import_module(package_name)
        except ImportError:
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

    def ask_question(self, question, response):
        user_response = input(f"{question} (yes/no)?: ").lower()
        if user_response in ['yes', 'y']:
            self.print_response(response)
            return True
        elif user_response in ['no', 'n']:
            print("Please ensure you fulfill the requirements before running the program.")
            sys.exit()
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")
            return False

if __name__ == "__main__":
    ascii_art = AsciiArt()
    ascii_art.print_banner()

    questions_responses = [
        ("The web-server is already running on your system", 
         r"""
U _____ u 
\| ___"|/ 
 |  _|"   
 | |___   
 |_____|  
 <<   >>  
(__) (__)
"""),
        ("Do you have a Linux distribution on your local machine for successful installation",
         r"""
   ____   
U | __")u 
 \|  _ \/ 
  | |_) | 
  |____/  
 _|| \\_  
(__) (__)   
"""),
        ("Ensure that your web server serves /var/www/html",
         r"""
    _      
U  /"\  u  
 \/ _ \/   
 / ___ \   
/_/   \_\  
 \\    >>  
(__)  (__)
"""),
        ("Extract ochkos into /var/www/html",
         r"""
   _      
  |"|     
U | | u   
 \| |/__  
  |_____| 
  //  \\  
 (_")("_)
"""),
        ("Point your browser to http://[ip-of-webserver]/ochkosweb",
         r"""
    _      
U  /"\  u  
 \/ _ \/   
 / ___ \   
/_/   \_\  
 \\    >>  
(__)  (__)

""")
    ]

    if all(ascii_art.ask_question(q, r) for q, r in questions_responses):
        print("Muslim ti ebala :D")
