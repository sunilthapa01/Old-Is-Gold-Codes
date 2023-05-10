 #Source:https://bit.ly/3pfYSJ6
import requests
from bs4 import BeautifulSoup
def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text
if __name__ == "__main__":
    print("Daily Horoscope. \n")
    print(
        "Input your Zodiac sign number:\n",
        "1. Aries\n",
        "2. Taurus\n",
        "3. Gemini\n",
        "4. Cancer\n",
        "5. Leo\n",
        "6. Virgo\n",
        "7. Libra\n",
        "8. Scorpio\n",
        "9. Sagittarius\n",
        "10. Capricorn\n",
        "11. Aquarius\n",
        "12. Pisces\n",
    )11
    zodiac_sign = int(input("Input a number from said list: ").strip())
    print("Choose some day:\n", "yesterday\n", "today\n", "tomorrow\n")
    day = input("Input the day from said list: ")
    horoscope_text = horoscope(zodiac_sign, day)
    print(horoscope_text)
    