# How to Run the Project Locally

## 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/uae-market-expansion-advisor.git  
cd uae-market-expansion-advisor

## 2. Create a virtual environment

python -m venv .venv

Activate it:

Windows

.venv\Scripts\activate

Mac/Linux

source .venv/bin/activate

## 3. Install dependencies

pip install -r requirements.txt

## 4. Configure environment variables

Create a `.env` file in the project root:

OPENAI_API_KEY=your_api_key_here

## 5. Run the CLI advisor

python -m app.cli

You can now ask questions such as:

Where should we open our first branch in Dubai?

Type `quit` to exit the program.
