def convert_to_int_or_float(data):
	"""
	Function to convert various numpy int and floats output to 'python' int and float to enable conversion
	to json format but FastAPI
	:param data:
	:return:
	"""
	if isinstance(data, dict):
		return {key: convert_to_int_or_float(value) for key, value in data.items()}
	elif isinstance(data, list):
		return [convert_to_int_or_float(value) for value in data]
	else:
		if data.is_integer():
			return int(data)
		else:
			return float(data)
