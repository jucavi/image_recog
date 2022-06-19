import cv2
import pytesseract

CONTENT_FORMAT = {
    'DATE': {
        'rows': 1,
        'cols': 2,
        'k': 0.055,
        'offsetX': 0,
        'offsetY': 0,
        'positions': [1, 1],
        'keys': [
            ('channel_name', 'date')
        ]
    },
    'LEVELS': {
        'rows': 6,
        'cols': 3,
        'k': 0.05,
        'offsetX': 0,
        'offsetY': 0,
        'positions': [5, 10],
        'keys': [
            ('pd_High', 'pw_High', 'pm_High'),
            ('pd_VAH', 'pw_VAH', 'pm_VAH'),
            ('pd_POC', 'pw_POC', 'pm_POC'),
            ('pd_EQ', 'pw_EQ', 'pm_EQ'),
            ('pd_VAL', 'pw_VAL', 'pm_VAL'),
            ('pd_Low', 'pw_Low', 'pm_Low')
        ]
    },
    'OPEN': {
        'rows': 1,
        'cols': 3,
        'k': 0.05,
        'offsetX': 0,
        'offsetY': 30,
        'positions': [12, 12],
        'keys': [
            ('daily_open', 'weekly_open', 'monthly_open')
        ]
    },
    'CC': {
        'rows': 2,
        'cols': 2,
        'k': 0.05,
        'offsetX': 0,
        'offsetY': 0,
        'positions': [15, 16],
        'keys': [
            ('global_resistance', 'local_resistance'),
            ('global_support', 'local_support')
        ]
    },
    'MISCELLANEUSS': {
        'rows': 2,
        'cols': 2,
        'k': 0.05,
        'offsetX': 0,
        'offsetY': 0,
        'positions': [18, 19],
        'keys': [
            ('current_price', 'funding'),
            ('svwap', '15m_CVD_divergences')
        ]
    },
    'NPOCS': {
        'rows': 4,
        'cols': 2,
        'k': 0.05,
        'offsetX': 0,
        'offsetY': 30,
        'positions': [21, 24],
        'keys': [
            ('downside_daily', 'upside_daily'),
            ('downside_weekly', 'upside_weekly'),
            ('downside_monthly', 'upside_monthly'),
            ('downside_NSPOC', 'upside_NSPOC')
        ]
    }
}

class Report:
    def __init__(self, path, reverse=True, resize=None, content_format=CONTENT_FORMAT):
        """
        Args:
            path (str): Image path
            reverse (bool, optional): Invert colors. Defaults to True.
            resize (tuple, optional): (width, height). Defaults to None.
        """

        try:
            self.width, self.height = resize
        except:
            self.width, self.height = self.img.shape[:2]

        self.img = self.__cleanup(path, reverse)
        self.content_format = content_format


    def __cleanup(self, path, reverse):
        img = cv2.imread(path)
        # img = cv2.resize(img, (1250, 1810))
        img = cv2.resize(img, (self.width, self.height))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh, img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
        img = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        if reverse:
            img = 255 - img

        return img


    def __get_rows(self, start, end, k=0.05, offset=0):
        """Returns a list with cropped rows from start to end, in a shape of (width * k x height)

        Args:
            start (int): First row to include in the list (inclusive)
            end (int): Last row to include in the list (inclusive)
            k (float, optional): Multiplier. Defaults to 0.05.
            offset (int, optional): vertical offset. Defaults to 0.

        Returns:
            list: list of cropped rows
        """

        start_row, start_col = 0, 0
        end_row, end_col = offset, 0
        steep = self.width * k
        row_counter = 0
        rows = []

        while end_row < self.height and row_counter <= end:
            start_row, start_col = end_row, 0
            end_row, end_col = int(end_row + steep), int(self.height)
            cropped = self.img[start_row:end_row, start_col:end_col]
            if start <= row_counter:
                rows.append(cropped)
            row_counter += 1

        return rows


    def __get_columns(self, img, cols, offset=0):
        """Returns a list with cropped cols

        Args:
            cols (int): Number of columns

        Returns:
            list: List of cropped columns
        """

        start_row, start_col = 0, 0
        end_row, end_col = 0, 0
        steep = (self.height - offset) / (cols + 1)
        chunks = []

        for _ in range(cols):
            start_row, start_col = 0, end_col
            end_row, end_col = int(self.width), int(start_col + offset + steep)
            chunks.append(img[start_row:end_row, start_col:end_col])

        return chunks


    def parse_image(self):
        for _, segment in self.content_format.items():
            start, end = segment['positions']
            rows = self.__get_rows(start, end, k=segment['k'], offset=segment['offsetY'])

            for row, keys in zip(rows, segment['keys']):
                cols = self.__get_columns(row, segment['cols'], offset=segment['offsetX'])

                for col, attr in zip(cols, keys):
                    custom_config = r'--oem 3 --psm 6'
                    details = pytesseract.image_to_data(col, output_type=pytesseract.Output.DICT, config=custom_config, lang='eng')
                    setattr(self, attr, details['text'][-1].replace('$', ''))



if __name__ == '__main__':
    r = Report('images/image4.png', resize=(1250, 1810))
    r.parse_image()
    for i in r.__dict__:
        print(i, '=', getattr(r, i))