import re, sys
pattern = r"'entry_id' : '(\w+)'"

def get_video_download_link(save_resource_path):
    with open(save_resource_path, encoding='utf-8') as f:
        html_content = f.readlines()
    entry_id_arr = [l for l in html_content if "entry_id" in l]
    if len(entry_id_arr) == 1: 
        entry_id_str = entry_id_arr[0].strip()
        match = re.search(pattern, entry_id_str)
        if match:
            download_link = f'https://cdnapisec.kaltura.com/p/1329972/sp/132997200/playManifest/entryId/{match.group(1)}/format/download/protocol/https/flavorParamIds/0'
            print(f'Please download the video from the following link.\n{download_link}')
            return download_link
        else: 
            print("No match found")
    else: 
        print(f'there are {len(entry_id_arr)} found.')

if __name__ == '__main__':
    # Example: python .\src\get_video_download_link.py "C:\Users\herbe\Downloads\Project-Management - Module 7_files\saved_resource(1).html"
    # get_video_download_link(r"C:\Users\herbe\Downloads\Project-Management - Module 7_files\saved_resource(1).html")
    get_video_download_link(sys.argv[1])