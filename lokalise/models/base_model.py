class BaseModel:
    ATTRS = []
    DATA_KEY = ''

    def __init__(self, raw_data):
        self.raw_data = raw_data
        if 'project_id' not in self.ATTRS:
            self.project_id = raw_data.get('project_id', None)

        for attr in self.ATTRS:
            if hasattr(self, 'DATA_KEY'):
                raw_data = raw_data.get(self.DATA_KEY, raw_data)
            setattr(self, attr, raw_data.get(attr, None))

    def __str__(self):
        result = ""
        for attr in self.ATTRS:
            if len(result) != 0:
                result += "\n"
            result += f"{attr}: {getattr(self, attr)}"

        return result
