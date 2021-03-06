import re

class Reviewer():

	def __init__(self, config_reader=None):
		self.config_reader = config_reader
	
	def get_name(self):
		return "formatting"
	
	def review_statement_spacing(self, file_content, message_bag):
		bad_format = len(re.findall("[a-zA-Z0-9_$]+: function", file_content))
		bad_format += len(re.findall("[a-zA-Z0-9_$]+:function", file_content))
		bad_format += len(re.findall(":function\(", file_content))
		bad_format += len(re.findall(": function\(", file_content))
		bad_format += len(re.findall(":function \(", file_content))
		bad_format += len(re.findall("function [a-zA-Z0-9$_]+\(", file_content))
		bad_format += len(re.findall("if\(", file_content))
		bad_format += len(re.findall("\)\{", file_content))
		
		if bad_format != 0:
			message_bag.add_error(self, "It seems you haven't properly formatted your file. Make sure you have configured a proper formatter")
	
	def review_empty_lines(self, lines, message_bag):
		empty_lines_passed = 0
		line_number_of_first_empty = -1
		for line in lines:
			if line.is_empty():
				if line_number_of_first_empty == -1:
					line_number_of_first_empty = line.line_number
				empty_lines_passed += 1
			else:
				empty_lines_passed = 0
				line_number_of_first_empty = -1
			
			if empty_lines_passed > 2:
				message_bag.add_warning(self, "There are several empty lines in a row, either you didn't format the file correctly, or you are trying to space complex things out.", line_number_of_first_empty)
	
	def review(self, file_data, message_bag):
		# TODO: The formatting reviewer is fucked up today, it only checks a few things and doesn't say where problems are
		# So it's better not to include it at all in fact
		#self.review_statement_spacing(file_data.content, message_bag)
		self.review_empty_lines(file_data.lines.all_lines, message_bag)
		
		
if __name__ == "__main__":
	print "NO TESTS TO RUN"