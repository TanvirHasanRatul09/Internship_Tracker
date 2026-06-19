class Application:

    VALID_STATUSES = [
        "Applied",
        "Under Review",
        "Interview",
        "Accepted",
        "Rejected",
        "Withdrawn"
    ]

    def __init__(
        self,
        student_id,
        company_id,
        position,
        apply_date,
        deadline,
        status
    ):
        self.student_id = student_id
        self.company_id = company_id
        self.position = position
        self.apply_date = apply_date
        self.deadline = deadline
        self.status = status

    def validate(self):

        if not self.position.strip():
            print("Position cannot be empty.")
            return False

        if self.status not in self.VALID_STATUSES:
            print("Invalid status.")
            return False

        if self.deadline < self.apply_date:
            print("Deadline cannot be before apply date.")
            return False

        return True