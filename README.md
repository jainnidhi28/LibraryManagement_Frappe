
Library Management System

A full-stack Library Management Web Application built with Django (Backend) and Vue.js (Frontend). This system allows librarians or administrators to manage books, members, and book transactions efficiently. It also supports importing book data from the Frappe Public Library API.


Features

🔹 Book Management
	•	Add new books manually with details like title, author, ISBN, publisher, page count, and stock.
	•	Import books from frappe.io public library API.
	•	Edit and delete books.
	•	Book list with search functionality.

🔹 Member Management
	•	Add and manage members with name, email, and outstanding debt tracking.
	•	Edit and delete member information.

🔹 Transactions (Issue & Return)
	•	Issue books to members (only if their debt ≤ ₹500).
	•	Return books with rent fee input.
	•	Update stock and member debt accordingly.
	•	Prevent issuing books to debt-heavy members (validation included).

🔹 Return System
	•	A separate route to return books.
	•	Displays book and member details.
	•	Allows return date and rent fee input.

Tech Stack
	•	Frontend: Vue.js 
	•	Backend: Django, Django REST Framework
	•	Database: SQLite (dev)
	•	CORS: Handled using django-cors-headers
	•	External API: Frappe Public Library API for importing books


⚙️ Getting Started

Backend (Django)

cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Frontend (Vue.js)

cd frontend/library-frontend
npm install
npm run dev

Access the app at: http://localhost:5173

Screenshots 
<img width="1429" alt="Screenshot 2025-04-09 at 10 54 09 PM" src="https://github.com/user-attachments/assets/72018dce-0fab-4368-8463-61d3d368d280" />
<img width="1429" alt="Screenshot 2025-04-09 at 10 53 57 PM" src="https://github.com/user-attachments/assets/ae89b10e-653a-4493-9988-64989273f52c" />
<img width="1429" alt="Screenshot 2025-04-09 at 10 53 51 PM" src="https://github.com/user-attachments/assets/18a17d1a-6c37-405b-9d2d-e236ce59d14d" />
<img width="1429" alt="Screenshot 2025-04-09 at 10 53 39 PM" src="https://github.com/user-attachments/assets/754859ca-531b-448b-a92b-d3a0a95a1e26" />
<img width="1429" alt="Screenshot 2025-04-09 at 10 53 29 PM" src="https://github.com/user-attachments/assets/4c09ea84-bd9f-4f4c-9d0d-dd41797c7ede" />
<img width="1429" alt="Screenshot 2025-04-09 at 10 53 22 PM" src="https://github.com/user-attachments/assets/304ed3ad-38a9-4472-a0b3-f29cd7a1a4ee" />
<img width="1429" alt="Screenshot 2025-04-09 at 10 53 12 PM" src="https://github.com/user-attachments/assets/142e37b4-f468-4766-a209-1ecf4b8364cd" />
<img width="1429" alt="Screenshot 2025-04-09 at 10 52 47 PM" src="https://github.com/user-attachments/assets/1ab6b995-5bc6-45bb-90a8-aefef38a6dcf" />
<img width="1429" alt="Screenshot 2025-04-09 at 10 52 08 PM" src="https://github.com/user-attachments/assets/556c76f6-72c9-4aef-be07-4328a271b247" />




📄 License

This project is open-source and available under the MIT License.



