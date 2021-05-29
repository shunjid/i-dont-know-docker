from models.user import User


def findAll():
    result = User.query.all()
    return result


def findOne(user_id):
    result = User.query.get(user_id)
    return result


def findByEmail(email):
    result = User.query.filter_by(email_address=email).first()
    return result


def findByMobile(mobile):
    result = User.query.filter_by(mobile_number=mobile).first()
    return result


def findByEmailExcludeId(email, user_id):
    result = User.query.filter_by(email_address=email).first()

    if result.id == int(user_id):
        return None
    else:
        return result


def findByMobileExcludeId(mobile, user_id):
    result = User.query.filter_by(mobile_number=mobile).first()

    if result.id == int(user_id):
        return None
    else:
        return result
