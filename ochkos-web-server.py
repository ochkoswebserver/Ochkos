import sys
import os
import time
import pyautogui
import math

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
        # Circular mouse movement
        while True:  # Infinite loop for continuous circular motion
            R = 400
            (x, y) = pyautogui.size()
            (X, Y) = pyautogui.position(x // 2, y // 2)
            
            for i in range(360):
                if i % 6 == 0:
                    pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))
                    time.sleep(0.05)  # Optional: Add a small delay between 

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
        ascii_art.move_mouse_to_center()
