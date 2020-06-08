class ProjectModel:
    def __init__(self, raw_data):
        attrs = ["project_id"]
        for attr in attrs:
            setattr(self, attr, raw_data.get(attr, None))
