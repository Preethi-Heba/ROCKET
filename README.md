🚀 Rocket App

A simple Rocket Information Web Application built using Flask that displays details about rockets, launches, or space missions using an external API (such as SpaceX API).

🚀 Features

🛰 Displays rocket details

📅 Shows launch information

🌍 Displays mission data

🔄 Fetches live API data

🎨 Clean UI design

🛠 Built With
. Python
. Flask
. SpaceX API (or the API you used)
. HTML & CSS
. Requests Library

📂 Project Structure
rocket_app/
│
├── app.py
├── templates/
│     ├── index.html
│
├── static/
│     ├── style.css

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/YOUR-USERNAME/rocket-app.git
cd rocket-app
2️⃣ Create virtual environment (optional)
python3 -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
pip install flask requests
4️⃣ Run the application
python3 app.py
5️⃣ Open in browser
http://127.0.0.1:5000

🔄 How It Works

1. App sends request to space API.

2. API returns rocket/launch JSON data.

3. Flask processes and displays it.

4. User can view mission details on UI.

🧠 Future Improvements

🔍 Search rockets by name

📅 Filter launches by date

📊 Display launch statistics

🖼 Add rocket images

🚀 Show live launch countdown
