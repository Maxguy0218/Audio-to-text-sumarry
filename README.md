# Streamlit Text Summarizer App

This is a simple Streamlit app that uses the Hugging Face model for text summarization. It allows users to input a piece of text, adjust the maximum summary length, and generate a summary of the input text.
Please have a look on the given url.

## Usage

1. Make sure you have Python and the required dependencies installed. You can install the dependencies using the following command: pip install -r requirements.txt
2. Run the Streamlit app locally by executing the following command: streamlit run app.py

3. This will open a new tab in your browser with the app running.

4. Enter the text you want to summarize in the provided text area.

5. Use the slider to select the maximum length for the summary.

6. Click the "Summarize" button to generate the summary.

## Deployment

You can deploy this app to various platforms like Heroku or Streamlit Sharing. Make sure to update the API URL and authorization token in the `app.py` file if you have your own Hugging Face model.

## Dependencies

- streamlit==1.24.0
- requests

## Author

Manas Pandey

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.




