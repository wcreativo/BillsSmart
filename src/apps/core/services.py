import csv
import io


class CSVExporter:
    @classmethod
    def export_to_csv(cls, data, field_names, file_path="output.csv"):
        if data:
            csv_content = io.BytesIO()
            with open(file_path, mode="w", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=field_names)

                writer.writeheader()

                for row in data:
                    writer.writerow(row)

            print(f"The CSV has been generated successfully at {file_path}")
            return True
        else:
            print("Data is required")
            return None
