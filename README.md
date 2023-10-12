## TMDB CONTENT BASED MOVIE RECOMMENDER SYSTEM

Link to the Live Server of my Recommender System:

https://tmdb-content-based-movie-recommender-system-dharmendra.streamlit.app/

## Objective:
Developed a TMDB Content-Based Movie Recommender System utilizing various tools and techniques. The primary objective of this project was to provide users with personalized movie recommendations based on their input, enhancing their movie-watching experience.

## Steps and Methods Used:

Obtained Datasets: Downloaded two distinct datasets from Kaggle - Movies and Credits.

Data Integration: Merged these datasets using pandas, utilizing the title column as the common key.

Data Cleaning: Unnecessary columns such as budget, homepage, and more were removed to streamline the dataset.

Handling Missing Values: Rows with null values in the overview feature were removed, ensuring data quality.

Genre and Keyword Extraction: Functions were created to extract genres and keywords from respective columns.

Actor and Director Extraction: Similar functions were used to extract actor and director names.

Textual Data Preprocessing: Overview, genres, keywords, cast, and director columns were processed for better analysis.

Feature Engineering: Concatenated the preprocessed columns to create a single "tags" feature.

TF-IDF Vectorization: The tags column was transformed into a numerical format using TF-IDF vectorization.

Cosine Similarity: Calculated cosine similarity scores to measure content similarity.

User-Friendly Interface: Developed a user interface using Streamlit to input user preferences and provide movie recommendations.

Web Scraping: Utilized the TMDB API to fetch movie posters for display.

Model Deployment: Saved essential objects as pickle files for deployment and hosted the recommender system on Streamlit Cloud.

## Business Impact:

The implementation of this Content-Based Movie Recommender System has had a significant positive impact on the movie-watching experience and the bottom line:

Enhanced User Experience: Users can now receive personalized movie recommendations based on their preferences, leading to higher user satisfaction and engagement.

Increased User Retention: By offering tailored content suggestions, the system encourages users to stay on the platform, resulting in improved user retention rates.

Revenue Generation: Higher user engagement and longer session durations can potentially lead to increased revenue through advertising and premium subscriptions.

Cost Savings: The system's deployment has streamlined content discovery, reducing the need for costly manual curation and recommendation efforts.

Data-Driven Insights: The project provided insights into user preferences and the popularity of different genres and keywords, enabling data-driven decision-making for content acquisition and production.

## In summary, this TMDB Content-Based Movie Recommender System has not only improved user satisfaction but also demonstrated its potential to drive business growth and efficiency, making it a valuable addition to the platform.
