import json
import gspread


class Sheet:
    def __init__(self):
        self.config = json.load(open('config.json', 'r'))
        self.gc = gspread.oauth()
        self.spreadsheet_key = self.config.get("SPREADSHEET_URL")
        self.ss = self.gc.open_by_url(self.spreadsheet_key)

    def search(self, search_term) -> list:
        cells = []
        for sheet in self.ss.worksheets():
            cell_list = sheet.findall(search_term)
            cells.extend(cell_list)

        columns = []
        for cell in cells:
            columns.append(cell.col)

        return columns


if __name__ == '__main__':
    s = Sheet()
    cols = s.search('USA')
    print(cols)
