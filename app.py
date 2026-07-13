from datetime import datetime

from flask import (
    abort,
    Flask,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from database.db import get_db_connection

app = Flask(__name__)

# App security
app.secret_key = "charity_event_secret_key"


@app.route("/")
def home():
    connection = get_db_connection()

    event = connection.execute(
        "SELECT * FROM Event LIMIT 1"
    ).fetchone()

    connection.close()

    return render_template("index.html", event=event)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        registration_date = datetime.now().strftime("%Y-%m-%d")

        connection = get_db_connection()

        # This project currently has one event, so registrations use event 1.
        connection.execute(
            """
            INSERT INTO Registration
            (participant_name, email, phone, registration_date, event_id)

            VALUES (?, ?, ?, ?, ?)
            """,
            (name, email, phone, registration_date, 1),
        )

        connection.commit()
        connection.close()

        # Success message
        flash("Registration completed successfully.", "success")

        return redirect(url_for("participants"))

    return render_template("register.html")


@app.route("/participants")
def participants():
    # Open database
    connection = get_db_connection()

    # Get records
    participants = connection.execute(
        """
        SELECT *
        FROM Registration
        ORDER BY registration_id DESC
        """
    ).fetchall()

    # Close database
    connection.close()

    # Load page
    return render_template(
        "participants.html",
        participants=participants,
    )


@app.route("/registration/<int:id>")
def registration_detail(id):
    # Open database
    connection = get_db_connection()

    # Get record
    registration = connection.execute(
        """
        SELECT
            Registration.registration_id,
            Registration.participant_name,
            Registration.email,
            Registration.phone,
            Registration.registration_date,
            Event.event_name,
            Event.event_date,
            Event.location

        FROM Registration

        JOIN Event

        ON Registration.event_id = Event.event_id

        WHERE Registration.registration_id = ?
        """,
        (id,),
    ).fetchone()

    # Close database
    connection.close()

    # Check record
    if registration is None:
        # Show error
        abort(404)

    # Load page
    return render_template(
        "registration_detail.html",
        registration=registration,
    )


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_registration(id):
    # Open database
    connection = get_db_connection()

    if request.method == "POST":
        # Get form
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        # Update record
        connection.execute(
            """
            UPDATE Registration

            SET
                participant_name = ?,
                email = ?,
                phone = ?

            WHERE registration_id = ?
            """,
            (name, email, phone, id),
        )

        # Save changes
        connection.commit()

        # Close database
        connection.close()

        # Success message
        flash("Registration updated successfully.", "success")

        # Redirect page
        return redirect(url_for("participants"))

    # Get record
    registration = connection.execute(
        """
        SELECT *

        FROM Registration

        WHERE registration_id = ?
        """,
        (id,),
    ).fetchone()

    # Close database
    connection.close()

    # Check record
    if registration is None:
        # Show error
        abort(404)

    # Load page
    return render_template(
        "edit_registration.html",
        registration=registration,
    )


@app.route("/delete/<int:id>")
def delete_registration(id):
    # Open database
    connection = get_db_connection()

    # Get record
    registration = connection.execute(
        """
        SELECT *
        FROM Registration
        WHERE registration_id = ?
        """,
        (id,),
    ).fetchone()

    # Check record
    if registration is None:
        # Close database
        connection.close()

        # Show error
        abort(404)

    # Delete record
    connection.execute(
        """
        DELETE FROM Registration
        WHERE registration_id = ?
        """,
        (id,),
    )

    # Save changes
    connection.commit()

    # Close database
    connection.close()

    # Success message
    flash(
        "Registration cancelled successfully.",
        "success",
    )

    # Redirect page
    return redirect(url_for("participants"))


@app.errorhandler(404)
def page_not_found(error):
    # Load error
    return render_template(
        "404.html",
    ), 404


if __name__ == "__main__":
    app.run(debug=True)
