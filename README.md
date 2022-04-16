# GRMDS-NFT-Competition
This repository contains all data processes + submissions of team Kebab to the [RMDS Lab's quarterly competition](https://grmds.org/comp/nft), specifically NFT dashboard making during 1st quarter of 2022.

### Description
The dashboard analyzes NFT Transactions during the 1st Quarter of 2022, starting from analyzing how popularity and sales impact the price of NFTs, comparing the distribution of cryptocurrency used on NFT Transactions, to describing Top 10 NFTs based on certain attributes. 

### Members
- [Kevin Bennett Haryono](https://github.com/kevinbennetth)
- [Matthew Adrianus Mulyono](https://github.com/Matthew1906)
- [Michael The Hadinata](https://github.com/blitzen23)
- [Ryne Ferdinand](https://github.com/RyneFerdinand)

### Table of Contents
|Name|Details|
|----|-------|
|[app](/app)|Contains the Dashboard structure made with [MVC Architectural pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) using [Dash Python](https://dash.plotly.com/) as the Backend Framework and [Tailwind CSS](https://tailwindcss.com/) as the Frontend Framework|
|[assets](/app/assets)|Contains necessary styles for the [dashboard](https://nft-transaction-dashboard.herokuapp.com/)|
|[models](/app/models)|Contains both raw and cleaned [datasets](https://en.wikipedia.org/wiki/Data_set)|
|[controllers](/app/controllers)|Contains the necessary [callbacks](https://dash.plotly.com/basic-callbacks) for the [dashboard](https://nft-transaction-dashboard.herokuapp.com/)|
|[views](/app/views)|Contains the [layout](https://dash.plotly.com/layout) of each visualization for the [dashboard](https://nft-transaction-dashboard.herokuapp.com/)|
|[data preprocessing](/app/preprocessing.py)|Preprocess the data from the [cleaned datasets](/app/models/cleaned-datasets) into fully usable [datasets]((https://en.wikipedia.org/wiki/Data_set))|
|[dashboard.py](dashboard.py)|Driver code to run the [dashboard](https://nft-transaction-dashboard.herokuapp.com/)|
|[notebook](GRMDS%20NFT%20Analysis.ipynb)|Contains all data processes and visualizations providing the necessary components to build the [dashboard](https://nft-transaction-dashboard.herokuapp.com/)|
|[technical report](GRMDS%20NFT%20Technical%20Report.pdf)| A presentation containing our groups analysis report on the NFT Transactions|
|[requirements.txt](requirements.txt)|Contains the necessary modules to build the [dashboard](https://nft-transaction-dashboard.herokuapp.com/)|

### Project Deployment Steps (in Visual Studio Code)
1. Clone this repository
2. Set up a virtual environment by typing ```python -m venv env``` in the command line
3. Set your interpreter path to the virtual environment path
4. Download all the dependencies (modules) by typing ```python -m pip install -r requirements.txt```
5. Run dashboard.py on Python terminal
6. Go to http://localhost:8050/ to go to the dashboard
