import os
import magic
import shutil

source_dir = "c:/users/omen/downloads"
dest_dirs = {
    "image" : "c:/users/omen/sorted_downs/pictures",
    "audio" : "c:/users/omen/sorted_downs/audio",
    "document" : "c:/users/omen/sorted_downs/documents",
    "app" : "c:/users/omen/sorted_downs/applications",
    "other" : "c:/users/omen/sorted_downs/others"
}

mime = magic.Magic(mime=True)

with os.scandir(source_dir) as entries:
    for entry in entries:
        if entry.is_file():
            file_path = os.path.join(source_dir, entry.name)
            
            mime_type = mime.from_file(file_path)
            main_type = mime_type.split("/")[0]
            
            if "pdf" in mime_type or "msword" in mime_type or "officedocument" in mime_type:
                main_type = "document"
            elif "x-dosexec" in mime_type:
                main_type = "app"
                
            dest_folder = dest_dirs.get(main_type, os.path.join(source_dir, "Other"))
            
            os.makedirs(dest_folder, exist_ok=True)
            
            shutil.move(file_path, os.path.join(dest_folder, entry.name))
            print(f"Moved: {entry.name} -> {dest_folder}/")
             