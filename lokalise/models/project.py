class ProjectModel:
    ATTRS = [
        "project_id",
        "project_type",
        "name",
        "description",
        "created_at",
        "created_at_timestamp",
        "created_by",
        "created_by_email",
        "team_id",
        "base_language_id",
        "base_language_iso",
        "settings",
        "statistics"
    ]

    def __init__(self, raw_data):
        self.raw_data = raw_data
        for attr in self.ATTRS:
            setattr(self, attr, raw_data.get(attr, None))

    def __str__(self):
        result = ""
        for attr in self.ATTRS:
            if len(result) != 0:
                result += "\n"
            result += f"{attr}: {getattr(self, attr)}"

        return result
