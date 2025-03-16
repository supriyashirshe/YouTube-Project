# Youtube_DataAnalysis

YouTube Channel Analysis Readme

Overview:
This project focuses on conducting exploratory data analysis (EDA) on data obtained from scraping the APIs of the top 12 YouTube channels based on subscriber count. Additionally, sentiment analysis is performed on the comments of each video to gain insights into viewer sentiments. The findings are then deployed using Streamlit to provide an interactive interface for stakeholders to explore the results of the analysis. Moreover, dashboards are created using Tableau for visualizing key metrics and trends.

Project Structure
The project is organized into the following directories:

data: Contains the datasets obtained from scraping the YouTube API.
notebooks: Jupyter notebooks for conducting EDA and sentiment analysis.
src: Source code for data scraping, EDA, sentiment analysis, and Streamlit app development.
assets: Images, logos, or other media files used in the Streamlit app.
dashboards: Tableau workbooks for visualizing key metrics and trends.
requirements.txt: List of dependencies required to run the project.
Dependencies
Ensure that the following dependencies are installed in your Python environment:

pandas
numpy
matplotlib
seaborn
nltk
vaderSentiment
streamlit
plotly-express
textblob
google-api-python-client
You can install the dependencies using pip with the command:

bash:
pip install -r requirements.txt

Running the Project:
Data Collection: Run the data scraping script in the src directory to collect data from the YouTube API and store it in the data directory.

Exploratory Data Analysis: Explore the collected data using the Jupyter notebooks provided in the notebooks directory. Perform analysis on video metrics, subscriber growth, and audience engagement.

Sentiment Analysis: Utilize the sentiment analysis notebook to classify comments from each video into positive, negative, or neutral sentiments. Analyze sentiment distribution and identify key themes.

Tableau Dashboards: Open the Tableau workbooks provided in the dashboards directory to visualize key metrics and trends derived from the YouTube channel data.

Streamlit App Deployment: Run the Streamlit app script in the src directory to deploy the interactive interface. Users can dynamically explore EDA findings, sentiment analysis results, and insights derived from the top YouTube channels' data.

Usage
Clone the repository:
git clone https://github.com/giri1699/Youtube_DataAnalysis
Navigate to the project directory:
cd youtube-channel-analysis
Follow the steps mentioned in the "Running the Project" section to collect data, conduct analysis, deploy the Streamlit app, and visualize dashboards using Tableau.

Contributors:
Supriya Shirshe
Girish Borkar
Mayuresh Arobekar
Nikhil Patil
Pradnya Yasade
Yash Marje

Acknowledgments
Special thanks to the developers of the libraries and tools used in this project:

NLTK
VADER Sentiment
Streamlit
Google API Client Library
Tableau

