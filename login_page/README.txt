NANA MILLETS LOGIN PAGE (FLASK)

1. Open this folder in Visual Studio Code.
2. Open Terminal > New Terminal.
3. Create and activate a virtual environment (recommended):
   Windows:
     py -m venv .venv
     .venv\Scripts\activate
4. Install Flask:
     pip install -r requirements.txt
5. Run the app:
     python app.py
6. Open this address in your browser:
     http://127.0.0.1:5000

IMPORTANT:
- This is a UI/form starter, not a production-ready authentication system.
- The login form currently validates that both fields are filled in and displays a demo message.
- Connect it to a user database and verify password hashes before enabling real sign-in.
- Replace SECRET_KEY and load it from an environment variable before deployment.
- Signup and forgot-password routes are placeholders.

Create account page: open http://127.0.0.1:5000/signup
Note: registration is a front-end/demo flow only; it does not save users. Connect a database and securely hash passwords before real use.
