from App import create_contact_app


contact_app = create_contact_app()

if __name__ == "__main__":
    contact_app.run(debug=True)