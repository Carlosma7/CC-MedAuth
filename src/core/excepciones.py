# IBAN not valid
class IBANFormatError(Exception):
	"""Raised when the input IBAN is not valid"""
	pass

# Wrong user type
class WrongUserTypeError(Exception):
	"""Raised when the user type is not valid"""
	pass

# Email not valid
class EmailFormatError(Exception):
	"""Raised when the input Email is not valid"""
	pass

# DNI not valid
class DNIFormatError(Exception):
	"""Raised when the input DNI is not valid"""
	pass

# An user exists with DNI provided
class ExistingUserError(Exception):
	"""Raised when the input user already exists"""
	pass

# User doesn't exist
class NonExistingUserError(Exception):
	"""Raised when the input user doesn't exist"""
	pass

# User already has an active policy
class ActivePolicyError(Exception):
	"""Raised when an input user has already an active policy"""
	pass

# Policy doesn't exist
class NonExistingPolicyError(Exception):
	"""Raised when an input policy doesn't exist"""
	pass

# The medical speciality is not valid
class SpecialityError(Exception):
	"""Raised when the input Speciality is not valid"""
	pass
	
# The prescription is not associated with the active policy
class TimedOutPrescriptionError(Exception):
	"""Raised when the input prescription is associated with a policy different from the active"""
	pass

# User has not an active policy
class NonActivePolicyError(Exception):
	"""Raised when the input user doesn't have an active policy"""
	pass

# Prescription ID doesn't exist
class NonExistingPrescriptionIDError(Exception):
	"""Raised when the input prescription ID doesn't exist"""
	pass

# The authorization is not associated with the active policy
class TimedOutAuthorizationError(Exception):
	"""Raised when the input authorization is associated with a policy different from the active"""
	pass

# Authorization doesn't exist
class NonExistingAuthorizationError(Exception):
	"""Raised when the input authorization doesn't exist"""
	pass

# Appointment doesn't exist
class NonExistingAppointmentError(Exception):
	"""Raised when the input appointment ID doesn't exist"""
	pass

