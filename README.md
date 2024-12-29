# el_pais_scrapper
A script demonstrating skills in web scraping, API integration, and text processing using the Selenium framework

# Note : The final output can be seen in final_output.txt file
## Problem Statement

This Python project aims to scrape and analyze articles from the "Opinion" section of El País, a Spanish news outlet. The main objectives are:

1. **Website Verification**: Ensure the website's text is displayed in Spanish.
2. **Article Scraping**:
   - Navigate to the Opinion section.
   - Fetch the first five articles' titles and content.
   - Save the cover image of each article locally (if available).
3. **Header Translation**:
   - Use a translation API (e.g., Google Translate API or Rapid Translate Multi Traduction API) to translate article titles into English.
   - Print the translated headers.
4. **Header Analysis**:
   - Identify words repeated more than twice across all translated headers.
   - Print each repeated word and its occurrence count.
5. **Cross-Browser Testing**:
   - Run the scraper locally to verify functionality.
   - Execute the solution on BrowserStack using 5 parallel threads to test across desktop and mobile browsers.

---

## Project Structure

Below is the project directory structure:

```
|-- .pytest_cache
|-- config
|   |-- __init__.py
|   |-- api_keys.py
|-- data/images
|   |-- data_images_'Las tres fronte...
|   |-- data_images_50 años de la m...
|   |-- data_images_Carta de invier...
|   |-- data_images_Feijóo y la conf...
|   |-- data_images_Un buen año pa...
|-- scraper
|-- tests
|   |-- __init__.py
|   |-- browserstack_tests.py
|-- venv
|   |-- bin
|   |-- include
|   |-- lib
|   |-- pyvenv.cfg
|-- main.py
|-- requirements.txt
```

### Project Structure Description
- **`config/`**: Contains configuration files, including API keys.
- **`data/images/`**: Directory to store cover images of articles.
- **`scraper/`**: The main scraper logic will be implemented here.
- **`tests/`**: Contains unit and integration tests, including BrowserStack tests.
- **`venv/`**: Virtual environment for dependency isolation.
- **`main.py`**: Entry point of the application.
- **`requirements.txt`**: Lists all required dependencies.

## Structure Image

<img width="310" alt="Screenshot 2024-12-29 at 3 43 45 PM" src="https://github.com/user-attachments/assets/35c7c90b-a9c5-4d7c-ac8b-9d27864b34ab" />

---

## Build Image

<img width="1364" alt="Screenshot 2024-12-29 at 3 49 53 PM" src="https://github.com/user-attachments/assets/584f811b-1f4e-4a5f-bfb4-7694e1faab5c" />


---

## How to Install and Run

### Prerequisites
- Python 3.8 or later
- Virtual environment set up (recommended)
- BrowserStack account (for cross-browser testing)
- API keys for translation (e.g., Google Translate or Rapid Translate Multi Traduction API)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/python-scraper.git
   cd python-scraper
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure API keys:
   - Add your API keys to `config/api_keys.py`.

### Running the Project
1. Execute the scraper locally:
   ```bash
   python main.py
   ```

2. Run tests:
   ```bash
   pytest tests/
   ```

3. Execute cross-browser tests on BrowserStack:
   - Ensure BrowserStack credentials are configured in the test setup.
   - Run the BrowserStack test script:
     ```bash
     python tests/browserstack_tests.py
     ```

---

## Notes
- Update paths in the codebase as needed to reflect your local setup.
- Replace the placeholder `path-to-build-image` with the actual path to the build image file.

Feel free to reach out for support !!

