from app import create_app

app = create_app()
app.title = "Team Kebab - NFT Transaction Dashboard"

server = app.server

if __name__ == "__main__":
    app.run_server()
