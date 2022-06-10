from bot import NewsBot

def main():
    newsBot = NewsBot()
    newsBot.activate()
    newsBot.post_news()

if __name__ == "__main__":
    main()