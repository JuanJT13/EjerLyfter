class Student:
    def __init__(
        self,
        name,
        section,
        spanish,
        english,
        social_studies,
        science
    ):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social_studies": self.social_studies,
            "science": self.science
        }

    @classmethod
    def from_dict(cls, student_data):
        return cls(
            student_data["name"],
            student_data["section"],
            float(student_data["spanish"]),
            float(student_data["english"]),
            float(student_data["social_studies"]),
            float(student_data["science"])
        )