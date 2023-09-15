# Travel Recommendations

# Project Overview

Create a simple FastAPI application that serves an endpoint to recommend three things to do in a given country during a specific season by consulting the OpenAI API.

# Tools and Technologies

- Python
- FastAPI
- OpendAPI
- PyTest
- VsCode

# Installation

1. Clone the repository:
```
git clone https://github.com/aipiping/hiring.git

```
2. Navigate to the project directory:
```
cd travel_recommendations
```

3. Create a virtual environment:
```
python3 -m venv venv
```
or

```
virtualenv venv
```

4. Activate the virtual environment:
```
source venv/bin/activate
```

5. Install the project dependencies:
```
pip install -r requirements.txt
```


7. Start the development server to run the port on 3000:
```
uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```
# How to Get the API:

- Export OpenAPI JSON: If you want to export the OpenAPI specification as a JSON file, you can use FastAPI's built-in endpoint. Visit http://0.0.0.0:3000/openapi.json to get the JSON representation of your API. You can then save this JSON file and share it with others.

## Test the Code

- Open the vscode.
- Go to the test flask icon on the VScode.
- Click on configure.
- Select Pytest as Testing Framework.
- Select the tests folder directory.

After doing these steps the tests will be configured.

# Runing the tests

- Click on Run tests button the tests will be running.
