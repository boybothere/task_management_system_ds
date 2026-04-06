import sys

class ProjectException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_,exec_tb=error_details.exc_info()
        self.lineno=exec_tb.tb_lineno
        self.filename=exec_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "error occurred at line no [{0}] in filename [{1}] with error message [{2}]".format(
            self.lineno,
            self.filename,
            self.error_message
        )