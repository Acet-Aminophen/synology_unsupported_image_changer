from PIL import Image, ImageSequence
import shutil
import os


file_path = "/target"
file_types = ("webp", "jfif")


def is_animated(FilePath):
    try:
        mf = Image.open(FilePath)
        idx = 0
        for frame in ImageSequence.Iterator(mf):
            idx += 1
        if idx > 1:
            return True
        else:
            return False
    except:
        return False


for file in os.walk(file_path):
    for name in file[2]:
        if "@eaDir" in file[0]:
            continue
        if name.split(".")[-1] in file_types:
            org_path = file[0] + "/" + name
            backup_path = file_path + "/.before_changed/" + org_path[len(file_path) + 1:]
            if is_animated(org_path):
                new_path = file[0] + "/" + ".".join(name.split(".")[:-1]) + ".gif"
                im = Image.open(org_path)
                im.info.pop('background', None)
                im.save(new_path, 'gif', save_all=True)
            else:
                new_path = file[0] + "/" + ".".join(name.split(".")[:-1]) + ".png"
                im = Image.open(org_path).convert('RGB')
                im.save(new_path, 'png')
                pass
            os.makedirs(os.path.dirname("/".join(backup_path.split("/")[:-1]) + "/"), exist_ok=True)
            shutil.move(org_path, backup_path)
            print("DONE : " + org_path)

print("CLEAR")