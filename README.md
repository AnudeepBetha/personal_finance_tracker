# Personal Finance Tracker

A web-based application designed to manage, track, and analyze personal financial transactions and goals.
## Features

- **Add Transactions**: Quickly input both income and expense transactions.
- **Bulk Add**: Option to add multiple transactions consecutively without interruption.
- **Edit Transactions**: Modify transaction details with ease.
- **Delete Transactions**: Remove unwanted transactions with a single click.
- **Dashboard**: Overview of transactions in a structured table format.
- **Budgeting**: Set financial goals for any month.
- **Trends**: Graphical representation of monthly income and expense patterns.
- **Reports**: In-depth visual analysis of income, expenses, and set goals over a month.

## Installation

1. **Install Python**:

   Before you can run/install this application, you need to have Python installed on your system. This application is built using Python, and having Python installed is a prerequisite.

   To check if Python is already installed on your system, open your terminal or command prompt and run the following command:

   ```bash
   python --version

2. **Clone the Repository**: 
   
   ```bash
   git clone git@code.umd.edu:anudeep/ENPM809WFall2023Project-anudeep.git
   ```

- Make sure you're in cloned project when running the following commands.

3. **Install Dependencies**:
 

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Django Migrations**:

    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

## Run the App:

```bash
python manage.py runserver
```

## Run Tests:
- For Entire Web Application
```bash
python manage.py test
```
- For Specific Application
```bash
python manage.py test <app-name>
```

## Test Account Credentials

- **Username**: testuser2.
- **Password**: TestPassword@123


## Workflow

1. **Access the Application**: Begin by entering the URL of the application(http://127.0.0.1:8000/) into the browser of your choice.

2. **Login/Registration**: If you're not already logged in, you'll be prompted to either log in or register. For testing purposes, you can use the test account credentials provided.

3. **Dashboard Overview**: 
   - Once logged in, you'll land on the dashboard, which provides a structured table format overview of all your transactions.
   - Each transaction entry in the table has an edit and delete icon associated with it.

4. **Edit Transactions**: 
   - Locate the transaction you want to modify from the table.
   - Click on the edit icon (pencil symbol) next to the desired transaction.
   - Update the necessary details such as the amount and date.
   - After making the changes, click on the save icon to save the modifications.

5. **Delete Transactions**: 
   - Identify the transaction you wish to remove from the table.
   - Click on the delete icon (trash bin symbol) next to the transaction you want to remove. The transaction will be deleted from the database.

6. **Add Transactions**: 
   - Use the "Financials" feature to input both income and expense transactions.
   - Choose the "Add Multiple Transactions" option if you wish to add multiple transactions consecutively without being redirected.

7. **Budget**: Navigate to the "Budget" section where you can:
   - Set financial goals for any month.
   - View your progress towards achieving those goals using the "Reports" section.

8. **Trends and Reports**: 
   - Access the "Trends" section to view a graphical representation of your monthly income and expense patterns.
   - Move to the "Reports" section for an in-depth visual analysis of income, expenses, and set goals over a month.
   - The charts in both sections are interactive. Clicking on a specific legend item in the chart will toggle the visibility of that data series, allowing you to focus on specific aspects of your financial data.

9. **Logout**: Once you're done with your tasks, you can safely log out from the application.

10. **Admin Operations**: Using the Pre-Built Django's Admin Panel (available at http://127.0.0.1:8000/admin/) the admin of this application will be able to perform user management and also perform transaction, budget data management. Currently only the Admin has the prvilieges to change the password for a user account.



## Dependencies

- **Django 4.2.6**: Web framework.
- **django-tables2 2.6.0**: Simplify table creation.

## Conclusion

The Personal Finance Tracker offers a comprehensive and user-friendly solution to manage and understand your finances.