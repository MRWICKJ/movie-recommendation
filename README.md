# Movie Recommendation System

This is a machine learning-based **Movie Recommendation System** built to suggest movies based on user preferences. The model analyzes patterns in the data and recommends movies using content-based filtering.

## Project Overview

- **Framework:** Streamlit is used to build the user interface.
- **Model:** A Machine Learning model built using collaborative filtering and content-based methods.
- **Data Handling:** Managed with Pandas and NumPy for efficient data manipulation.
- **File Storage:** Model data is serialized using Pickle for reusability.
- **API Requests:** Handled using the Requests library to gather data dynamically.

## Features

- **User Interaction:** Simple user interface to select or input movies.
- **Real-Time Recommendation:** Based on user-selected movies, the model generates recommendations.
- **Data Processing:** Uses Pandas and NumPy for data cleaning and manipulation.
- **Efficient Storage:** Model serialized using Pickle for quick loading.
- **Customizable:** Can be extended with additional recommendation strategies like collaborative filtering.

## Technologies Used

- **Python:** Core programming language.
- **Pandas:** For data manipulation.
- **NumPy:** For numerical computation.
- **Streamlit:** To create an interactive web interface.
- **Pickle:** For saving and loading the trained model.
- **Requests:** For handling external API requests.

## Screenshots

**1. User Input Screen**
![User Input](img1.png)

**2. Recommended Movies Screen**
![Recommended Movies](img2.png)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MRWICKJ/movie-recommendation.git
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
Here's an updated section for your `README.md` to include information about using an API key:

---

## Important: API Key Required

To access certain features of the Movie Recommendation System, you may need to obtain an API key from the relevant service. Follow these steps:

1. **Register for an API Key:**
   - Go to the service provider's website (e.g., The Movie Database, TMDB API).
   - Sign up for an account and generate your API key.

2. **Add Your API Key to the Project:**
   - Create a `.env` file in the root of your project.
   - Add your API key in the following format:
     ```
      response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<TMDB_API_KEY>>&language=en-US")
     ```

### Note
Always keep your API keys confidential to prevent unauthorized access and potential misuse. If your API key is exposed, consider regenerating it from the service provider.

---

This section will help users understand the importance of the API key and how to properly manage it in your project. Let me know if you need any more adjustments!

## Contributing

Feel free to contribute by submitting pull requests or reporting issues.

