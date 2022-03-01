import pandas as pd
from glob import glob
import os

def delete_file_if_existent(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)

def get_gl_file_lists(csv_file):
    df = pd.read_csv(csv_file)
#     df_out = pd.DataFrame()
    
    cell_stat_names = []
    mask_names = []
    prob_map_names = []
    dataset_index = []
    
    col_headers = df.columns
    col_values = {}
    for col_header in col_headers:
        col_values[col_header] = []
    
    for index, row in df.iterrows():
        path = row.data_path
        subdirs = next(os.walk(path))[1]
        
        for subpath in subdirs:
            dataset_index.append(index)
            full_path = os.path.join(path, subpath)
#             print("full_path: " + full_path)
            cell_stat_name = glob(full_path+'/ExportedCellStats__*')[0]
            cell_stat_names.append(cell_stat_name)
            prob_map_name = glob(full_path+'/*__model_9e5727e4ed18802f4ab04c7494ef8992d798f4d64d5fd75e285b9a3d83b13ac9.tif')[0]
            prob_map_names.append(prob_map_name)
            mask_name = glob(full_path+'/ExportedCellMasks__*')[0]
            mask_names.append(mask_name)
            for col_header in col_headers:
                col_values[col_header].append(row[col_header])
    
#     print('mask_names:')
#     print(mask_names)
    
    df_result = pd.DataFrame({'cell_stats_path': cell_stat_names,
                      'mask_image_path': mask_names,
                      'probability_map_path': prob_map_names,
                      'dataset_index': dataset_index,
                     })

    for col_header in col_headers:
        df_result[col_header] = col_values[col_header]

    return df_result
#             print(cell_stat_name)
#         print(path)
#         print(subdirs)
#         print(glob(path))
    
    pass

def read_exported_cell_stats(csv_file):
    df = pd.read_csv(csv_file)
#     print(df)
    cell_stat_names = []
    mask_names = []
    prob_map_names = []
    dataset_index = []
    
    df_result = pd.DataFrame()
    
    col_headers = df.columns
    col_values = {}
    for col_header in col_headers:
        col_values[col_header] = []
    
    for index, row in df.iterrows():
        path = row.data_path
        print(f'path: {path}')
#         subdirs = next(os.walk(path))[1]
#         print(f'subdirs: {subdirs}')
        full_path = path
        dataset_index.append(index)
#         full_path = os.path.join(path, subpath)
        cell_stat_name = glob(full_path+'/ExportedCellStats__*')[0]
#         print(f'cell_stat_name: {cell_stat_name}')
        df_tmp = pd.read_csv(cell_stat_name, skiprows=4, delimiter=',')
#         print(f'df_tmp: {df_tmp}')
#         print(f'cell_stat_name: {cell_stat_name}')
#         cell_stat_names.append(cell_stat_name)
        for col_header in col_headers:
            df_tmp[col_header] = row[col_header]
#             print(f'col_header: {col_header}')
            col_values[col_header].append(row[col_header])
#         print(df_tmp)
        df_result = df_result.append(df_tmp)
#     print('mask_names:')
#     print(mask_names)
    
#     df_result = pd.DataFrame({'cell_stats_path': cell_stat_names,
#                       'mask_image_path': mask_names,
#                       'probability_map_path': prob_map_names,
#                       'dataset_index': dataset_index,
#                      })

#     for col_header in col_headers:
#         df_result[col_header] = col_values[col_header]
    df_result.loc[pd.isnull(df_result['type_of_end']), 'type_of_end'] = 'map'
    
    return df_result
