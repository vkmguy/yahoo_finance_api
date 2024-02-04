from rest_framework import serializers


class DataFrameSerializer(serializers.Serializer):
    def __init__(self, instance=None, data=None, **kwargs):
        if instance is not None:
            data = self.flatten_dataframe(instance)
        super().__init__(data=data, **kwargs)

    @staticmethod
    def flatten_dataframe(dataframe):
        flattened_data = []
        for _, row in dataframe.iterrows():
            row_data = {}
            for column, value in row.items():
                row_data[column] = value
            flattened_data.append(row_data)
        return flattened_data
