# Did you know The synology doesn't suppor webp or jfif? because I just find out.
- This Docker Image changes every webp and jfjf files to png type. if the webp picture is animated, it will be gonna changed to gif.
- you must set volume destination as "/target" in container.
- Every originl image gonna be backed up in "/target/.before_changed" + original directory path
- Thanks
