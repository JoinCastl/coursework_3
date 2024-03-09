import json
from zipfile import ZipFile
from datetime import datetime


def get_last_five_operations(zip_file):
    operations = []

    with ZipFile(zip_file, 'r') as archive:
        for file in archive.filelist:
            with archive.open(file.filename) as f:
                data = json.load(f)
                if data.get('state') == 'EXECUTED':
                    operation_date = datetime.strptime(data.get('date'), '%d.%m.%Y').date()
                    operations.append((data, operation_date))

    operations.sort(key=lambda x: x[1], reverse=True)

    result = []

    for data, _ in operations[:5]:
        output = [
            data.get('date'),
            data.get('description'),
            f"{data.get('from')} -> {data.get('to')}",
            f"{data.get('operationAmount')} руб."
        ]

        result.append('\n'.join(output))

    return result


if __name__ == '__main__':
    last_five_operations = get_last_five_operations('operations.zip')
    for operation in last_five_operations:
        print(operation)
        print()