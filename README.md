
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
![image](https://github.com/user-attachments/assets/c7946669-15c2-4368-afbb-d5fcf9a61354)
![image](https://github.com/user-attachments/assets/67ff5649-6639-4135-9845-f08651bb6aec)
![image](https://github.com/user-attachments/assets/c5c13b8f-86b9-4f42-a41b-004249b1621f)
![image](https://github.com/user-attachments/assets/bca6d112-cddc-49fa-a72e-11e75efc1b88)
![image](https://github.com/user-attachments/assets/43d83b9b-4180-4ffd-ac28-bb6a5b4c7ac5)
![image](https://github.com/user-attachments/assets/163358bf-9ef1-486c-b86c-165bb3574bf4)
![image](https://github.com/user-attachments/assets/5a305627-de4f-4823-9097-f3c642c4c032)
![image](https://github.com/user-attachments/assets/9cc4832e-a6da-4483-bea9-11af020f89a7)
![image](https://github.com/user-attachments/assets/03f4da9f-51fd-4902-8513-e86681be2930)








📄 License

This project is open-source and available under the MIT License.



