class ValidationResult:
    def __init__(self, is_valid, errors):
        self.is_valid = is_valid
        self.errors = errors


class DeterministicValidator:
    def __init__(self):
        self.required_sections = [
            "Executive Summary",
            "Key Findings",
            "Final Recommendation",
            "Risks and Tradeoffs",
            "Next Data Needed"
        ]

        self.placeholder_markers = [
            "(No Output)",
            "TBD",
            "None",
            "N/A"
        ]

        self.minimum_length = 300

    def validate(self, answer: str, plan: dict) -> ValidationResult:
        errors = []

        answer = (answer or "").strip()

        if not answer:
            errors.append("Answer is empty.")
            return ValidationResult(False, errors)

        if len(answer) < self.minimum_length:
            errors.append("Answer is too short.")

        for section in self.required_sections:
            if section.lower() not in answer.lower():
                errors.append(f"Missing required section: {section}")

        for marker in self.placeholder_markers:
            if marker.lower() in answer.lower():
                errors.append(f"Contains placeholder text: {marker}")

        cities = plan.get("cities", "both")

        if cities == "dubai":
            if "dubai" not in answer.lower():
                errors.append("Dubai-specific answer does not clearly mention Dubai.")

        elif cities == "abudhabi":
            if "abu dhabi" not in answer.lower() and "abudhabi" not in answer.lower():
                errors.append("Abu Dhabi-specific answer does not clearly mention Abu Dhabi.")

        elif cities == "both":
            has_dubai = "dubai" in answer.lower()
            has_abu_dhabi = "abu dhabi" in answer.lower() or "abudhabi" in answer.lower()

            if not has_dubai:
                errors.append("Answer for both cities does not clearly mention Dubai.")
            if not has_abu_dhabi:
                errors.append("Answer for both cities does not clearly mention Abu Dhabi.")

        is_valid = len(errors) == 0
        return ValidationResult(is_valid, errors)