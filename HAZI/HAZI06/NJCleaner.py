import pandas as pd
import numpy as np

class NJCleaner:
    def __init__(self, path) -> None:
        self.path = path
        self.data = pd.read_csv(path)
    
    def order_by_scheduled_time(self) -> pd.DataFrame:
        order = self.data.sort_values(by=['scheduled_time'])
        return order


    def grep_df(self,save_csv_path):
        self.data = self.order_by_scheduled_time()
        self.data.to_csv(save_csv_path)

    def drop_columns_and_nan(in_df : pd.DataFrame) -> pd.DataFrame:
        out_df = in_df.copy()
        out_df.drop('from','to')
        out_df.dropna(axis=0)
        return out_df
    
    def convert_date_to_day(in_df : pd.DataFrame) -> pd.DataFrame:
        out_df = in_df.copy()
        out_df['day'] = pd.to_datetime(out_df['date']).dt.day_name()
        return out_df

    def convert_scheduled_time_to_part_of_the_day(in_df : pd.DataFrame) -> pd.DataFrame:
        out_df = in_df.copy()
        out_df['part_of_the_day'] = ''
        for i in range(len(out_df)):
            scheduledtime = out_df['scheduled_time'][i]
            if scheduledtime < '4:00':
                out_df['part_of_the_day'][i] = 'late_night'
                continue
            if scheduledtime < '8:00':
                out_df['part_of_the_day'][i] = 'early_morning'
                continue
            if scheduledtime < '12:00':
                out_df['part_of_the_day'][i] = 'morning'
                continue
            if scheduledtime < '16:00':
                out_df['part_of_the_day'][i] = 'afternoon'
                continue
            if scheduledtime < '20:00':
                out_df['part_of_the_day'][i] = 'evening'
                continue
            if scheduledtime <= '23:59':
                out_df['part_of_the_day'][i] = 'late_night'
                continue
        return out_df
    
    def convert_delay(self):
        out_df = self.data.copy()
        out_df['delay'] = out_df['delay_minutes'].apply(get_delay)

        def get_delay(delay):
            if delay>=5:
                return '1'
            return '0'
        
        return out_df
    
    