class Interview:

    VALID_RESULTS = [
        "Pending",
        "Passed",
        "Failed"
    ]

    def __init__(
        self,
        application_id,
        interview_date,
        result
    ):
        self.application_id = application_id
        self.interview_date = interview_date
        self.result = result

    def validate(self):

        if self.result not in self.VALID_RESULTS:
            print("Invalid result.")
            return False

        return True