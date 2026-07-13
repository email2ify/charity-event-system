# Charity Fundraising Event Registration System

## Project Overview

This project is a web-based event registration and management
application developed for a charity fundraising event.

Participants can view event information and submit registrations.
Organisers can view, update, and cancel participant registrations.

## Technologies

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

## Main Features

- Event information page
- Participant registration form
- SQLite database storage
- Registered participant list
- Registration detail page
- Edit registration
- Cancel registration
- JavaScript cancellation confirmation
- Flash notification messages
- Responsive design
- Custom error handling

## Database Structure

The database contains two related tables:

1. Event
2. Registration

One event can contain many registrations.

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create the database:

```bash
python database/init_db.py
```

5. Run the application:

```bash
python app.py
```

## Project Scope

The application intentionally focuses on the minimum required
functionality. Advanced features such as authentication, payments,
email notifications, and multiple event management are outside the
current project scope.

## Complete Functional Testing

Perform each test manually and record the result for the report's
testing section.

| Test | Expected result |
|---|---|
| Open home page | Event information appears |
| Select Register | Registration form opens |
| Submit valid form | Registration is saved |
| Submit spaces only | Error message appears |
| Submit invalid email | Browser rejects form |
| Open participants | All registrations appear |
| Select View | Correct details appear |
| Edit registration | Updated data appears |
| Cancel and reject confirmation | Registration remains |
| Cancel and approve confirmation | Registration is removed |
| Open invalid ID | Custom 404 page appears |
| Use mobile view | Layout adjusts correctly |
| Navigate with Tab | Focus indicator appears |

## Remove Test Data

Before submission:

1. Open the database.
2. Remove unnecessary test registrations.
3. Keep zero, one, or two realistic sample registrations.
4. Ensure the sample event remains present.
5. Restart the application.
6. Perform one final complete test.

## Final Git Commit

Check the project status:

```bash
git status
```

Stage the files:

```bash
git add .
```

Commit the project:

```bash
git commit -m "Complete charity event registration system"
```

Optional version tag:

```bash
git tag v1.0
```
