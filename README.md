# AWS-Machine-learning-integration

This project demonstrates the integration of machine learning models to improve the accuracy of event detection, particularly focusing on identifying privilege escalation patterns. The project uses historical event data, preprocesses it, trains a machine learning model, and allows you to detect potentially suspicious events.
Installation

    Clone the repository:

    sh

git clone https://github.com/your-username/event-detection-project.git
cd event-detection-project

Install the required Python packages:

sh

    pip install -r requirements.txt

Usage

    Place your historical event data CSV file in the data directory (e.g., data/historical_event_data.csv).

    Run the main script to perform data preprocessing, model training, and event detection:

    sh

    python main.py

    The script will display a classification report showing the model's performance on the test data. It will also prompt you to input an event description for event detection.

    Follow the instructions to provide an event description. The script will then predict whether the event is potentially a privilege escalation.

Command Line Interface (CLI)
