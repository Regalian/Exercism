class School:
    def __init__(self):
        self._students: dict[str, int] = {}
        self._added: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        """Add a student to the school

        Student names are unique across grades, i.e. there can only be one, Highlander
        If a student already exists update fails. Success or otherwise of update is recorded.

        Args:
            name (str): The name of the student
            grade (int): The grade of the student
        """

        if name not in self._students:
            self._students[name] = grade
            self._added += [True]
        else:
            self._added += [False]

    def roster(self) -> list[str]:
        """ School roster.

        returns: list[str]: Students sorted by grade and then by name
        """
        return sorted(self._students.keys(), key=lambda x: (self._students[x], x))

    def grade(self, grade_number: int) -> list[str]:
        """Grade roster.

        returns: list[str]: Students in grade sorted by name
        """
        return sorted(
            [
                student
                for student, grade in self._students.items()
                if grade == grade_number
            ]
        )

    def added(self):
        """ Success status of student addition.

        returns: list[bool]: statuses of student addition attempts.
        """
        return self._added
