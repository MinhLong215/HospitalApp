def get_user_type(user):
    if user.user_type == 'doctor':
        return 'Doctor'
    elif user.user_type == 'nurse':
        return 'Nurse'
    elif user.user_type == 'patient':
        return 'Patient'
    else:
        return 'Unknown'