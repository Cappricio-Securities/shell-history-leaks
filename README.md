
<div align="center">
  <img src="https://blogs.cappriciosec.com/uploaders/shell-history-leaks-tool.png" alt="logo">
</div>


## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![PyPI - Version](https://img.shields.io/pypi/v/shell-history-leaks)
![PyPI - Downloads](https://img.shields.io/pypi/dm/shell-history-leaks)
![GitHub all releases](https://img.shields.io/github/downloads/Cappricio-Securities/shell-history-leaks/total)
<a href="https://github.com/Cappricio-Securities/shell-history-leaks/releases/"><img src="https://img.shields.io/github/release/Cappricio-Securities/shell-history-leaks"></a>![Profile_view](https://komarev.com/ghpvc/?username=Cappricio-Securities&label=Profile%20views&color=0e75b6&style=flat)
[![Follow Twitter](https://img.shields.io/twitter/follow/cappricio_sec?style=social)](https://twitter.com/cappricio_sec)
<p align="center">

<p align="center">







## License

[MIT](https://choosealicense.com/licenses/mit/)



## Installation 

1. Install Python3 and pip [Instructions Here](https://www.python.org/downloads/) (If you can't figure this out, you shouldn't really be using this)

   - Install via pip
     - ```bash
          pip install shell-history-leaks 
        ```
   - Run bellow command to check
     - `shell-history-leaks -h`

## Configurations 
2. We integrated with the Telegram API to receive instant notifications for vulnerability detection.
   
   - Telegram Notification
     - ```bash
          shell-history-leaks --chatid <YourTelegramChatID>
        ```
   - Open your telegram and search for [`@CappricioSecuritiesTools_bot`](https://web.telegram.org/k/#@CappricioSecuritiesTools_bot) and click start

## Usages 
3. This tool has multiple use cases.
   
   - To Check Single URL
     - ```bash
          shell-history-leaks -u http://example.com 
        ```
   - To Check List of URL 
      - ```bash
          shell-history-leaks -i urls.txt 
        ```
   - Save output into TXT file
      - ```bash
          shell-history-leaks -i urls.txt -o out.txt
        ```
   - Want to Learn about [`shell-history-leaks`](https://blogs.cappriciosec.com/blog/179/shell-history-leaks)? Then Type Below command
      - ```bash
          shell-history-leaks -b
        ```
     
<p align="center">
  <b>🚨 Disclaimer</b>
  
</p>
<p align="center">
<b>This tool is created for security bug identification and assistance; Cappricio Securities is not liable for any illegal use. 
  Use responsibly within legal and ethical boundaries. 🔐🛡️</b></p>


## Working PoC Video

[![asciicast](https://blogs.cappriciosec.com/uploaders/Screenshot%202024-06-03%20at%204.32.40%20PM.png)](https://asciinema.org/a/XneAaRzMsYZZNpFQGHb898Qs6)




## Help menu

#### Get all items

```bash
👋 Hey Hacker
                                                                             v1.0
         __         ____      __    _      __                         __           __
   _____/ /_  ___  / / /     / /_  (_)____/ /_____  _______  __      / /__  ____ _/ /_______
  / ___/ __ \/ _ \/ / /_____/ __ \/ / ___/ __/ __ \/ ___/ / / /_____/ / _ \/ __ `/ //_/ ___/
 (__  ) / / /  __/ / /_____/ / / / (__  ) /_/ /_/ / /  / /_/ /_____/ /  __/ /_/ / ,< (__  )
/____/_/ /_/\___/_/_/     /_/ /_/_/____/\__/\____/_/   \__, /     /_/\___/\__,_/_/|_/____/
                                                      /____/                                                                                    
                                               Developed By https://cappriciosec.com

shell-history-leaks : Bug scanner for WebPentesters and Bugbounty Hunters 

$ shell-history-leaks [option]

Usage: shell-history-leaks [options]
```


| Argument | Type     | Description                | Examples |
| :-------- | :------- | :------------------------- | :------------------------- |
| `-u` | `--url` | URL to scan | shell-history-leaks -u https://target.com |
| `-i` | `--input` | filename Read input from txt  | shell-history-leaks -i target.txt | 
| `-o` | `--output` | filename Write output in txt file | shell-history-leaks -i target.txt -o output.txt |
| `-c` | `--chatid` | Creating Telegram Notification | shell-history-leaks --chatid yourid |
| `-b` | `--blog` | To Read about shell-history-leaks Bug | shell-history-leaks -b |
| `-h` | `--help` | Help Menu | shell-history-leaks -h |



## 🔗 Links
[![Website](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cappriciosec.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karthikeyan--v/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/karthithehacker)



## Author

- [@karthithehacker](https://github.com/karthi-the-hacker/)



## Feedback

If you have any feedback, please reach out to us at contact@karthithehacker.com
