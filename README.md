### mail_app 

This project (mail_app) consists of several files for downloading email attachments and storing them in a database. Below are instructions on how to set up and run the project manually or using Docker.

#### Files:

- **logger.py**: This file contains the logger configuration used for logging information, errors, and warnings during the execution of the application.
- **db.py**: This file contains the SQLAlchemy database model and session setup.
- **main.py**: This file contains the functions for downloading email attachments and uploading them to the database.

#### Setup:

1. **Environment Setup:**

   - Create a virtual environment using `python -m venv venv`.
   - Activate the virtual environment:
     - On Windows: `source venv\Scripts\activate`
     - On macOS and Linux: `source venv/bin/activate`.
   - Install dependencies using `pip install -r requirements.txt`.

2. **Environment Variables:**

   - Fill in the required environment variables in the `.env` file. Example:

     ```dotenv
      EMAIL=your_email@example.com
      PASSWORD=your_email_password
      IMAP_SERVER=imap.example.com
      IMAP_PORT=993
      ATTACHMENTS_DIR=Attachments
      LOGS_DIR=Logs
      DB_USER=your_db_user
      DB_PASSWORD=your_db_password
      DB_HOST=your_db_host
      DB_PORT=your_db_port
      DB_NAME=your_db_name
     ```

#### Running the Application:

**Manual Execution:**

- Make sure the virtual environment is activated `source venv/bin/activate`.
- Run the application using `python3 mail_app/main.py`.


**Build the Docker Image:**

   ```bash
   docker compose up --build
   ```
