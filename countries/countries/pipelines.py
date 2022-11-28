# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from collections.abc import Mapping
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter


class CountriesPipeline:

    def process_item(self, item, _):
        adapter = ItemAdapter(item)
        
        if adapter.get("name"):
            adapter["name"] = self.clean_name(adapter["name"])
        else:
            raise DropItem(f"Missing name in {item}")
    
        if adapter.get("capital"):
            adapter["capital"] = self.clean_capital(adapter["capital"])
        else:
            raise DropItem(f"Missing capital in {item}")

        if adapter.get("population"):
            population = int(self.clean_population(adapter["population"]))
            adapter["population"] = population
        else:
            raise DropItem(f"Missing population in {item}")

        if adapter.get("area"):
            area = float(self.clean_data(adapter["area"]))
            adapter["area"] = area
        else:
            raise DropItem(f"Missing area in {item}")

        return item

    def clean_name(self, value):
        return value.replace("/n", "").strip()

    def clean_capital(self, value):
        return value.strip()

    def clean_population(self, value):
        return value.strip()

    def clean_data(self, value):
        return value.strip()


class CustomCsvItemExporter(CsvItemExporter):
    
    labels = ["Nome", "capital", "população", "área"]

    def _write_headers_and_set_fields_to_export(self, item):
        if self.include_headers_line:
            if not self.fields_to_export:
                # use declared field names, or keys if the item is a dict
                self.fields_to_export = ItemAdapter(item).field_names()
            if self.labels:
                fields = self.labels
            elif isinstance(self.fields_to_export, Mapping):
                fields = self.fields_to_export.values()
            else:
                fields = self.fields_to_export
            row = list(self._build_row(fields))
            self.csv_writer.writerow(row)
