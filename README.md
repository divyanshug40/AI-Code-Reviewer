# Python Code Reviewer

## Introduction

The **Python Code Reviewer** is an easy-to-use web application powered by **Streamlit** and **Google's Generative AI**. This app assists users by reviewing Python code snippets, providing helpful feedback, identifying bugs, suggesting optimizations, and offering clear explanations in a user-friendly manner.

With this tool, you can quickly receive an automated review of your Python code. Whether you're a beginner or an experienced developer, the app helps improve your coding by pointing out errors, inefficiencies, and ways to make your code cleaner and more efficient.

---

## Features

- **Bug Detection**: The app will automatically detect potential bugs and errors in the Python code.
- **Code Optimization**: The reviewer will suggest areas where code can be optimized for better performance and readability.
- **Step-by-Step Explanation**: Each bug fix or code improvement is accompanied by an explanation, making it easy to understand the changes.
- **Code Review in Real-Time**: The app provides real-time feedback, allowing users to see and fix issues immediately.
- **User-Friendly Interface**: The interface is designed to be intuitive, with clear instructions and easy navigation.

---

## How It Works

1. **Input your Code**: You can enter your Python code directly into the provided text area.
2. **Click the "Review Code" Button**: Once your code is ready, click the "Review Code" button. The AI-powered model will then analyze your code.
3. **Review the Feedback**: The app will present you with a detailed code review, pointing out any bugs or inefficiencies, and suggesting improvements.
4. **Fixed Code and Explanation**: Along with the review, the app provides a fixed version of your code and an explanation of the changes made.

---

## Installation

To run this Python code review app locally, follow these steps:

### Prerequisites

- Python 3.x
- Streamlit (for building the web interface)
- Google Generative AI SDK (for code reviewing)

### Step-by-Step Guide

1. **Clone the Repository**: If you are working with a version control system like Git, clone the repository:

   ```bash
   git clone https://github.com/your-repo/Python-Code-Reviewer.git```
2. **Install Dependencies**: Install all required Python libraries using pip:

   ```bash
   pip install -r requirements.txt```
   Ensure that you have **Streamlit** and **google-generativeai** in the requirements.txt file.
3. **Set Up API Key**:
   The app uses Google’s Generative AI API. Make sure you have a valid API key from Google’s platform. Set it up in the script as shown below:
   
  ```python
  ai.configure(api_key="YOUR_API_KEY")
```
  Replace "YOUR_API_KEY" with your actual API key.
4. **Run the Application**:
  Finally, run the Streamlit app using the following command:

  ```bash
  streamlit run app.py```
  This will open the app in your browser where you can start testing it.
