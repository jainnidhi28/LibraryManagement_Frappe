
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
<img width="1440" alt="Screenshot 2025-04-09 at 10 43 08 PM" src="https://github.com/user-attachments/assets/e84c8e2c-5561-414f-845c-d00679eb9d0a" />
<img width="1440" alt="Screenshot 2025-04-09 at 10 43 03 PM" src="https://github.com/user-attachments/assets/60ce2628-c6fc-4028-857b-c42d969d894b" />
<img width="1440" alt="Screenshot 2025-04-09 at 10 43 00 PM" src="https://github.com/user-attachments/assets/2e6b7bb2-6057-41db-8b16-3ed23e7dc02f" />
<img width="1440" alt="Screenshot 2025-04-09 at 10 42 55 PM" src="https://github.com/user-attachments/assets/7b117e06-326c-4a62-964f-1f9299d957af" />
<img width="1440" alt="Screenshot 2025-04-09 at 10 42 52 PM" src="https://github.com/user-attachments/assets/320242ad-855a-425b-95fc-00571caa11df" />
<img width="1440" alt="Screenshot 2025-04-09 at 10 42 46 PM" src="https://github.com/user-attachments/assets/a6b85778-17d8-48cf-8fb9-995dcaad3814" />
<img width="1440" alt="Screenshot 2025-04-09 at 10 42 37 PM" src="https://github.com/user-attachments/assets/c8ff7621-a8e8-48a4-80fd-0ee6c57bfab1" />
<img width="1440" alt="Screenshot 2025-04-09 at 10 42 29 PM" src="https://github.com/user-attachments/assets/8fcfc2b4-8e18-4f40-9eae-2c8170938517" />
<img width="1440" alt="Screenshot 2025-04-09 at 10 41 19 PM" src="https://github.com/user-attachments/assets/66ff47de-5b57-4362-b84a-f7b475255664" />





📄 License

This project is open-source and available under the MIT License.



