db.session.add(
    User(
        first_name="Test",
        last_name="Doe",
        email_address="test@example.com",
        mobile_number="+8801172211111",
    )
)

db.session.commit()
